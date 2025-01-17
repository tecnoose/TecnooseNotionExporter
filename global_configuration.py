
class Config:    
    class Notion:
        api_url: str = "https://api.notion.com"
        api_version: str = "v1"
        api_key: str = "API_KEY"
        api_timeout: int = 30  # seconds
        database_id: str = "78a60b28a70f4411968f548597d8fc1e"

        @staticmethod
        def get_url():
            return Config.Notion.api_url

        @staticmethod
        def get_api_key():
            return Config.Notion.api_key

        @staticmethod
        def get_timeout():
            return Config.Notion.api_timeout
        
        @staticmethod
        def get_database_id():
            return Config.Notion.database_id

    class Export:
        export_path: str = "/Users/paolo/Blogs/Tecnoose/content/posts"

        @staticmethod
        def get_export_path():
            return Config.Export.export_path