"""
### CODE OWNERS: Rick Moton
### OBJECTIVE:
    Handle secret management
### DEVELOPER NOTES:
"""

import logging
import json
import os

from google.cloud import secretmanager

logging.basicConfig(
    format="%(asctime)s - %(message)s", level=os.environ.get("LOGLEVEL", "INFO")
)
LOGGER = logging.getLogger(__name__)

# ===========================================================

class SecretManger:
    def __init__(self, project_id: str = None, secret_id: str = None, version_id: str = "latest"):
        self.project_id = project_id
        self.secret_id = secret_id
        self.version_id = str(version_id)
        self.client = secretmanager.SecretManagerServiceClient()

    def create_secret(self, project_id: str, secret_id: str, secret: str):
        """
        Create a secret to push to secret manger

        Args:
            project_id:
            secret_id:
        """
        parent = f"projects/{project_id}"
        secret = self.client.create_secret(
            request={
                "parent": parent,
                "secret_id": secret_id,
                "secret": {"replication": {"automatic": {}}},
            }
        )

        # add the new secret version
        try:
            self.client.add_secret_version(
                request={
                    "parent": secret.name, 
                    "payload": {
                        "data": b"".format(secret)
                    }
                }
            )
        except:
            pass

    def read_secret(self, version_id: str=None):
        """
        Read secret from secret manager

        Args:
            project_id (str)
            secret_id (str)
            version_id (str, optional): Defaults to "latest".

        Returns:
            _type_: _description_
        """
        version_id = version_id or self.version_id
        name = self.client.secret_version_path(self.project_id, self.secret_id, str(version_id))
        response = self.client.access_secret_version(name=name)
        payload = response.payload.data.decode("UTF-8")
        return payload
    
    def delete_secret(self, version_id: str=None):
        """
        Delete secret from secret manager

        Args:
            project_id (str)
            secret_id (str)
            version_id (str, optional): Defaults to "latest".

        Returns:
            _type_: _description_
        """
        version_id = version_id or self.version_id
        name = self.client.secret_version_path(self.project_id, self.secret_id, str(version_id))
        response = self.client.destroy_secret(name=name)
        return response
    
    def get_database_params(self, version_id: str=None):
        """
        Get database params from secret manager

        Args:
            db_name (str): Database name
            version_id (str, optional): Secret version ID. Defaults to "latest".

        Returns:
            db_params: nested dictionary of database params (e.g. {"database": {"connection_name", connection_name, "db_name": db_name}})
        """
        version_id = version_id or self.version_id
        secret_payload = self.read_secret(version_id=str(version_id))
        secret_dict = json.loads(secret_payload)
        db_params = secret_dict["db_params"]
        return db_params
