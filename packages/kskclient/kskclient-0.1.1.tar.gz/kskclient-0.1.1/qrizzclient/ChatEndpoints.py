import os
import time
from io import BytesIO
from PIL import Image
import requests
import logging
from qrizzclient.Session import Session
from .Config import BASE_URL,AUTH_TOKEN
logger = logging.getLogger(__name__)

class ChatEndpoints:
    """
    Class for handling chat-related operations.

    This class provides methods for performing searches, managing conversations, and retrieving
    conversation information.

    Attributes:
        client (QrizzClient): The instance of the QrizzClient class.
    """
    def __init__(self, client):
        """
        Initialize an instance of the ChatEndpoints class.

        Args:
            client (QrizzClient): The instance of the QrizzClient class.
        """
        self.client = client

    def search(self, msg, conv_id=None, current_flow_flag=None):
        """
        Perform a search using the provided inputs.

        Args:
            msg (str): The search query or message.
            conv_id (str, optional): The conversation ID to use for the search.
            current_flow_flag (bool, optional): Flag indicating the current flow state.

        Returns:
            tuple: A tuple containing the status code and the response data from the API.
        """
        if conv_id is None:
            conv_id = self.client.session.get_conv_id()
            if conv_id is None:
                # Create a new session only if there is no existing conv_id
                self.client.session = Session()
                print("Created a new session")
            else:
                print(f"Using existing conv_id: {conv_id}")
        else:
            print(f"Using provided conv_id: {conv_id}")
            self.client.session.set_conv_id(conv_id)

        payload = {
            "msg": str(msg),
            "currentFlowFlag": current_flow_flag,
            "convId": conv_id,
        }
        endpoint = self.client.endpoints.chat_endpoints['search']
        response = self.client.send_request("POST", json=payload, endpoint=endpoint)
        data = self.client.handle_response(response)
        
        # Update the conv_id from the response
        if 'convId' in data[1]:
            new_conv_id = data[1]['convId']
            print(f"Updating conv_id from root level: {new_conv_id}")
            self.client.session.set_conv_id(new_conv_id)
        elif 'response' in data[1] and 'convId' in data[1]['response']:
            new_conv_id = data[1]['response']['convId']
            print(f"Updating conv_id from 'response' dictionary: {new_conv_id}")
            self.client.session.set_conv_id(new_conv_id)
        else:
            print("convId not found in the response")

        # Check if the response contains image data
        if 'response' in data[1] and 'image' in data[1]['response']:
            image_data = data[1]['response']['image']
            self.save_image_locally(image_data)

        return data

    def save_image_locally(self, image_data):
        """
        Save the image data to a local file.

        Args:
            image_data (bytes): The image data as bytes.
        """
        # Create a directory to store the images if it doesn't exist
        images_dir = 'images'
        os.makedirs(images_dir, exist_ok=True)

        # Generate a unique filename for the image
        filename = f"image_{int(time.time())}.png"
        file_path = os.path.join(images_dir, filename)

        # Save the image data to the local file
        try:
            image = Image.open(BytesIO(image_data))
            image.save(file_path)
            print(f"Image saved to {file_path}")
        except Exception as e:
            print(f"Error saving image: {e}")

    def end_session(self):
        """
        End the current session and reset the conversation ID.
        """
        self.client.session.close()
        print("Session is end")

    

    def userconvid(self):
        """
        Retrieve the conversation IDs associated with the authenticated user.

        Returns:
            tuple: A tuple containing the status code and the response data from the API.
        """
        headers = {
            "auth-token": AUTH_TOKEN
        }
        endpoint = self.client.endpoints.chat_endpoints['get_user_conv']
        response = self.client.send_request("GET", headers=headers, endpoint=endpoint)
        status_code, data = self.client.handle_response(response)
        if status_code == 200:
            logger.info("UserConverstionId retrieved Successfully")
            return data
        else:
            logger.error(f"Failed to retrieve UserConverstionId with status code: {status_code}")
            return False

    def getconv(self, conv_id):
        """
        Get the details of the specified conversation.

        Returns:
            dict or None: The conversation details if the request is successful, None otherwise.
        """
        headers = {
            "auth-token": AUTH_TOKEN
        }
        endpoint = f"{self.client.endpoints.chat_endpoints['get_conv']}/{conv_id}"
        response = self.client.send_request("GET", headers=headers, endpoint=endpoint)
        status_code, data = self.client.handle_response(response)

        if status_code == 200:
            logger.info("convId retrieved successfully.")
            return data
        else:
            logger.error(f"Failed to get convid. Status code: {status_code}")
            return None

    def get_title(self, conv_id):
        """
        Get the title for the specified conversation ID.

        Args:
            conv_id (str): The conversation ID.

        Returns:
            tuple: A tuple containing the status code and the response data from the API.
               The response data is a dict containing the title if the request is successful, None otherwise.

        """
        endpoint = f"{self.client.endpoints.chat_endpoints['get_title']}/{conv_id}"
        response = self.client.send_request("GET", endpoint=endpoint)
        status_code, data = self.client.handle_response(response)

        if status_code == 200:
            logger.info("Get title successfully.")
            return data
        else:
            logger.error(f"Failed to get title. Status code: {status_code}")
            return None
        
    def set_title(self, convId):
        """
        Set the title for the specified conversation ID.

        Args:
            conv_id (str): The conversation ID.

        Returns:
            dict: The response data from the API.
        """
        headers = {
            "Content-Type": "application/json"
        }
        endpoint = f"{self.client.endpoints.chat_endpoints['set_title']}"
        payload = {"convId": convId}
        response = self.client.send_request("POST", json=payload, headers=headers, endpoint=endpoint)
        status_code, data = self.client.handle_response(response)

        if status_code == 200:
            logger.info("Title set successfully.")
            return data
        else:
            logger.error(f"Failed to set title. Status code: {status_code}")
            return None
        
        
    def clear_user_conv(self):
        """
        Clear the conversation for the authenticated user.

        Returns:
            dict or None: The response data after clearing the conversation if the request is successful, None otherwise.
        """
        headers = {
            "auth-token": AUTH_TOKEN
        }
        endpoint = f"{self.client.endpoints.chat_endpoints['clear_conv']}"
        response = self.client.send_request("DELETE", headers=headers, endpoint=endpoint)
        status_code, data = self.client.handle_response(response)
        if status_code == 200:
            logger.info("Deleted  successfully.")
            return data
        else:
            logger.error(f"Failed to Delete. Status code: {status_code}")
            return None