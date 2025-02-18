from tecnoose_notion_exporter.utils.import_logging import logger as logging
from tecnoose_notion_exporter.services.notion_service import NotionService
from tecnoose_notion_exporter.services.markdown_service import MarkdownService
from tecnoose_notion_exporter.services.file_service import FileService
from tecnoose_notion_exporter.config.global_configuration import Config



def main():
    """
    Main function to query posts from Notion, convert them to Markdown,
    and save them to the file system.
    """
    Config.ToString()

    def is_empty_or_no_results(pages):
        return not pages or "results" not in pages or len(pages["results"]) == 0

    try:
        notion_service = NotionService()
        pages_to_post = notion_service.query_posts(Config.Notion.database_id)

        if is_empty_or_no_results(pages_to_post):
            logging.error("Failed to query posts from Notion. The database ID might be invalid.")
            return

        if "results" not in pages_to_post or len(pages_to_post["results"]) == 0:
            logging.info("No pages to post.")
            return

        markdown_service = MarkdownService()
        file_service = FileService()
        logging.info(f"Found {len(pages_to_post['results'])} pages to post.")

        for page in pages_to_post["results"]:
            properties = page.get('properties', {})
            name = properties.get('Name', {})
            title_list = name.get('title', [])
            if title_list and 'text' in title_list[0] and 'content' in title_list[0]['text']:
                title = title_list[0]['text']['content']
                logging.info(f"Title found: {title}")
            else:
                logging.info("Title not found.")
                continue

            page_id = page['id']
            page_blocks = notion_service.get_page_blocks(page_id)

            if page_blocks is None or "results" not in page_blocks or len(page_blocks["results"]) == 0:
                logging.info("No page blocks found.")
                continue

            post_folder_name = title.replace(' ', '-')
            file_service.delete_folder(post_folder_name)
            file_service.create_post_root_folder(post_folder_name)
            file_service.create_post_images_folder(post_folder_name)

            markdown_content = markdown_service.convert_to_markdown(page_blocks.get("results"), post_folder_name)
            if markdown_content:
                file_service.create_post(post_folder_name, markdown_content)
                notion_service.update_page_tags(page_id)

    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()