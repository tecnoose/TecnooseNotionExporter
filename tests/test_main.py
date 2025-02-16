import unittest
from unittest.mock import patch
from tecnoose_notion_exporter.main import main

class TestMain(unittest.TestCase):

    @patch('tecnoose_notion_exporter.main.NotionService')
    @patch('tecnoose_notion_exporter.main.MarkdownService')
    @patch('tecnoose_notion_exporter.main.FileService')
    def test_main(self, MockFileService, MockMarkdownService, MockNotionService):
        mock_notion_service = MockNotionService.return_value
        mock_markdown_service = MockMarkdownService.return_value
        mock_file_service = MockFileService.return_value

        mock_notion_service.query_posts.return_value = {'results': [{'id': 'page_id', 'properties': {'Name': {'title': [{'text': {'content': 'Test Title'}}]}}}]}
        mock_notion_service.get_page_blocks.return_value = {'results': [{'type': 'paragraph', 'paragraph': {'rich_text': [{'plain_text': 'Paragraph text'}]}}]}
        mock_markdown_service.convert_to_markdown.return_value = 'Markdown content'
        
        main()

        mock_notion_service.query_posts.assert_called_once()
        mock_notion_service.get_page_blocks.assert_called_once_with('page_id')
        mock_markdown_service.convert_to_markdown.assert_called_once()
        mock_file_service.create_post.assert_called_once_with('Test-Title', 'Markdown content')
        mock_notion_service.update_page_tags.assert_called_once_with('page_id')

if __name__ == '__main__':
    unittest.main()