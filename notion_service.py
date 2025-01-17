from global_configuration import Config
import requests

class NotionService:
    """The current class aim to export post from notion when available"""
    apiKey: str
    apiUrl: str 
    apiVersion: str
    apiTimeout: int

    request_header = {
        "Authorization": f"Bearer {Config.Notion.api_key}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }

    def __init__(self):
        self.apiKey = Config.Notion.api_key
        self.apiUrl = Config.Notion.api_url
        self.apiVersion = Config.Notion.api_version
        self.apiTimeout = Config.Notion.api_timeout

    def printParameters(self):
        print(f"apiUrl={self.apiUrl}")
        print(f"apiKey={self.apiKey}")
        print(f"apiVersion={self.apiVersion}")
        print(f"apiTimeout={str(self.apiTimeout)}")
        print(f"header authorization={self.request_header}")

    def queryPosts(self, database_id: str) -> dict:
        
        #1. Check the input
        if database_id == "":
            print(f"Missing database Id. Provide a valid id and try again.") 
            return None

        #2. Define the notion endpoint route
        url = f"{self.apiUrl}/{self.apiVersion}/databases/{database_id}/query"

        #3. Create the payload
        payload = {
            "filter": {
                "property": "Tags",
                "multi_select": {
                    "contains": "Post"
                }
            }
        }

        #4. Execute the request
        response = requests.post(url, headers=self.request_header, json=payload)

        #5. Check the response and return
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve database: {response.status_code}")
            return None

    def exportPage(self, page_id: str) -> str:
        pass

    def getPageBlocks(self, page_id: str) -> str:
        pass
        
        #1. Check the input
        if page_id == "":
            print(f"Missing page Id. Provide a valid id and try again.")
            return None

        #2. Define the notion endpoint route
        url = f"{self.apiUrl}/{self.apiVersion}/blocks/{page_id}/children"

        #3. Execute the request
        response = requests.get(url, headers=self.request_header)

        #4. Check the response and return
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve page block children: {response.status_code}")
            return None
