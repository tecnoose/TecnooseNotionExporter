import os
from dotenv import load_dotenv
from tecnoose_notion_exporter.utils.import_logging import logger as logging

# Load environment variables from .env file
load_dotenv()

class Config:
    """
    Configuration class for Notion and Export settings.
    """
    class Notion:
        """
        Configuration settings for Notion API.
        """
        api_url: str = os.getenv('NOTION_API_URL')
        api_version: str = os.getenv('NOTION_API_VERSION')
        api_key: str = os.getenv('NOTION_API_KEY')
        notion_version: str = os.getenv('NOTION_VERSION')
        api_timeout: int = int(os.getenv('NOTION_API_TIMEOUT', 30))
        database_id: str = os.getenv('NOTION_DATABASE_ID')

        @staticmethod
        def get_url() -> str:
            """
            Get the Notion API URL.
            
            :return: str representing the Notion API URL
            """
            return Config.Notion.api_url

        @staticmethod
        def get_api_key() -> str:
            """
            Get the Notion API key.
            
            :return: str representing the Notion API key
            """
            return Config.Notion.api_key
        
        @staticmethod
        def get_api_version() -> str:
            """
            Get the Notion API version.
            
            :return: str representing the Notion API version
            """
            return Config.Notion.api_version

        @staticmethod
        def get_timeout() -> int:
            """
            Get the Notion API timeout.
            
            :return: int representing the Notion API timeout in seconds
            """
            return Config.Notion.api_timeout
        
        @staticmethod
        def get_database_id() -> str:
            """
            Get the Notion database ID.
            
            :return: str representing the Notion database ID
            """
            return Config.Notion.database_id
        
        @staticmethod
        def get_notion_version() -> str:
            """
            Get the Notion Version.
            
            :return: str representing the Notion Version
            """
            return Config.Notion.notion_version

    class Export:
        """
        Configuration settings for export paths.
        """
        export_path: str = os.getenv('EXPORT_PATH')

        @staticmethod
        def get_export_path() -> str:
            """
            Get the export path.
            
            :return: str representing the export path
            """
            return Config.Export.export_path
        
    def ToString():
        logging.info(f"Notion API URL: {Config.Notion.get_url()}")
        logging.info(f"Notion API Version: {Config.Notion.get_api_version()}")
        logging.info(f"Notion API Key: {Config.Notion.get_api_key()}")
        logging.info(f"Notion API Timeout: {Config.Notion.get_timeout()}")
        logging.info(f"Notion Database ID: {Config.Notion.get_database_id()}")
        logging.info(f"Notion Version: {Config.Notion.get_notion_version()}")
        logging.info(f"Export Path: {Config.Export.get_export_path()}")