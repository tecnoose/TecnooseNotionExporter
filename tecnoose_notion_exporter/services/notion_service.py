import logging
import requests
from tecnoose_notion_exporter.config.global_configuration import Config

class NotionService:
    """The current class aims to export posts from Notion when available."""
    
    def __init__(self):
        self.api_key = Config.Notion.api_key
        self.api_url = Config.Notion.api_url
        self.api_version = Config.Notion.api_version
        self.api_timeout = Config.Notion.api_timeout
        self.request_header = {
            "Authorization": f"Bearer {self.api_key}",
            "Notion-Version": self.api_version,
            "Content-Type": "application/json",
        }

    def print_parameters(self):
        """Prints the current configuration parameters."""
        logging.info(f"apiUrl={self.api_url}")
        logging.info(f"apiKey={self.api_key}")
        logging.info(f"apiVersion={self.api_version}")
        logging.info(f"apiTimeout={self.api_timeout}")
        logging.info(f"header authorization={self.request_header}")

    def query_posts(self, database_id: str) -> dict:
        """
        Queries posts from a Notion database.
        
        Args:
            database_id (str): The ID of the Notion database.
        
        Returns:
            dict: The response from the Notion API.
        """
        if not database_id:
            logging.error("Missing database ID. Provide a valid ID and try again.")
            return None

        url = f"{self.api_url}/{self.api_version}/databases/{database_id}/query"
        payload = {
            "filter": {
                "property": "Tags",
                "multi_select": {
                    "contains": "Post"
                }
            }
        }

        response = requests.post(url, headers=self.request_header, json=payload)

        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Failed to retrieve database: {response.status_code}")
            return None

    def get_page_blocks(self, page_id: str) -> dict:
        """
        Retrieves the blocks of a Notion page.
        
        Args:
            page_id (str): The ID of the Notion page.
        
        Returns:
            dict: The response from the Notion API.
        """
        if not page_id:
            logging.error("Missing page ID. Provide a valid ID and try again.")
            return None

        url = f"{self.api_url}/{self.api_version}/blocks/{page_id}/children"
        response = requests.get(url, headers=self.request_header)

        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Failed to retrieve page block children: {response.status_code}")
            return None

    def update_page_tags(self, page_id: str) -> bool:
        """
        Updates the tags of a Notion page.
        
        Args:
            page_id (str): The ID of the Notion page.
        
        Returns:
            bool: True if the update was successful, False otherwise.
        """
        if not page_id:
            logging.error("Missing page ID. Provide a valid ID and try again.")
            return False

        url = f"{self.api_url}/{self.api_version}/pages/{page_id}"
        payload = {
            "properties": {
                "Tags": {
                    "multi_select": [
                        {"name": "Posted"}
                    ]
                }
            }
        }

        response = requests.patch(url, headers=self.request_header, json=payload)

        if response.status_code == 200:
            return True
        else:
            logging.error(f"Failed to update page tags: {response.status_code}")
            return False