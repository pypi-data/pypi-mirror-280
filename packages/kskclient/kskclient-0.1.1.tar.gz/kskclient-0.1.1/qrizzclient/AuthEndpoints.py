import logging
from .Exceptions import QrizzException
from .Config import BASE_URL,AUTH_TOKEN
logger = logging.getLogger(__name__)

class AuthEndpoints:
    """
    Class for handling authentication-related operations.

    This class provides methods for creating a new user, logging in, and retrieving user details.

    Attributes:
        client (QrizzClient): The instance of the QrizzClient class.
    """
    def __init__(self, client):
        """
        Initialize an instance of the AuthEndpoints class.

        Args:
            client (QrizzClient): The instance of the QrizzClient class.
        """
        self.client = client

    def create_user(self, name, email, password):
        """
        Create a new user with the provided credentials.

        Args:
            name (str): The name of the user.
            email (str): The email address of the user.
            password (str): The password for the user.

        Returns:
            bool: True if the user is created successfully, False otherwise.
        """
        headers = {
            "Content-Type": "application/json"
        }
        endpoint = self.client.endpoints.auth_endpoints['create_user']
        payload = {"name": name, "email": email, "password": password}
        response = self.client.send_request("POST", json=payload, headers=headers, endpoint=endpoint)
        status_code, data = self.client.handle_response(response)

        if status_code == 200:
            logger.info("Created User successfully")
            return data
        else:
            logger.error(f"Create User failed with status code: {status_code}")
            return False

    def login(self, email, password):
        """
        Authenticate the user with the provided email and password.

        Args:
            email (str): The email address of the user.
            password (str): The password of the user.

        Returns:
            bool: True if the authentication is successful, False otherwise.
        """
        headers = {
            "Content-Type": "application/json"
        }
        endpoint = self.client.endpoints.auth_endpoints['login']
        payload = {"email": email, "password": password}
        response = self.client.send_request("POST", json=payload, headers=headers, endpoint=endpoint)
        status_code, data = self.client.handle_response(response)

        if status_code == 200:
            logger.info("Authentication successful")
            return data
        else:
            logger.error(f"Authentication failed with status code: {status_code}")
            return False

    def get_user_details(self):
        """
        Get the details of the authenticated user.

        Returns:
            dict or None: The user details if the request is successful, None otherwise.

        Raises:
            QrizzException: If the request to get user details fails.
        """
        headers = {
            "auth-token": AUTH_TOKEN
        }
        endpoint = self.client.endpoints.auth_endpoints['get_user']
        response = self.client.send_request("GET", headers=headers, endpoint=endpoint)
        status_code, data = self.client.handle_response(response)

        if status_code == 200:
            logger.info("User details retrieved successfully.")
            return data
        else:
            logger.error(f"Failed to get user details. Status code: {status_code}")
            raise QrizzException(f"Failed to get user details. Status code: {status_code}")