import logging

logger = logging.getLogger(__name__)

class ConnectDbEndpoints:
    """
    Class for handling database connection-related operations.

    This class provides methods for connecting to a database, storing and retrieving database schemas,
    submitting credentials, and managing database connections.

    Attributes:
        client (QrizzClient): The instance of the QrizzClient class.
    """

    def __init__(self, client):
        """
        Initialize an instance of the ConnectDbEndpoints class.

        Args:
            client (QrizzClient): The instance of the QrizzClient class.
        """
        self.client = client

    def connect_db(self, username, password, host, database, dbtype, role, warehouse, port, schema):
        """
        Send a request to connect to a database with the provided credentials and configuration.

        Args:
            username (str): The username for the database connection.
            password (str): The password for the database connection.
            host (str): The host address for the database.
            database (str): The name of the database.
            dbtype (str): The type of the database.
            role (str): The role for the database connection.
            warehouse (str): The warehouse for the database connection.
            port (int): The port number for the database connection.
            schema (str): The schema for the database connection.

        Returns:
            tuple: A tuple containing the status code and the response data from the API.
        """
        payload = {
            "username": username,
            "password": password,
            "host": host,
            "database": database,
            "dbtype": dbtype,
            "role": role,
            "warehouse": warehouse,
            "port": port,
            "schema": schema
        }

        endpoint = self.client.endpoints.connectdb_endpoints['store_db']
        response = self.client.send_request("POST", json=payload, endpoint=endpoint)
        status_code, data = self.client.handle_response(response)
        if status_code == 200:
            logger.info("Connected to DB successfully.")
            return data
        else:
            logger.error(f"Failed to Connect DB . Status code: {status_code}")
            return None

    def storeschema(self, schema, dbId=None):
        """
        Store the database table schema on the server.

        Args:
            schema (dict): The database table schema to be stored.
            dbId (str, optional): The ID of the database.

        Returns:
            tuple: A tuple containing the status code and the response data from the API.
        """
        payload = {
            "schema": schema
        }
        endpoint = f"{self.client.endpoints.connectdb_endpoints['store_schema']}/{dbId}"
        response = self.client.send_request("POST", json=payload, endpoint=endpoint)
        status_code, data = self.client.handle_response(response)
        if status_code == 200:
            logger.info("Successfully Stored the Schema.")
            return data
        else:
            logger.error(f"Failed to Store Schema. Status code: {status_code}")
            return None

    def getschema(self, dbId):
        """
        Retrieve the database schema from the server.

        Args:
            dbId (str): The ID of the database.

        Returns:
            tuple: A tuple containing the status code and the response data from the API.
        """
        endpoint = f"{self.client.endpoints.connectdb_endpoints['get_schema']}/{dbId}"
        response = self.client.send_request("GET", endpoint=endpoint)
        status_code, data = self.client.handle_response(response)
        if status_code == 200:
            logger.info("Retrieved Schema successfully.")
            return data
        else:
            logger.error(f"Failed to retrieve schema. Status code: {status_code}")
            return None

    def get_db(self):
        """
        Retrieve the database details from the server.

        Returns:
            tuple: A tuple containing the status code and the response data from the API.
        """
        endpoint = self.client.endpoints.connectdb_endpoints['get_db']
        response = self.client.send_request("GET", endpoint=endpoint)
        status_code, data = self.client.handle_response(response)
        if status_code == 200:
            logger.info("Retrieved DB successfully.")
            return data
        else:
            logger.error(f"Failed to retrieve db . Status code: {status_code}")
            return None

    def delete_db(self, dbId):
        """
        Delete the database from the server.

        Args:
            dbId (str): The ID of the database.

        Returns:
            tuple: A tuple containing the status code and the response data from the API.
        """
        endpoint = f"{self.client.endpoints.connectdb_endpoints['delete_db']}/{dbId}"
        response = self.client.send_request("DELETE", endpoint=endpoint)
        status_code, data = self.client.handle_response(response)
        if status_code == 200:
            logger.info("DB Deleted successfully.")
            return data
        else:
            logger.error(f"Failed to delete db . Status code: {status_code}")
            return None