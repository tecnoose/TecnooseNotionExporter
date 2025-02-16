import os
import logging
import requests
from urllib.parse import urlparse
from tecnoose_notion_exporter.config.global_configuration import Config

class FileService:
    """
    Service class for handling file operations related to exporting Notion content.
    """
    base_path: str
    image_index: int = 0

    def __init__(self):
        self.base_path = Config.Export.export_path

    def create_post_root_folder(self, folder_name: str) -> str:
        """
        Create the root folder for a post.

        :param folder_name: str representing the folder name
        :return: str representing the path of the created folder
        """
        folder_path = os.path.join(self.base_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        return folder_path

    def create_post_images_folder(self, folder_name: str) -> str:
        """
        Create the images folder for a post.

        :param folder_name: str representing the folder name
        :return: str representing the path of the created folder
        """
        folder_path = os.path.join(self.base_path, folder_name, 'images')
        os.makedirs(folder_path, exist_ok=True)
        return folder_path
    
    def delete_folder(self, folder_name: str) -> None:
        """
        Delete a folder and its contents.

        :param folder_name: str representing the folder name
        """
        folder_path = os.path.join(self.base_path, folder_name)
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            for root, dirs, files in os.walk(folder_path, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(folder_path)
        
    def create_post(self, folder_name: str, content: str = "") -> str:
        """
        Create a markdown file for a post.

        :param folder_name: str representing the folder name
        :param content: str representing the content to write to the file
        :return: str representing the path of the created file
        """
        file_path = os.path.join(self.base_path, folder_name, 'index.md')
        with open(file_path, 'w') as file:
            file.write(content)
        return file_path
    
    def download_image(self, image_url: str, folder_name: str) -> str:
        """
        Download an image from a URL and save it to the images folder.

        :param image_url: str representing the URL of the image
        :param folder_name: str representing the folder name to save the image
        :return: str representing the filename of the downloaded image
        """
        response = requests.get(image_url)
        if response.status_code == 200:
            parsed_url = urlparse(image_url)
            original_filename = os.path.basename(parsed_url.path)
            self.image_index += 1
            new_filename = f"{self.image_index}_{original_filename}"

            full_path = os.path.join(self.base_path, folder_name, 'images', new_filename)
            with open(full_path, 'wb') as file:
                file.write(response.content)
            return new_filename
        else:
            logging.error(f"Failed to download image from {image_url}")
            raise Exception(f"Failed to download image from {image_url}")