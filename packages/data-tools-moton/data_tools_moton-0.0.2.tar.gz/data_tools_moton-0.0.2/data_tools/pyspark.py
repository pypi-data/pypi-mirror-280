"""
### CODE OWNERS: Demerrick Moton
### OBJECTIVE:
    Create high-level constructs for implementing and managing ETL processes
### DEVELOPER NOTES:
"""

import json
import random
import logging
import os

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as F
from pyspark.context import SparkContext
from pyspark.conf import SparkConf
from pathlib import Path

from .config import load_config
from .io.db import DBConnector
from .utils.schema import SchemaReader, convert_ints, convert_uuids
from .utils.secrets import SecretManger
# from .validation import DataValidator

logging.basicConfig(
    format="%(asctime)s - %(message)s", level=os.environ.get("LOGLEVEL", "INFO")
)
LOGGER = logging.getLogger(__name__)

CURRENT_DIR = Path(__file__).parent
LOCAL_BQ_JAR = str(
    CURRENT_DIR / "io/spark_bq/spark-bigquery-with-dependencies_2.12-0.27.0.jar"
)
BQ_JAR = "gs://spark-lib/bigquery/spark-bigquery-with-dependencies_2.12-0.27.0.jar"

DEFAULT_BQ_WRITE_OPTIONS = {
    # "enableModeCheckForSchemaFields": False,
    # "writeMethod": "direct",
    # "allowFieldAddition": True
}
DEFAULT_BQ_READ_OPTIONS = {
    "project": "",
    "table": "",
}

# ===========================================================


class SparkApp(SparkSession):
    def __init__(
        self,
        args: str = None,
        conf: SparkConf = None,
        local: bool = False,
        bq_key: str = None,
        log_level: str="WARN"
    ):
        self.sparkapp_params = {
            "master": "yarn",
            "app_name": "",
            "temp_bucket_name": "",
            "project_id": "",
            "db_connection_name": "",
            "db_user": "",
            "db_name": "",
            "db_connection_string": "",
            "omit_db": False,
            "omit_bq": False,
            "secret_id": "",
            "version_id": "latest",
            "branch_name": "",
            "capture_metadata": False,
        }

        self.db_connectors = {}
        self.db_connector = None
        self.schema_reader = None
        self.secret_manager = None
        self.db_params = None

        if local:
            LOGGER.info("Initializing schema reader")
            self.schema_reader = SchemaReader()

            LOGGER.info("Initializing validator client")
            # self.validator_client = DataValidator(base_path=None, sparkapp=self)

            super().__init__(self._create_local_spark_context(bq_key=bq_key, conf=conf))
        else:
            if not args:
                LOGGER.warn("No SparkApp arguments were provided")
                return

            # load configuration arguments from 'args'
            self._load_args(args)
            super().__init__(self._create_spark_context(conf))

            LOGGER.info("Initializing schema reader")
            self.schema_reader = SchemaReader()

            LOGGER.info("Initializing secret manager")
            self.secret_manager = SecretManger(
                project_id=self.sparkapp_params["project_id"],
                secret_id=self.sparkapp_params["secret_id"],
                version_id=self.sparkapp_params["version_id"],
            )

            LOGGER.info("Initializing validator client")
            bucket_uri = self.sparkapp_params.get("bucket_uri")
            # self.validator_client = DataValidator(base_path=bucket_uri, sparkapp=self)

            LOGGER.info("Setting database parameters")
            assert self.sparkapp_params[
                "version_id"
            ], "Secret version id must be provided (for database params)"
            self.db_params = self.secret_manager.get_database_params(
                version_id=self.sparkapp_params["version_id"]
            )

        # set logging level
        self.sparkContext.setLogLevel(log_level)

    def __eq__(self, other):
        assert getattr(other, "app_name"), "Object {} is incompatible".format(other)
        assert other.app_name, "Object {} is not properly initialized".format(other)
        return self.app_name == other.app_name

    def __ne__(self, other):
        assert getattr(other, "app_name"), "Object {} is incompatible".format(other)
        assert other.app_name, "Object {} is not properly initialized".format(other)
        return self.app_name != other.app_name

    def _get_rand_num(self):
        return str(random.randrange(1, 420, 1))

    def _load_args(self, args: str):
        """
        Load dictionary-like string to be parsed into Spark configuration

        Args:
            args (str): dictionary-like string
        """
        args_dict = json.loads(args)
        self.sparkapp_params = {**self.sparkapp_params, **args_dict}

    def _create_spark_context(self, conf: SparkContext):
        LOGGER.info("Creating Spark Context")
        app_name = self.sparkapp_params["app_name"]
        master = self.sparkapp_params["master"]
        rand_num = self._get_rand_num()
        app_name = f"{app_name}_{rand_num}"
        conf = conf or SparkConf()
        conf.set("spark.jars", BQ_JAR)
        conf.set("temporaryGcsBucket", self.sparkapp_params["temp_bucket_name"])
        conf.set("spark.sql.legacy.parquet.int96RebaseModeInRead", "CORRECTED")
        conf.set("spark.sql.legacy.parquet.int96RebaseModeInWrite", "CORRECTED")
        conf.set("spark.sql.legacy.parquet.datetimeRebaseModeInRead", "CORRECTED")
        conf.set("spark.sql.legacy.parquet.datetimeRebaseModeInWrite", "CORRECTED")
        spark_context = SparkContext(master=master, appName=app_name, conf=conf)
        return spark_context

    def _create_local_spark_context(self, bq_key: str = None, conf: SparkConf = None):
        """
        Initialize a local SparkApp instance. Useful for quick debugging.

        Args:
            config_file (Union[Path, str]): Path to local configuration file
        Returns:
            ciq_pyspark.SparkApp: SparkApp instance
        """
        LOGGER.info("Creating Spark Context")

        # check that Spark BQ jar is up to date
        # print current auth and project according to gsutil
        app_name = "local_" + str(random.randrange(1, 420, 1))
        conf = conf or SparkConf()
        conf.set("spark.jars", LOCAL_BQ_JAR)

        if bq_key:
            assert Path(
                bq_key
            ).exists(), (
                "BigQuery json key was not found. Cannot start local pyspark instance"
            )
            conf.set("credentialsFile", bq_key)

        spark_context = SparkContext(
            master="local",
            appName=app_name,
            conf=conf,
        )
        return spark_context

    def _setup_db_connector(self, **db_kwargs):
        LOGGER.info("Initializing database instance")
        if "db_name" in db_kwargs:
            db_name = db_kwargs["db_name"]
            if db_name in self.db_connectors:
                self.db_connector = self.db_connectors[db_name]
            else:
                self.db_connector = DBConnector(
                    user=self.sparkapp_params["db_user"], **db_kwargs
                )
            assert self.db_connector, "Database is not currently connected"
            self.db_connectors[db_name] = self.db_connector
        else:
            LOGGER.error(
                "Connection name/string and database name needed to create database connection"
            )

    def read_csv(self, path: str, header: bool = True, **kwargs) -> DataFrame:
        """
        Convert csv file into Pyspark dataframe

        Args:
            path (str): Path to csv file
            header (bool, optional): [description]. Defaults to True.

        Returns:
            DataFrame: Pyspark dataframe
        """
        LOGGER.info("Loading table {path} from csv")
        _df = self.read.csv(path, header=header, **kwargs)
        LOGGER.info("Table %s loaded from csv", path)
        return _df

    def read_db(
        self,
        table: str,
        columns: list = ["*"],
        limit: int = None,
        namespace: str = "public",
        **db_kwargs,
    ) -> DataFrame:
        """
        Convert database table into Pyspark dataframe

        Args:
            table (str): Table name
            columns (list, optional): List is columns to read. Defaults to ["*"].
            db_name (str): Name of database to be queried
            limit (int, optional): Maximum number of columns to read at once. Defaults to None.
            namespace (str, optional): Schema to be used. Deaults to public
            db_kwargs:
                connection_name (str, optional): Cloud SQL database connection string. Defaults to None.
                user (str, optional): Database username. Defaults to None.
                db_name (str, optional): Name of database. Defaults to None.
                password (str, optional): Password for database user. Defaults to None.
                connection_string (str, optional): Custom connection string to pass to Sqlalchemy. Defaults to None.
                engine (sqlalchemy.engine.Engine, optional): Pregenerated Sqlalchemy engine. Defaults to None.
        Returns:
            DataFrame: Spark dataframe of database table
        """
        LOGGER.info("Creating DB connection")
        # create a distinct db connector per db
        self._setup_db_connector(**db_kwargs)

        LOGGER.info("Loading table %s from database", table)
        if limit and limit > 0:
            # read table with limit
            limit_clause = f" limit {limit}"
            pdf = self.db_connector.read_table(
                table_name=table,
                columns=columns,
                limit_clause=limit_clause,
                namespace=namespace,
            )
        else:
            # read table w/o limit
            pdf = self.db_connector.read_table(
                table_name=table, columns=columns, namespace=namespace
            )

        LOGGER.info("Loading schema for table %s", table)
        schema_df = self.db_connector.read_schema_df(
            table_name=table, columns=columns, namespace=namespace
        )
        schema = self.schema_reader.generate_schema(schema_df)

        cols = list(pdf.columns)
        schema_cols = schema_df["column_name"]
        LOGGER.debug(f"Columns {cols} \n Schema {schema_cols}")

        LOGGER.info("Convert UUIDs to strings")
        pdf = convert_uuids(pdf=pdf, ref_df=schema_df)
        pdf = convert_ints(pdf=pdf, ref_df=schema_df)

        LOGGER.info("Creating dataframe from db table {}".format(table))
        _df = self.createDataFrame(pdf, schema)

        LOGGER.info("Table %s loaded from database", table)

        return _df

    def read_bq(self, dataset: str = None, table: str = None, **options) -> DataFrame:
        """
        Convert BigQuery table to a Pyspark dataframe

        Args:
            dataset (str): Name if BigQuery dataset
            table (str): Name of BigQuery table
        Returns:
            DataFrame: Pyspark dataframe
        """

        DEFAULT_BQ_READ_OPTIONS = {
            "project": f"{self.sparkapp_params['project_id']}",
            "table": f"{dataset}.{table}",
        }

        options = options or DEFAULT_BQ_READ_OPTIONS
        LOGGER.info(f"{options}")

        LOGGER.info(f"Loading table {dataset}.{table} from BigQuery")
        _df = self.read.format("bigquery").options(**options).load()

        LOGGER.info("Table %s was loaded from BigQuery", table)
        return _df

    def table_exists_in_bq(self, dataset: str, table: str) -> bool:
        """
        Show whether the table is, in fact, available in BigQuery

        Args:
            dataset (str): table dataset name
            table (str): table name

        Returns:
            bool: The table is in BigQuery
        """
        try:
            _df = self.read_bq(dataset=dataset, table=table)
            return True
        except Exception as e:
            return False

    def read_json(self, path: str):
        LOGGER.info("Loading json from {}".format(path))
        _df = self.read.json(path)
        return _df

    def write_csv(self, df: DataFrame, path: str, sep: str = ","):
        LOGGER.info("Writing table {} to csv".format(path))
        df = self.toPandas()
        df.to_csv(path)

    def write_json(self, path):
        LOGGER.info("Writing table {} to json".format(path))
        _df = self.toPandas()
        self.write.json("path")

    def write_bq(
        self,
        df: DataFrame,
        dataset: str,
        table: str,
        save_mode: str = "overwrite",
        **options,
    ):
        """
        Save Pyspark dataframe to BigQuery

        Args:
            df (DataFrame): Pyspark dataframe
            dataset (str): Name of BigQuery dataset
            table (str): Name of BigQuery table
            save_mode (str, optional): Spark overwrite policy[append, errorifexists, ignore, overwrite]. Defaults to "overwrite".
        """

        options = options or DEFAULT_BQ_WRITE_OPTIONS
        LOGGER.info(f"{options}")

        LOGGER.info("Writing table {} to BigQuery".format(table))
        try:
            df.write.format("bigquery").option(
                "table", "{}.{}".format(dataset, table)
            ).options(**options).mode(saveMode=save_mode).save()
        except Exception as e:
            LOGGER.exception(f"Error writing table {table} to BigQuery: {e}")

        # capture and write metadata, if applicable
        # if self.sparkapp_params["capture_metadata"]:
        #     LOGGER.info("Writing metadata to BigQuery")
        #     meta_df = self.validator_client.get_meta_table(
        #         df=df,
        #         table=table,
        #         script_type=dataset,
        #         branch_name=self.sparkapp_params["branch_name"],
        #         dataset="meta",
        #     )
        #     # prevent infinite recursion
        #     self.sparkapp_params["capture_metadata"] = not self.sparkapp_params[
        #         "capture_metadata"
        #     ]
        #     self.write_bq(df=meta_df, dataset="meta", table=table, save_mode="append")
        #     self.sparkapp_params["capture_metadata"] = not self.sparkapp_params[
        #         "capture_metadata"
        #     ]

    def write_db(self, df: DataFrame, db: DBConnector, table_name: str):
        db.write_table(df, table_name=table_name)


# PySpark Tools


def replace_values(
    df: DataFrame, columns: list, replace: dict, inverse=False
) -> DataFrame:
    """
    Replace values for certain columns

    Args:
        df (DataFrame): DataFrame to modify values
        columns (list): Columns to apply replacement
        replace (dict): Dictionary of replacements

    Returns:
        DataFrame: Modified dataframe
    """
    assert columns and len(columns) > 0, "No columns provided to replace values"
    assert replace, "Replacement dictionary must be populated"

    for col in columns:
        if inverse:
            # IF NOT THESE VALUES, REPLACE
            replace_vals = list(replace.values())

            assert (
                len(set(replace_vals)) == 1
            ), "Only one value allowed for inverse replacement"
            replace_val = replace_vals[0]
            replace_keys = list(replace.keys())

            df = df.withColumn(
                col,
                F.when(~F.col(col).isin(replace_keys), F.lit(replace_val)).otherwise(
                    F.col(col)
                ),
            )
        else:
            for orig_val, new_val in replace.items():
                # IF THESE VALUES, REPLACE
                df = df.withColumn(
                    col,
                    F.when(F.col(col) == orig_val, F.lit(new_val)).otherwise(
                        F.col(col)
                    ),
                )
    return df


def count_check(dataset: str, table: str, sparkapp: SparkApp):
    sparkapp.load_bq(
        dataset=dataset,
        table=table,
    )


def view(self, df: DataFrame, nrows: int = 420):
    """
    Launch a PyQT5 table of the dataframe

    Args:
        nrows (int): Number of rows to print
    """
    pass
