"""
### CODE OWNERS: Demerrick Moton
### OBJECTIVE: 
### DEVELOPER NOTES:
"""
import logging
import os

from airflow.operators.slack_operator import SlackAPIPostOperator
from airflow.models import DAG

SLACK_TOKEN = os.getenv("SLACK_TOKEN", None)
SLACK_ALERT_CHANNEL = "$etl-alerts"

logging.basicConfig(
    format="%(asctime)s - %(message)s", level=os.environ.get("LOGLEVEL", "INFO")
)
LOGGER = logging.getLogger(__name__)

GREEN_CIRCLE = ":large_green_circle:"
RED_CIRCLE = ":large_red_circle:"
GREEN_SQUARE = ":green_square:"
RED_SQUARE = ":red_square:"

# ===========================================================


class SlackAlert:
    """This is the task alert object that will be passed to indicate pipeline failure, successes, and warnings"""

    def __init__(self, branch=None, **kwargs):
        self.branch = branch

    def task_failure_slack_alert(self, context):
        """
        task_fail_slack_alert

        Args:
            context: context passed by on_failure_callback which includes dag parameters

        Returns:
            SlackAPIPostOperator: execution of SlackAPIPostOperator
        """
        LOGGER.info("Alerting user of task failure")
        failure_message = f"""
            :red_circle: *Task Failed*
----------------------------------------
*Task*: {context.get('task_instance').task_id}
*Dag*: {context.get('task_instance').dag_id}
*Branch*: {self.branch}
*Execution Date*: {context.get('execution_date')}
*Log URL*: {context.get('task_instance').log_url}
            """

        failure_alert = SlackAPIPostOperator(
            task_id="task_fail_slack_alert",
            token=SLACK_TOKEN,
            text=failure_message,
            username="airflow",
            channel=SLACK_ALERT_CHANNEL,
        )
        return failure_alert.execute(context=context)

    def task_warning_slack_alert(self, message, context):
        """
        task_warning_slack_alert

        Args:
            context: context passed by on_failure_callback which includes dag parameters

        Returns:
            SlackAPIPostOperator: execution of SlackAPIPostOperator
        """
        warning_message = f"""
            :large_yellow_circle: *Task Warning*
----------------------------------------
*Message*: {message}

*Task*: {context.get('task_instance').task_id}
*Dag*: {context.get('task_instance').dag_id}
*Execution Date*: {context.get('ts')}
*Log URL*: {context.get('task_instance').log_url}
            """
        warning_slack_alert = SlackAPIPostOperator(
            task_id="warning_slack_alert",
            token=SLACK_TOKEN,
            text=warning_message,
            username="airflow",
            channel=SLACK_ALERT_CHANNEL,
        )
        return warning_slack_alert.execute(context=context)

    def pipeline_summary_alert(self, context):
        """
        Summary of what tasks pass/failed in the pipeline

        Args:
            context: context passed by on_success_callback which includes dag parameters

        Returns:
            SlackAPIPostOperator: execution of SlackAPIPostOperator
        """

        LOGGER.info("Generating summary of tasks")

        dagrun: DAG = context["dag_run"]
        tasks = {}
        for ti in dagrun.get_task_instances():
            if "checkfile" in ti.task_id:
                continue
            tasks[ti.task_id] = ti.state
        tasks.pop("generate_run_summary")

        is_pipeline_successful = set(list(tasks.values())) == set(
            {"success"}
        )  # failed if any tasks isn't successful
        dag_status = (
            ":large_green_circle:  *Pipeline Succeeded*"
            if is_pipeline_successful
            else ":red_circle:  *Pipeline Failed*"
        )
        success_message = f"""
            {dag_status}
----------------------------------------
*Dag*: {context.get('dag').dag_id}
*Execution Date*: {context.get('ts')}

*Tasks*
----------------------------------------
"""
        for task_name, task_status in tasks.items():
            icon = (
                ":small_green_square:"
                if task_status == "success"
                else ":small_red_square:"
            )
            success_message = success_message + f"{icon}  *{task_name}*\n"

        success_alert = SlackAPIPostOperator(
            task_id="dag_success_slack_alert",
            token=SLACK_TOKEN,
            text=success_message,
            username="airflow",
            channel=SLACK_ALERT_CHANNEL,
        )
        return success_alert.execute(context=context)
