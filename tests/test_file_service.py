import unittest
from tecnoose_notion_exporter.services.file_service import FileService

class TestFileService(unittest.TestCase):

    def setUp(self):
        self.file_service = FileService()

    def test_create_post_root_folder(self):
        folder_name = "test_folder"
        folder_path = self.file_service.create_post_root_folder(folder_name)
        self.assertTrue(os.path.exists(folder_path))

    def test_create_post_images_folder(self):
        folder_name = "test_folder"
        folder_path = self.file_service.create_post_images_folder(folder_name)
        self.assertTrue(os.path.exists(folder_path))

    def test_delete_folder(self):
        folder_name = "test_folder"
        self.file_service.create_post_root_folder(folder_name)
        self.file_service.delete_folder(folder_name)
        self.assertFalse(os.path.exists(os.path.join(self.file_service.base_path, folder_name)))

    def test_create_post(self):
        folder_name = "test_folder"
        self.file_service.create_post_root_folder(folder_name)
        content = "Test content"
        file_path = self.file_service.create_post(folder_name, content)
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, 'r') as file:
            self.assertEqual(file.read(), content)

    def test_download_image(self):
        folder_name = "test_folder"
        self.file_service.create_post_images_folder(folder_name)
        image_url = "https://via.placeholder.com/150"
        file_name = self.file_service.download_image(image_url, folder_name)
        self.assertTrue(os.path.exists(os.path.join(self.file_service.base_path, folder_name, 'images', file_name)))

if __name__ == '__main__':
    unittest.main()