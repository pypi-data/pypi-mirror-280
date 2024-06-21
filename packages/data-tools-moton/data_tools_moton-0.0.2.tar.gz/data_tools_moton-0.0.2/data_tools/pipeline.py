"""
### CODE OWNERS: Demerrick Moton
### OBJECTIVE:
    Abstract commonly used airflow operators and functions
### DEVELOPER NOTES:
  create_postpipeline_tasks() is currently used to signal the success
    or failure of a pipeline run. This is done by creating a checkfile in the
    ci bucket. This file is then read by Gitlab CI/CD to determine
    whether or not the pipeline succeeded or failed.
"""

import logging
import os
import json
from datetime import datetime
import functools

from pathlib import Path
from airflow.models import DAG
from airflow.providers.google.cloud.operators import dataproc
from airflow.providers.google.cloud.transfers.local_to_gcs import (
    LocalFilesystemToGCSOperator,
)
from airflow.operators.python import PythonOperator

from data_tools.config import load_config, update_config, init_resources
from data_tools.alerts import SlackAlert

PROJECT_SUFFIX = "/home/airflow/gcs"
BQ_JAR = "gs://spark-lib/bigquery/spark-bigquery-with-dependencies_2.12-0.27.0.jar"

logging.basicConfig(
    format="%(asctime)s - %(message)s", level=os.environ.get("LOGLEVEL", "INFO")
)
LOGGER = logging.getLogger(__name__)

# ===========================================================


class PipelineBuilder:
    def __init__(self, dag: DAG, project_uri: str, **kwargs):
        self.dag = dag
        self.tasks = {}

        self.params = {
            "project_id": "",
            "cluster_name": "",
            "branch_name": "",
            "bucket_name": "",
            "dags_uri": "",
            "region": "",
        }

        self.project_uri = project_uri
        self.project_name = kwargs.get("project_name") or Path(project_uri).name
        project_path = "/".join([PROJECT_SUFFIX, "dags", self.project_name])

        self.config_filepath = kwargs.get("config_filepath") or Path(
            "/".join([project_path, "configs", "pipeline.json"])
        )
        self.task_config_filepath = kwargs.get("task_config_filepath") or Path(
            "/".join([project_path, "configs", "tasks.json"])
        )
        self.cluster_name_filepath = kwargs.get("cluster_name_filepath") or Path(
            "/".join([project_path, "configs", "cluster_name.txt"])
        )
        self.branch_name_filepath = kwargs.get("branch_name_filepath") or Path(
            "/".join([project_path, "configs", "branch_name.txt"])
        )
        self.init_script_filepath = kwargs.get("init_script_filepath") or Path(
            "/".join([project_path, "configs", "init_action.sh"])
        )

        # set params from config (or use directly passed params)
        self.params["bucket_name"] = kwargs.get("bucket_name")
        self.params["project_id"] = kwargs.get("project_id")
        self.params["region"] = kwargs.get("region")
        self.params["dags_uri"] = kwargs.get("dags_uri")
        self.params["cluster_name"] = (
            kwargs.get("cluster_name") or self._get_cluster_name()
        )
        self.params = load_config(
            config_file=self.config_filepath,
            header="PipelineBuilder",
            config_dict=self.params,
        )
        LOGGER.info(f"Pipeline params: {self.params}")

        # set checkfile variables
        self.success_checkfile = f"{self.project_name}_success.txt"
        self.failure_checkfile = f"{self.project_name}_failure.txt"

    def _get_cluster_name(self) -> str:
        """
        Pull cluster name from cluster_name.txt file

        Returns:
            str: cluster_name
        """

        cluster_name = "at-cluster"
        try:
            cluster_name_file = open(self.cluster_name_filepath, "r")
            cluster_name = cluster_name_file.read()
        except:
            LOGGER.warning(
                f"Cluster name file {self.cluster_name_filepath} was not found"
            )
        finally:
            LOGGER.info(f"Cluster name: {cluster_name}")
            self.params["cluster_name"] = cluster_name
            return cluster_name

    def _get_branch_name(self) -> str:
        """
        Get branch name and set as config value

        Returns:
            str: branch name
        """

        try:
            branch_name_file = open(self.branch_name_filepath, "r")
            branch_name = branch_name_file.read()
        except:
            LOGGER.warning("Branch name file was not found")
        finally:
            LOGGER.info(f"Branch name: {branch_name}")
            self.params["branch_name"] = branch_name
            # update branch name to be passed to pipeline
            update_config(
                header="spark",
                option="branch_name",
                value=branch_name,
                config_file=self.task_config_filepath,
            )
            return branch_name

    def _get_cluster_config(self, project_id: str) -> dict:
        LOGGER.info("Creating cluster generator object")
        resources = init_resources(
            config_file=str(self.config_filepath),
            resources={
                "ClusterGenerator": dataproc.ClusterGenerator(
                    project_id=project_id,
                    init_actions_uris=[
                        str(self.init_script_filepath).replace(
                            "/home/airflow/gcs/dags", self.params["dags_uri"]
                        )
                    ],
                )
            },
        )

        assert (
            "ClusterGenerator" in resources
        ), "'ClusterGenerator' not found in resources"
        assert resources["ClusterGenerator"], "ClusterGenerator instance not created"

        return resources["ClusterGenerator"].make()

    def _get_args(self, header) -> list:
        """
        Parse the Spark aruguments in the json config file

        Returns:
            args: Arguments for Spark instance
        """
        LOGGER.info(f"Getting args for {header}")
        args_dict = load_config(header=header, config_file=self.task_config_filepath)
        assert len(args_dict) > 0, f"No args found for {header}"
        args = [json.dumps(args_dict)]
        return args, args_dict

    def _write_checkfile(
        self, checkfile: str, checkfile_type: str, message: str = None
    ) -> None:
        """
        Write a checkfile to the local filesystem
        """
        assert checkfile_type in [
            "success",
            "failure",
        ], f"Invalid checkfile type: {checkfile_type}. Must be 'success' or 'failure'."

        current_date_utc = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task_list = {task_name for (task_name, task) in self.tasks.items()}
        message = (
            message
            or f"""
            result: {checkfile_type}
            time: {current_date_utc}
            tasks run: {task_list}
        """
        )
        with open(checkfile, "w") as f:
            f.write(message)

    def build_create_cluster_task(
        self,
        dag: DAG = None,
        project_id: str = None,
        region: str = None,
        cluster_name: str = None,
        cluster_config: dict = None,
        **kwargs,
    ) -> dataproc.DataprocCreateClusterOperator:
        """
        Build a DataprocCreateClusterOperator task for creating a cluster

        Args:
            dag (DAG, optional): Airflow dag. Defaults to None.
            project_id (str, optional): GCP project id. Defaults to None.
            region (str, optional): GCP region. Defaults to None.
            cluster_name (str, optional): _description_. Defaults to None.
            cluster_config (dict, optional): _description_. Defaults to None.

        Returns:
            dataproc.DataprocCreateClusterOperator: _description_
        """
        dag = dag or self.dag
        project_id = project_id or self.params["project_id"]
        region = region or self.params["region"]
        cluster_name = cluster_name or self.params["cluster_name"]
        cluster_config = self._get_cluster_config(project_id)

        LOGGER.info(f"Creating create_cluster task for {cluster_name}... ")
        create_cluster = dataproc.DataprocCreateClusterOperator(
            task_id="create_cluster",
            dag=self.dag,
            project_id=project_id,
            region=region,
            cluster_name=cluster_name,
            cluster_config=cluster_config,
            use_if_exists=False,
            **kwargs,
        )

        return create_cluster

    def build_delete_cluster_task(
        self,
        dag: DAG = None,
        project_id: str = None,
        region: str = None,
        cluster_name: str = None,
        trigger_rule: str = "all_done",
        **kwargs,
    ) -> dataproc.DataprocDeleteClusterOperator:
        """
        Build a DataprocDeleteClusterOperator task for deleting a cluster

        Args:
            dag (DAG, optional): _description_. Defaults to None.
            project_id (str, optional): _description_. Defaults to None.
            region (str, optional): _description_. Defaults to None.
            cluster_name (str, optional): _description_. Defaults to None.
            trigger_rule (str, optional): _description_. Defaults to "all_done".

        Returns:
            dataproc.DataprocDeleteClusterOperator: _description_
        """
        dag = dag or self.dag
        project_id = project_id or self.params["project_id"]
        region = region or self.params["region"]
        cluster_name = cluster_name or self.params["cluster_name"]

        LOGGER.info(f"Creating delete_cluster task for {cluster_name}... ")
        delete_cluster = dataproc.DataprocDeleteClusterOperator(
            task_id="delete_cluster",
            dag=dag,
            project_id=project_id,
            region=region,
            cluster_name=cluster_name,
            trigger_rule=trigger_rule,
            **kwargs,
        )

        return delete_cluster

    def build_pyspark_task(
        self,
        task_id: str,
        dag: DAG = None,
        project_id: str = None,
        region: str = None,
        cluster_name: str = None,
        args: list = [],
        args_key: str = None,
        task_params: dict = None,
        script_uri: str = None,
        dependencies: list = [],
        include_dependencies: bool = True,
        job_params: dict = {},
        pyspark_params: dict = {},
    ) -> dataproc.DataprocSubmitJobOperator:
        """
        Build a DataprocSubmitJobOperator task for running a pyspark script

        Args:
            task_id (str): Airflow task id.
            dag (DAG, optional): Dag from which the task is run. Defaults to None.
            project_id (str, optional): GCP project id. Defaults to None.
            region (str, optional): GCP region. Defaults to None.
            cluster_name (str, optional): Randomized name of the cluster. Defaults to None.
            args (list, optional): Arguments for the task. Defaults to [].
              e.g. ['{"master": "yarn", "app_name": "at-test"}']
            args_key (str, optional): Key for the task arguments in config. Defaults to None.
            task_params (dict, optional): Parameters for the script path and dependencies. Defaults to None.
              e.g. {
                     "script_path": "analytics_pipeline/scripts/import_script.py",
                     "dependencies": ["task1", "task2"]
                   }
            script_uri (str, optional): URI for the script. Defaults to None.
            dependencies (list, optional): List of dependencies. Defaults to [].
            include_dependencies (bool, optional): Whether or not to include dependencies with parent task. Defaults to True.
            pyspark_params (dict, optional): Parameters for the pyspark job. Defaults to {}.
            job_params (dict, optional): Parameters for the job. Defaults to {}.

        Returns:
            dataproc.DataprocSubmitJobOperator: _description_
        """
        assert task_id and type(task_id) == str, "Valid task_id string must be provided"

        if task_id in self.tasks:
            LOGGER.info(f"Rebuilding task {task_id}")
        else:
            LOGGER.info(f"Building task {task_id}")

        # allow for caller to customize/override params
        dag = dag or self.dag
        project_id = project_id or self.params["project_id"]
        region = region or self.params["region"]
        cluster_name = cluster_name or self.params["cluster_name"]

        args_header = args_key or "spark"
        spark_args = args or self._get_args(args_header)[0]
        task_params = task_params or self._get_args(task_id)[1]

        job_id = f"{task_id}-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        script_uri = script_uri or "/".join(
            [self.project_uri, task_params["script_path"]]
        )
        include_dependencies = (
            task_params.get("include_dependencies") or include_dependencies
        )
        dependencies = dependencies or task_params["dependencies"]

        pyspark_task = dataproc.DataprocSubmitJobOperator(
            task_id=task_id,
            region=region,
            job={
                "reference": {"job_id": job_id, "project_id": project_id},
                "placement": {"cluster_name": cluster_name},
                "pyspark_job": {
                    # will be stored in gs://[composer_bucket]/dags/project_name/scripts/[script_name]
                    "main_python_file_uri": script_uri,
                    "args": spark_args,
                    "jar_file_uris": [BQ_JAR],
                    **pyspark_params,
                },
                **job_params,
            },
        )

        # build and load dependencies
        if include_dependencies == True and len(dependencies) > 0:
            for dep in dependencies:
                if dep in self.tasks:
                    LOGGER.info(f"Dependency {dep} already added to pipeline")
                    pyspark_task.set_upstream(self.tasks[dep])
                else:
                    LOGGER.info(f"Adding dependency: {dep} to {task_id}")
                    dep_tasks = self.build_pyspark_task(task_id=dep)
                    pyspark_task.set_upstream(dep_tasks)

        # add task to builder's dictionary of tasks
        LOGGER.info(f"Adding task: {task_id} to pipeline")
        self.tasks[task_id] = pyspark_task

        return pyspark_task

    def build_write_checkfile_tasks(
        self, dag: DAG = None
    ) -> (PythonOperator, PythonOperator):
        """
        Build tasks for writing success and failure checkfiles

        Args:
            dag (DAG, optional): Dag from which the task is run. Defaults to None.

        Returns:
            Tuple(PythonOperator, PythonOperator): (write_success_checkfile, write_failure_checkfile)
        """
        dag = dag or self.dag
        write_success_checkfile = PythonOperator(
            task_id="write_success_checkfile",
            python_callable=functools.partial(
                self._write_checkfile,
                checkfile=self.success_checkfile,
                checkfile_type="success",
            ),
            dag=dag,
            trigger_rule="all_success",
        )

        write_failure_checkfile = PythonOperator(
            task_id="write_failure_checkfile",
            python_callable=functools.partial(
                self._write_checkfile,
                checkfile=self.failure_checkfile,
                checkfile_type="failure",
            ),
            dag=dag,
            trigger_rule="one_failed",
        )
        return write_success_checkfile, write_failure_checkfile

    def build_upload_checkfile_tasks(
        self, ci_dir: str, dag: DAG = None, bucket_name: str = None
    ) -> (LocalFilesystemToGCSOperator, LocalFilesystemToGCSOperator):
        """
        Build tasks for uploading success and failure checkfiles to GCS

        Args:
            ci_dir (str): Defines where Tools or pipline
            dag (DAG, optional): Dag from which the task is run. Defaults to None.

        Returns:
            Tuple(LocalFilesystemToGCSOperator, LocalFilesystemToGCSOperator): (upload_success_checkfile, upload_failure_checkfile)
        """
        dag = dag or self.dag
        bucket_name = bucket_name or self.params["bucket_name"]

        upload_success_checkfile = LocalFilesystemToGCSOperator(
            task_id="upload_success_checkfile",
            src=self.success_checkfile,
            dst="/".join(["ci", ci_dir, self.success_checkfile]),
            bucket=bucket_name,
        )
        upload_failure_checkfile = LocalFilesystemToGCSOperator(
            task_id="upload_failure_checkfile",
            src=self.failure_checkfile,
            dst="/".join(["ci", ci_dir, self.failure_checkfile]),
            bucket=bucket_name,
        )
        return upload_success_checkfile, upload_failure_checkfile

    def build_summary_alert_task(self, alert, dag: DAG = None) -> None:
        """
        Build a task for sending a summary alert

        Args:
            alert (_type_): _description_
            dag (DAG, optional): _description_. Defaults to None.
        """

        def summary_alert_callable():
            pass

        dag = dag or self.dag
        generate_run_summary = PythonOperator(
            task_id="generate_run_summary",
            python_callable=summary_alert_callable,
            dag=dag,
            on_success_callback=alert.pipeline_summary_alert,
            trigger_rule="all_done",
        )

        return generate_run_summary
