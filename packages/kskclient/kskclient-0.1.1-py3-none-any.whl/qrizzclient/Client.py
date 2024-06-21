import requests
import logging
from .AuthEndpoints import AuthEndpoints
from .ChatEndpoints import ChatEndpoints
from .ConnectDbEndpoints import ConnectDbEndpoints
from .FileEndpoints import FileEndpoints
from .Endpoints import Endpoints
from .Session import Session
from .Exceptions import QrizzException
from .Config import BASE_URL,AUTH_TOKEN

logger = logging.getLogger(__name__)

class QrizzClient:
    """
    Client class for interacting with the Qrizz API.

    This class serves as the main entry point for the Qrizz API client. It provides methods
    to set authentication credentials, send requests to the API, and handle responses. It also
    encapsulates the various API endpoints through separate classes for authentication, chat,
    database connection, and file management.

    Attributes:
        credentials (dict): The authentication credentials for the API.
        session (Session): The current session object for managing conversation IDs.
        endpoints (Endpoints): The collection of API endpoints.
        auth_endpoints (AuthEndpoints): The authentication-related API endpoints.
        chat_endpoints (ChatEndpoints): The chat-related API endpoints.
        connectdb_endpoints (ConnectDbEndpoints): The database connection-related API endpoints.
        file_endpoints (FileEndpoints): The file management-related API endpoints.
    """
    def __init__(self):
        self.credentials = None
        self.session = Session()
        self.endpoints = Endpoints()
        self.auth_endpoints = AuthEndpoints(self)
        self.chat_endpoints = ChatEndpoints(self)
        self.connectdb_endpoints = ConnectDbEndpoints(self)
        self.file_endpoints = FileEndpoints(self)

    def set_credentials(self, email, key):
        """
        Set the authentication credentials for the client.

        Args:
            email (str): The email address associated with the account.
            key (str): The authentication key or password.
        """
        self.credentials = {"email": email, "key": key}

    def get_credentials(self):
        """
        Retrieve the currently set authentication credentials.

        Returns:
            dict: A dictionary containing the email and key for authentication.
        """
        return self.credentials

    def send_request(self, method, json=None, data=None, endpoint=None, headers=None):
        """
        Send an HTTP request to the API endpoint with the provided credentials and method.

        Args:
            method (str): The HTTP method (e.g., 'GET', 'POST', 'PUT', 'DELETE').
            json (dict, optional): The JSON payload for the request.
            data (object, optional): The data payload for the request.
            endpoint (str): The API endpoint.
            headers (dict, optional): Additional headers for the request.

        Returns:
            requests.Response or None: The response object or None if an exception occurred.
        """
        url = f"{BASE_URL}/{endpoint}"
        default_headers = {
            "Content-Type": "application/json",
            "auth-token": AUTH_TOKEN
        }
        if headers:
            default_headers.update(headers)

        try:
            response = requests.request(method, url, headers=default_headers, json=json, data=data)
            print(response.text)
            response.raise_for_status()  # Raise an exception for non-2xx status codes
        except requests.exceptions.RequestException as e:
            logger.error(f"Error: {e}")
            return None

        logger.info(f"Response status code: {response.status_code}")
        return response

    def handle_response(self, response):
        """
        Handle the response from the API.

        Args:
            response (requests.Response): The response object from the API request.

        Returns:
            tuple: A tuple containing the status code and the response data.

        Raises:
            QrizzException: If the request failed or the response status code is not successful.
        """
        if response is None:
            raise QrizzException("Request failed")

        if response.status_code >= 400:
            try:
                data = response.json()
            except ValueError:
                data = response.text
            raise QrizzException(
                f"Request failed with status code {response.status_code}: {data}"
            )

        logger.info(f"Response text: {response.text}")  # Print the response text

        # Check if the response is JSON
        try:
            data = response.json()
        except ValueError:
            data = response.text

        return response.status_code, data