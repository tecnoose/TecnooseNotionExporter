from global_configuration import Config
import os
import requests
from urllib.parse import urlparse

class FileService:
    basePath: str 
    imageIndex: int = 0

    def __init__(self):
        self.basePath = Config.Export.export_path

    def create_post_root_folder(self, folder_name: str) -> str:
        folder_path = os.path.join(self.basePath, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        return folder_path

    def create_post_images_folder(self, folder_name: str) -> str:
        folder_path = os.path.join(self.basePath, folder_name,'images')
        os.makedirs(folder_path, exist_ok=True)
        return folder_path
    
    def delete_folder(self, folder_name: str) -> str:
        folder_path = os.path.join(self.basePath, folder_name)
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            for root, dirs, files in os.walk(folder_path, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(folder_path)
        
    def create_post(self, folder_name : str, content: str="") -> str:
        file_path = os.path.join(self.basePath,folder_name, 'index.md')
        with open(file_path, 'w') as file:
            file.write(content)
        return file_path
    
    def download_image(self, image_url: str, folder_name: str) -> str:
        response = requests.get(image_url)
        if response.status_code == 200:
            parsed_url = urlparse(image_url)

            # Extract the filename from the path
            original_filename = os.path.basename(parsed_url.path)
            self.imageIndex += 1
            original_filename = f"{self.imageIndex}_{original_filename}"

            full_path = os.path.join(self.basePath, folder_name, 'images', original_filename)
            with open(full_path, 'wb') as file:
                file.write(response.content)
            return original_filename
        else:
            raise Exception(f"Failed to download image from {image_url}")

