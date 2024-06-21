"""
### CODE OWNERS: Demerrick Moton
### OBJECTIVE:
    Connect and manage common database functionality
### DEVELOPER NOTES: 
 - Assuming PostgresSQL as only database option
 - Can connect during or after DBConnector instantiation
 - Four ways to connect
    1. Provide connection string directly
    2. IAM connection with connection name, db name, and username
    3. Standard connection with connection name, username, and password
    4. Provide sqlalchemy engine directly
 - To connect other DBs in the future... DBConnector -> [PGConnector/MYSQL/...]
"""

import logging
import os

import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import pg8000
from google.cloud.sql.connector import connector
from google.cloud.sql.connector import IPTypes

logging.basicConfig(
    format="%(asctime)s - %(message)s", level=os.environ.get("LOGLEVEL", "INFO")
)
LOGGER = logging.getLogger(__name__)

# ===========================================================


class DBConnector:
    def __init__(
        self,
        connection_name: str = None,
        user: str = None,
        db_name: str = None,
        password: str = None,
        connection_string: str = None,
        engine: sqlalchemy.engine.Engine = None,
    ):
        """
        Database Connector for database I/O

        Args:
            connection_name (str, optional): Cloud SQL database connection string. Defaults to None.
            user (str, optional): Database username. Defaults to None.
            db_name (str, optional): Name of database. Defaults to None.
            password (str, optional): Password for database user. Defaults to None.
            connection_string (str, optional): Custom connection string to pass to Sqlalchemy. Defaults to None.
            engine (sqlalchemy.engine.Engine, optional): Pregenerated Sqlalchemy engine. Defaults to None.
        """
        LOGGER.info("instantiating database connector...")
        self.connection_name = connection_name
        self.db_name = db_name
        self.user = user
        self.password = password
        self.connection_string = connection_string
        self.engine = engine

        if self._check_connection_method() == "engine":
            LOGGER.info(
                "Using provided SQLAlchemy Engine to connect database connector"
            )
        elif self._check_connection_method() == "connection_string":
            LOGGER.info(
                "Using provided SQLAlchemy connection string to connect database connector"
            )
            self.connection_string = connection_string
            self.engine = create_engine(self.connection_string)
        elif self._check_connection_method() == "standard":
            LOGGER.info(
                "Using standard connection method (uname/pass) to connect database connector"
            )
            self.db_connect()
        elif self._check_connection_method() == "iam":
            LOGGER.info("Using Cloud IAM to connect database connector")
            self.db_connect_iam()
        elif self._check_connection_method() == "insufficient_params":
            LOGGER.error("Insufficient parameters provided to database connector")
        else:
            # no inputs provided
            LOGGER.warn("No inputs provided to DBConnector")

    def _check_connection_method(self):
        # ensure that if standard or iam method is used, all required params are provided
        insuff_params = lambda: (
            self.connection_name or self.user or self.db_name or self.password
        ) and (
            (not self.connection_name)
            or (not self.user)
            or (not self.db_name)
            or (not self.password)
        )
        if self.engine:
            return "engine"
        elif self.connection_string:
            return "connection_string"
        elif self.connection_name and self.user and self.db_name:
            if self.password:
                return "standard"
            else:
                return "iam"
        elif insuff_params() != True:
            return "insufficient_params"

    def db_exists(self, db_name):
        """
        Check whether a db connector instance for this db already exists

        Args:
            db_name (str): Database name

        Returns:
            (bool): Flag for is database connector already exists
        """
        return db_name == self.db_name

    def db_connect(
        self,
        connection_name: str = None,
        user: str = None,
        db_name: str = None,
        password: str = None,
        ip_type=IPTypes.PRIVATE,
    ) -> sqlalchemy.engine.Engine:
        connection_name = connection_name or self.connection_name
        user = user or self.user
        db_name = db_name or self.db_name
        password = password or self.password

        LOGGER.info(f"Connecting to database {db_name} as {user}")

        def getconn() -> pg8000.dbapi.Connection:
            conn: pg8000.dbapi.Connection = connector.connect(
                connection_name,
                "pg8000",
                user=user,
                password=password,
                db=db_name,
                ip_type=ip_type,
            )
            return conn

        engine = sqlalchemy.create_engine(
            "postgresql+pg8000://",
            creator=getconn,
        )
        engine.dialect.description_encoding = None
        return engine

    def db_connect_iam(
        self,
        connection_name: str = None,
        user: str = None,
        db_name: str = None,
        ip_type=IPTypes.PRIVATE,
    ) -> sqlalchemy.engine.Engine:
        connection_name = connection_name or self.connection_name
        user = user or self.user
        db_name = db_name or self.db_name

        LOGGER.info(f"Connecting to database {db_name} as {user}")

        def get_conn() -> pg8000.dbapi.Connection:
            conn: pg8000.dbapi.Connection = connector.connect(
                connection_name,
                "pg8000",
                user=user,
                db=db_name,
                ip_type=ip_type,
                enable_iam_auth=True,
            )
            return conn

        engine = sqlalchemy.create_engine(
            "postgresql+pg8000://",
            creator=get_conn,
        )
        engine.dialect.description_encoding = None
        self.engine = engine

    def read_schema_df(
        self, table_name: str, columns: list = ["*"], namespace: str = "public"
    ) -> pd.DataFrame:
        if namespace:
            query = f"SELECT table_name, column_name, is_nullable, data_type FROM information_schema.columns WHERE table_schema='{namespace}' and table_name='{table_name}'"
        else:
            query = f"SELECT table_name, column_name, is_nullable, data_type FROM information_schema.columns WHERE table_name='{table_name}'"
        pdf = pd.read_sql(sql=query, con=self.engine)
        if columns == ["*"]:
            pdf_final = pdf.sort_values("column_name")
        else:
            pdf_final = pdf.loc[pdf["column_name"].isin(columns)].sort_values(
                "column_name"
            )
        return pdf_final

    def read_table_query(self, query: str) -> pd.DataFrame:
        """
        Read table using provided query

        Args:
            query (str): Provided query

        Returns:
            pd.DataFrame: Pandas Dataframe
        """
        return pd.read_sql(sql=query, con=self.engine)

    def read_table(
        self,
        table_name: str,
        columns: list = ["*"],
        limit_clause: str = "",
        namespace: str = "public",
    ) -> pd.DataFrame:
        """
        Read table using predefined parameterized query

        Args:
            table_name (str): Name of table
            columns (list): Desired columns
            limit_clause (str): Desired row limit

        Returns:
            pd.DataFrame: [description]
        """

        # def convert_uuid()
        if namespace:
            table_name = namespace + "." + table_name

        LOGGER.info(f"Loading table {table_name} from Postgres...")
        if columns == ["*"]:
            # no need to quotify columns for *
            query = f"select {', '.join(columns)} from {table_name}" + limit_clause
        else:
            quotify = lambda columns: ['"' + col + '"' for col in columns]
            query = (
                f"select {', '.join(quotify(columns))} from {table_name}" + limit_clause
            )
        LOGGER.info(f"query: {query}")
        pdf = pd.read_sql(sql=query, con=self.engine).sort_index(axis=1)
        return pdf

    def write_table(self, dataframe, table_name, namespace: str = "public"):
        LOGGER.info("Write Datasets from Postgres...")
        if namespace:
            table_name = namespace + "." + table_name
        dataframe.to_sql(table_name, self.engine, index=False, if_exists="replace")
        return True

    def close_connection(self):
        LOGGER.info("Connection to Postgres disposed.")
        self.engine.dispose()
        return True
