"""
### CODE OWNERS: Demerrick Moton
### OBJECTIVE:
    Implementation of great_expectations for data_tools
### DEVELOPER NOTES:
Consider adding arbitrary fields to be used for custom metadata capture
(i.e. num_field1, num_field2, str_field1, str_field2, etc.). Then use labels
in the dataframe metadata to define the custom fields.
"""

import json
from pathlib import Path
from datetime import datetime
import logging
import os

# from great_expectations.dataset import SparkDFDataset
from google.cloud import storage
from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from pyspark.sql.window import Window

logging.basicConfig(
    format="%(asctime)s - %(message)s", level=os.environ.get("LOGLEVEL", "INFO")
)
LOGGER = logging.getLogger(__name__)

DEFAULT_RESULTS_FORMAT = "SUMMARY"

# ===========================================================


# class DataValidatorDataset:
#     """
#     A managed object representing a specific dataset to be validated
#     """

#     def __init__(
#         self, base_path: str, validation_path: str, dataframe: DataFrame
#     ) -> None:
#         self.dataframe = SparkDFDataset(dataframe)
#         self.validation_path = validation_path
#         self.base_path = base_path
#         self.expectations = self._read_validation_file()

#     def _read_validation_file(self):
#         validation_file = self._get_validation_path()

#         # Get expectations
#         try:
#             with open(validation_file, "r") as f:
#                 val_dic = json.load(f)
#             return val_dic["expectations"]
#         except Exception as e:
#             LOGGER.error(f"Error reading validation file: {e}")
#             return None

#     def _get_validation_path(self):
#         # Download from cloud storage
#         if self.base_path is not None:
#             try:
#                 validation_uri = self.base_path + self.validation_path
#                 bucket_name = self.base_path.split("/")[2]
#                 validation_file = self.validation_path.split("/")[-1]
#                 source_blob_name = "/".join(validation_uri.split("/")[3:])

#                 storage_client = storage.Client()
#                 bucket = storage_client.bucket(bucket_name)
#                 blob = bucket.blob(source_blob_name)
#                 blob.download_to_filename(validation_file)
#                 return validation_file
#             except Exception as error:
#                 LOGGER.warn("Unable to read validation file")
#                 LOGGER.error(error)
#                 return None
#         else:  # local file
#             return self.validation_path

# class DataValidator:
#     """
#     Object responsible for validating data
#     Args:
#         base_path(str): For local: None; For Cloud: gs:// path
#         sparkapp(SparkApp): Sparkapp instance
#     """

#     def __init__(self, sparkapp, base_path: str = None):
#         self.sparkapp = sparkapp
#         self.base_path = base_path
#         self.meta_df = None

#     def _validate_expectation(self, ge_df, expectation):
#         """
#         Validate the given dataset based on given expectations

#         Args:
#             ge_df (SparkDFDataset): Managed dataframe object used for validating dataset
#             expectation (dict): Dictionary of expectations (from json config)

#         Returns:
#             result: Dictionary of expectation results
#         """
#         exp_type = expectation["expectation_type"]
#         val_fun = getattr(ge_df, exp_type)
#         return val_fun(**expectation["kwargs"], result_format=DEFAULT_RESULTS_FORMAT)

#     def _save_validation_result(self, results):
#         # convert dictionary to dataframe
#         if len(results) == 0:
#             LOGGER.warning("No results to write")
#             return
#         results_df = self.sparkapp.createDataFrame(results).select(
#             F.col("table"),
#             F.col("script_type"),
#             F.col("validation"),
#             F.col("success"),
#             F.current_timestamp().alias("created_at"),
#         )

#         # write df to table
#         self.sparkapp.write_bq(df=results_df, dataset="meta", table="validations")

#     def create_validation_dataset(self, dataframe: DataFrame):
#         val_df = SparkDFDataset(dataframe)
#         return val_df

#     def validate_data(self, dataframe: DataFrame, validation_path: str):
#         """
#         Validate data based on validation configuration

#         Args:
#             dataframe (DataFrame): data to be vlaidated
#             validation_path (str): path to validation configuration
#         """
#         LOGGER.info(f"Start data validation with {validation_path}")

#         results = []
#         failed = []

#         def add_result(result):
#             """
#             Parse result and add to result/failed list

#             Args:
#                 result (dict): Expectation result

#             Returns:
#                 dict: Dictionary of useful elements of result
#             """
#             result_params = {
#                 "table": None,
#                 "validation": None,
#                 "success": None,
#             }

#             # assumes stem will take the form 'stage_risk' or 'import_appointments'
#             script = Path(validation_path).stem
#             script_type = script.split("_")[0]
#             table = script.split("_")[1]

#             result_params["table"] = table
#             result_params["script_type"] = script_type
#             result_params["validation"] = result["expectation_config"][
#                 "expectation_type"
#             ]
#             result_params["success"] = result["success"]

#             results.append(result_params)

#             # add to failed list if failed, unless overridden
#             if not result_params["success"]:
#                 meta = result["expectation_config"]["meta"]
#                 if "override" in meta:
#                     if meta["override"]:
#                         # skip is override is asserted
#                         return
#                 result["validation"] = result_params["validation"]
#                 failed.append(result)

#         # Create dataset and expectations
#         DVdataset = DataValidatorDataset(self.base_path, validation_path, dataframe)
#         dataset = DVdataset.dataframe
#         expectations = DVdataset.expectations
#         from pyspark.sql.utils import AnalysisException

#         # Validate expectations
#         for expectation in expectations:
#             try:
#                 result = self._validate_expectation(dataset, expectation)
#                 add_result(result)
#             except AnalysisException as exp:
#                 pass

#         LOGGER.info(f"Writing validation results to Meta dataset")
#         self._save_validation_result(results)

#         assert len(failed) == 0, f"Validation failures found: {failed}"

#         LOGGER.info(f"Finish data validation with {validation_path}")
#         return results

#     def _get_current_meta_value(self, _df, script_type, branch_name):
#         default_time = datetime(1900, 1, 1)

#         if set(("created_at", "updated_at")).issubset(set(_df.columns)):
#             # if created_at and updated_at columns exist, provide latest timestamp
#             meta_df = _df.select(
#                 F.lit(script_type).alias("script_type"),
#                 F.lit(branch_name).alias("branch_name"),
#                 F.lit(_df.count()).alias("count"),
#                 F.max("created_at").alias("latest_created"),
#                 F.max("updated_at").alias("latest_updated"),
#                 F.lit(datetime.now()).alias("created_at"),
#             )
#         else:
#             meta_df = _df.select(
#                 F.lit(script_type).alias("script_type"),
#                 F.lit(branch_name).alias("branch_name"),
#                 F.lit(_df.count()).alias("count"),
#                 F.lit(default_time).alias("latest_created"),
#                 F.lit(default_time).alias("latest_updated"),
#                 F.lit(datetime.now()).alias("created_at"),
#             ).limit(1)
#         return meta_df

#     def _get_previous_meta_values(
#         self,
#         table: str,
#         script_type: str,
#         branch_name: str = None,
#         dataset: str = "meta",
#     ):
#         # if the table doesn't currently exist in bq, use current_meta_df as previous_meta_df initially
#         # and upload as the initial table
#         if self.sparkapp.table_exists_in_bq(dataset=dataset, table=table):
#             LOGGER.info("Getting existing meta values")
#             # retrieve the last row of the table for the current script_type and branch_name

#             # retrieve the last row of the table for the current script_type and branch_name
#             existing_meta_all_df = self.sparkapp.read_bq(
#                 dataset=dataset,
#                 table=table,
#             )

#             if existing_meta_all_df.count() == 0:
#                 LOGGER.warning("No existing meta values found")
#                 return None
#         else:
#             LOGGER.info(
#                 f"Table {table} does not exist in {dataset}. Creating new table."
#             )
#             existing_meta_all_df = None

#         return existing_meta_all_df

#     def get_meta_table(
#         self,
#         df: DataFrame,
#         table: str,
#         script_type: str,
#         branch_name: str = None,
#         dataset: str = "meta",
#     ):
#         LOGGER.info(f"Generating meta table for {table}")
#         branch_name = branch_name or self.sparkapp.sparkapp_params["branch_name"]

#         # if no previous values, set current values as previous values
#         current_meta_df = self._get_current_meta_value(df, script_type, branch_name)
#         previous_meta_df = (
#             self._get_previous_meta_values(table, script_type, branch_name, dataset)
#             or current_meta_df
#         )

#         LOGGER.info("Prepare previous meta for comparison")
#         previous_meta_df.cache()
#         script_branch_window = Window.partitionBy("script_type", "branch_name").orderBy(
#             F.col("created_at").desc()
#         )
#         previous_meta_prep_df = previous_meta_df.select(
#             F.row_number().over(script_branch_window).alias("row_number"),
#             F.col("script_type"),
#             F.col("branch_name"),
#             F.col("count").alias("previous_count"),
#             F.col("latest_created").alias("previous_latest_created"),
#             F.col("latest_updated").alias("previous_latest_updated"),
#         ).where(F.col("row_number") == 1)

#         LOGGER.info("Comparing meta values for current and existing data")
#         comparison_df = current_meta_df.join(
#             previous_meta_prep_df, ["script_type", "branch_name"], "inner"
#         )

#         # check if comparison_df is empty or invalid

#         meta_df = comparison_df.select(
#             F.col("script_type"),
#             F.col("branch_name"),
#             F.col("count"),
#             F.col("latest_created"),
#             F.col("latest_updated"),
#             (F.col("count") - F.col("previous_count")).alias("new_records"),
#             F.datediff(F.col("latest_created"), F.col("previous_latest_created")).alias(
#                 "since_last_created"
#             ),
#             F.datediff(F.col("latest_updated"), F.col("previous_latest_updated")).alias(
#                 "since_last_updated"
#             ),
#             F.col("created_at"),
#         )

#         return meta_df

#     def has_new_data(
#         self,
#         df: DataFrame,
#         table: str,
#         script_type: str,
#         branch_name: str = None,
#         dataset: str = "meta",
#     ):
#         LOGGER.info(f"Checking if {table} has new data")
#         branch_name = branch_name or self.sparkapp.sparkapp_params["branch_name"]

#         meta_df = self.get_meta_table(df, table, script_type, branch_name, dataset)

#         # get metadata on data recency
#         new_records = meta_df.select(F.col("new_records")).collect()[0][0]
#         since_created = meta_df.select(F.col("since_last_created")).collect()[0][0]
#         since_updated = meta_df.select(F.col("since_last_updated")).collect()[0][0]

#         if not (new_records | since_created):
#             LOGGER.info(f"No new data found for {table}")
#             return False

#         return True
