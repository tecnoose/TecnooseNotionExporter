import unittest
from unittest.mock import patch
from tecnoose_notion_exporter.services.notion_service import NotionService

class TestNotionService(unittest.TestCase):

    def setUp(self):
        self.notion_service = NotionService()

    @patch('requests.post')
    def test_query_posts(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'results': []}
        result = self.notion_service.query_posts('database_id')
        self.assertIsNotNone(result)
        self.assertIn('results', result)

    @patch('requests.get')
    def test_get_page_blocks(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'results': []}
        result = self.notion_service.get_page_blocks('page_id')
        self.assertIsNotNone(result)
        self.assertIn('results', result)

    @patch('requests.patch')
    def test_update_page_tags(self, mock_patch):
        mock_patch.return_value.status_code = 200
        result = self.notion_service.update_page_tags('page_id')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()