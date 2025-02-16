import unittest
from tecnoose_notion_exporter.services.markdown_service import MarkdownService

class TestMarkdownService(unittest.TestCase):

    def setUp(self):
        self.markdown_service = MarkdownService()

    def test_convert_text_block(self):
        text_block = {'text': 'Sample text'}
        result = self.markdown_service.convert_text_block(text_block)
        self.assertEqual(result, 'Sample text')

    def test_convert_heading_block(self):
        heading_block = {'heading_1': {'rich_text': [{'plain_text': 'Heading 1'}]}}
        result = self.markdown_service.convert_heading_block(heading_block, 1)
        self.assertEqual(result, '# Heading 1')

    def test_convert_bulleted_list_block(self):
        bulleted_list_block = {'text': 'List item'}
        result = self.markdown_service.convert_bulleted_list_block(bulleted_list_block)
        self.assertEqual(result, '- List item')

    def test_convert_numbered_list_block(self):
        numbered_list_block = {'text': 'List item'}
        result = self.markdown_service.convert_numbered_list_block(numbered_list_block)
        self.assertEqual(result, '1. List item')

    def test_convert_paragraph_block(self):
        paragraph_block = {'paragraph': {'rich_text': [{'plain_text': 'Paragraph text'}]}}
        result = self.markdown_service.convert_paragraph_block(paragraph_block)
        self.assertEqual(result, 'Paragraph text')

    def test_convert_image_block(self):
        image_block = {'image': {'file': {'url': 'https://via.placeholder.com/150'}}}
        folder_name = 'test_folder'
        result = self.markdown_service.convert_image_block(image_block, folder_name)
        self.assertTrue(result.startswith('![Image](images/'))

if __name__ == '__main__':
    unittest.main()