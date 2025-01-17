from file_service import FileService

class MarkdownService:
    fileService: FileService 
    def __init__(self):
        self.fileService = FileService()

    def convert_text_block(self, text_block: dict) -> str:
        """
        Convert a Notion text block to standard Markdown.
        
        :param text_block: dict representing a Notion text block
        :return: str containing the converted Markdown text
        """
        text = text_block.get('text', '')
        return text

    def convert_heading_block(self, heading_block: dict, level: int) -> str:
        """
        Convert a Notion heading block to standard Markdown.
        
        :param heading_block: dict representing a Notion heading block
        :param level: int representing a level of the heading block
        :return: str containing the converted Markdown heading
        """
        heading = f'heading_{level}'
        rich_text = heading_block.get(heading, {}).get('rich_text', [])
        text_content = ''.join([text.get('plain_text', '') for text in rich_text])
        return f"{'#' * level} {text_content}"
        
    def convert_bulleted_list_block(self, bulleted_list_block: dict ) -> str:
        """
        Convert a Notion bulleted list block to standard Markdown.
        
        :param bulleted_list_block: dict representing a Notion bulleted list block
        :return: str containing the converted Markdown bulleted list
        """
        text = bulleted_list_block.get('text', '')
        return f"- {text}"

    def convert_numbered_list_block(self, numbered_list_block: dict ) -> str:
        """
        Convert a Notion numbered list block to standard Markdown.
        
        :param numbered_list_block: dict representing a Notion numbered list block
        :return: str containing the converted Markdown numbered list
        """
        text = numbered_list_block.get('text', '')
        return f"1. {text}"

    def convert_paragraph_block(self, paragraph_block: dict) -> str:
        """
        Convert a Notion paragraph block to standard Markdown.
        
        :param paragraph_block: dict representing a Notion paragraph block
        :return: str containing the converted Markdown paragraph
        """
        rich_text = paragraph_block.get('paragraph', {}).get('rich_text', [])
        text_content = ''
        for text in rich_text:
            plain_text = text.get('plain_text', '')
            annotations = text.get('annotations', {})
            href = text.get('href', None)
            
            if annotations.get('bold'):
                plain_text = f"**{plain_text}**"
            if annotations.get('italic'):
                plain_text = f"*{plain_text}*"
            if annotations.get('strikethrough'):
                plain_text = f"~~{plain_text}~~"
            if annotations.get('underline'):
                plain_text = f"<u>{plain_text}</u>"
            if annotations.get('code'):
                plain_text = f"`{plain_text}`"
            
            if href:
                plain_text = f"[{plain_text}]({href})"
            
            text_content += plain_text
        
        return text_content

    def convert_image_block(self, image_block: dict, folder_name: str) -> str:
        """
        Convert a Notion image block to standard Markdown.
        
        :param image_block: dict representing a Notion image block
        :return: str containing the converted Markdown image
        """
        image_url = image_block.get('image', {}).get('file', {}).get('url', '')
        
        fileName = self.fileService.download_image(image_url, folder_name)
        return f"![Image](images/{fileName})"
    
    def convert_bulleted_list_item_block(self, bulleted_list_item_block: dict) -> str:
        """
        Convert a Notion bulleted list item block to standard Markdown.
        
        :param bulleted_list_item_block: dict representing a Notion bulleted list item block
        :return: str containing the converted Markdown bulleted list item
        """
        rich_text = bulleted_list_item_block.get('bulleted_list_item', {}).get('rich_text', [])
        text_content = ''.join([text.get('plain_text', '') for text in rich_text])
        return f"- {text_content}"
    
    def convert_code_block(self, code_block: dict) -> str:
        """
        Convert a Notion code block to standard Markdown.
        
        :param code_block: dict representing a Notion code block
        :return: str containing the converted Markdown code block
        """
        rich_text = code_block.get('code', {}).get('rich_text', [])
        language = code_block.get('code', {}).get('language', '')
        code_content = ''.join([text.get('plain_text', '') for text in rich_text])
        return f"```{language}\n{code_content}\n```"

    def convert_callout_block(self, callout_block: dict) -> str: 
        """
        Convert a Notion callout block to standard Markdown.
        
        :param callout_block: dict representing a Notion callout block
        :return: str containing the converted Markdown callout
        """
        rich_text = callout_block.get('callout', {}).get('rich_text', [])
        text_content = ''.join([text.get('plain_text', '') for text in rich_text])
        return f"> {text_content}"

    def convert_to_markdown(self, notion_blocks: dict,folder_name: str) -> str:
        """
        Convert a list of Notion blocks to standard Markdown.
        
        :param notion_blocks: list of dicts representing Notion blocks
        :return: str containing the converted Markdown text
        """
        markdown = []
        for block in notion_blocks:
            if hasattr(block, 'get'):
                block_type = block.get('type')
                if block_type == 'text':
                    markdown.append(self.convert_text_block(block))
                elif block_type == 'heading_1':
                    markdown.append(self.convert_heading_block(block,1))
                elif block_type == 'heading_2':
                    markdown.append(self.convert_heading_block(block,2))
                elif block_type == 'heading_3':
                    markdown.append(self.convert_heading_block(block,3))
                elif block_type == 'heading_4':
                    markdown.append(self.convert_heading_block(block,4))
                elif block_type == 'bulleted_list':
                    markdown.append(self.convert_bulleted_list_block(block))
                elif block_type == 'numbered_list':
                    markdown.append(self.convert_numbered_list_block(block))
                elif block_type == 'paragraph':
                    markdown.append(self.convert_paragraph_block(block))
                elif block_type == 'image':
                    markdown.append(self.convert_image_block(block, folder_name))
                elif block_type == 'bulleted_list_item':
                    markdown.append(self.convert_bulleted_list_item_block(block))
                elif block_type == 'code':
                    markdown.append(self.convert_code_block(block))
                elif block_type == 'callout':
                    markdown.append(self.convert_callout_block(block))

        return '\n'.join(markdown)