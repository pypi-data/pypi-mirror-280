"""
### CODE OWNERS: Rick Moton
### OBJECTIVE:
    Handle schema manipulations
### DEVELOPER NOTES:
"""

import logging
import os
import pandas as pd
from pyspark.sql.types import (
    BooleanType,
    StringType,
    StructField,
    StructType,
    IntegerType,
    TimestampType,
    FloatType,
    DateType,
)

logging.basicConfig(
    format="%(asctime)s - %(message)s", level=os.environ.get("LOGLEVEL", "INFO")
)
LOGGER = logging.getLogger(__name__)

PG_SPARK_TYPEMAP = {
    "character varying": StringType(),
    "jsonb": StringType(),
    "uuid": StringType(),
    "timestamp without time zone": TimestampType(),
    "integer": IntegerType(),
    "boolean": BooleanType(),
    "float": FloatType(),
    "date": DateType(),
}

SPARK_BQ_TYPEMAP = {
    "StringType": "STRING",
    "VarcharType": "STRING",
    "CharType": "STRING",
    "ByteType": "BYTES",
    "ShortType": "INTEGER",
    "IntegerType": "INTEGER",
    "LongType": "BIGNUMERIC",
    "FloatType": "FLOAT",
    "DoubleType": "FLOAT",
    "DecimalType": "FLOAT",
    "BooleanType": "BOOLEAN",
    "TimestampType": "TIMESTAMP",
    "DateType": "DATE",
}

PG_SPARK_TYPE_MAP = {}

# ===========================================================


def convert_ints(pdf: pd.DataFrame, ref_df: pd.DataFrame):
    """
    Correct erroneous PostgreSQL int values back to int for Spark

    Args:
        pdf (pandas.DataFrame): Pandas dataframe
        ref_df (pandas.DataFrame): Reference dataframe with types
    """
    int_cols = list(ref_df[ref_df["data_type"] == "integer"].column_name)
    for col in int_cols:
        pdf[col] = pdf[col].fillna(-1).astype(pd.Int32Dtype())
    return pdf


def convert_uuids(pdf: pd.DataFrame, ref_df: pd.DataFrame):
    """
    Convert PostgreSQL UUIDs to strings so that they convert to Spark DFs nicely

    Args:
        pdf (pandas.DataFrame): Pandas dataframe
        ref_df (pandas.DataFrame): Reference dataframe with types
    """
    uuid_cols = list(ref_df[ref_df["data_type"] == "uuid"].column_name)
    for col in uuid_cols:
        pdf = pdf.astype({col: str})
    return pdf


class SchemaReader:
    """
    Utility for converting SQL file to Spark schema
    """

    def __init__(self):
        pass

    def find_type(self, data_type: str):
        """
        Resolves type mapping between spark and sql

        Args:
            data_type (str): Given SLQ data type

        Returns:
            [Spark DataType]: Equivalent Spark data type
        """
        if data_type in PG_SPARK_TYPEMAP.keys():
            return PG_SPARK_TYPEMAP[data_type]
        else:
            return StringType()

    def generate_schema(self, schema_df: pd.DataFrame) -> StructType:
        """
        Take database schema as a pandas dataframe and convert it to a Spark schema

        Args:
            schema_df (pd.DataFrame): Database schema as a pandas dataframe

        Returns:
            StructType: Spark schema
        """
        col_names = schema_df["column_name"]
        col_types = schema_df["data_type"]
        schema_ = []

        for n, t in zip(col_names, col_types):
            schema_.append(StructField(n, self.find_type(t), True))

        schema = StructType(schema_)
        return schema

    def get_bq_schema(self, file_path):
        df = pd.read_csv(file_path)
        df.columns = ["name", "type"]
        bq_schema_dict = df.to_dict("records")
        return bq_schema_dict
