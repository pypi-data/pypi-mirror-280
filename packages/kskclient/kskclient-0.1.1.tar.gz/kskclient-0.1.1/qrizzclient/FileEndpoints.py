import os
import logging
from requests_toolbelt.multipart.encoder import MultipartEncoder
from .Config import BASE_URL,AUTH_TOKEN
logger = logging.getLogger(__name__)

class FileEndpoints:
    """
    Class for handling file management-related operations.

    This class provides methods for uploading files, retrieving files, deleting files,
    and updating file metadata.

    Attributes:
        client (QrizzClient): The instance of the QrizzClient class.
    """
    def __init__(self, client):
        """
        Initialize an instance of the FileEndpoints class.

        Args:
            client (QrizzClient): The instance of the QrizzClient class.
        """
        self.client = client

    def upload_file(self, file_path, title):
        """
        Upload a file to the server.

        Args:
            file_path (str): The path to the file to be uploaded.
            title (str): The title of the file.

        Returns:
            tuple: A tuple containing the status code and the response data from the API.
        """
        endpoint = self.client.endpoints.file_endpoints['upload_file']
        with open(file_path, 'rb') as file:
            m = MultipartEncoder(
                fields={
                    'file': (title, file, "text/csv"),
                    'title': title
                }
            )
            headers = {
                "Content-Type": m.content_type,
                "auth-token": AUTH_TOKEN
            }
            response = self.client.send_request("POST", data=m, headers=headers, endpoint=endpoint)
            status_code, data = self.client.handle_response(response)
            if status_code == 200:
                logger.info("File Uploaded successfully.")
                return data
            else:
                logger.error(f"Failed to Upload file. Status code: {status_code}")
                return None

    def storeschema_File(self, schema, file_id):
        """
        Store the Schema in MongoDB.

        Args:
            schema (dict): The schema to be stored.
            file_id (str): The ID of the file.

        Returns:
            tuple: A tuple containing the status code and the response data from the API.
               The response data is a dict containing the list of files if the request is successful, None otherwise.
        """
        endpoint = f"{self.client.endpoints.file_endpoints['store_schema']}/{file_id}"
        headers = {
            "Content-Type": "application/json",
            "auth-token": AUTH_TOKEN
        }
        payload = {
            "schema": schema
        }
        response = self.client.send_request("POST", json=payload, headers=headers, endpoint=endpoint)
        status_code, data = self.client.handle_response(response)
        if status_code == 200:
            logger.info("Schema Stored successfully.")
            return data
        else:
            logger.error(f"Failed to store schema. Status code: {status_code}")
            return None

    def getschema_File(self, file_id):
        """
        Retrieve the schema for the specified file.

        Args:
            file_id (str): The ID of the file.

        Returns:
            tuple: A tuple containing the status code and the response data from the API.
               The response data is a dict containing the schema if the request is successful, None otherwise.
        """
        headers = {
            "auth-token": AUTH_TOKEN
        }
        endpoint = f"{self.client.endpoints.file_endpoints['get_schema']}/{file_id}"
        response = self.client.send_request("GET", headers=headers, endpoint=endpoint)
        status_code, data = self.client.handle_response(response)
        if status_code == 200:
            logger.info("Retrieved Schema successfully.")
            return data
        else:
            logger.error(f"Failed to Retrieve schema. Status code: {status_code}")
            return None

    def get_files(self):
        """
        Retrieve a list of files from the server.

        Returns:
            tuple: A tuple containing the status code and the response data from the API.
               The response data is a dict containing the list of files if the request is successful, None otherwise.
        """
        headers = {
            "auth-token":AUTH_TOKEN
        }
        endpoint = self.client.endpoints.file_endpoints['get_files']
        response = self.client.send_request("GET", headers=headers, endpoint=endpoint)
        status_code, data = self.client.handle_response(response)
        if status_code == 200:
            logger.info("Files Retrieved successfully.")
            return data
        else:
            logger.error(f"Failed to Retrieve the files. Status code: {status_code}")
            return None


    def delete_file(self, file_id):
        """
        Delete a file from the server.

        Args:
            file_id (str): The ID of the file to be deleted.

        Returns:
            dict or None: The response data after deleting the file if the request is successful, None otherwise.
        """
        headers = {
            "auth-token": AUTH_TOKEN
        }
        endpoint = f"{self.client.endpoints.file_endpoints['delete_file']}/{file_id}"
        response = self.client.send_request("DELETE", headers=headers, endpoint=endpoint)
        status_code, data = self.client.handle_response(response)

        if status_code == 200:
            logger.info("File Deleted successfully.")
            return data
        else:
            logger.error(f"Failed to delete file. Status code: {status_code}")
            return None

    def update_file(self, title, file_id):
        """
        Update a file on the server.

        Args:
            title (str): The new title for the file.
            file_id (str): The ID of the file to be updated.

        Returns:
            dict or None: The response data after updating the file if the request is successful, None otherwise.
        """
        headers = {
            "Content-Type": "application/json",
            "auth-token": AUTH_TOKEN
        }
        endpoint = f"{self.client.endpoints.file_endpoints['update_file']}/{file_id}"
        payload = {
            "title": title
        }
        response = self.client.send_request("PUT", json=payload, headers=headers, endpoint=endpoint)
        status_code, data = self.client.handle_response(response)

        if status_code == 200:
            logger.info("File Updated successfully.")
            return data
        else:
            logger.error(f"Failed to update file. Status code: {status_code}")
            return None