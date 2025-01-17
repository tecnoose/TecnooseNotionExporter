from notion_service import NotionService
from markdown_service import MarkdownService
from file_service import FileService
from global_configuration import Config

def Main():
    notionService = NotionService()
    pagesToPost = notionService.queryPosts(Config.Notion.database_id)

    if not pagesToPost or "results" not in pagesToPost or len(pagesToPost["results"]) == 0:
        print("No pages to post.")
    else:
        markdownService = MarkdownService()
        fileService = FileService()
        print(f"Found {len(pagesToPost['results'])} pages to post.")
        for page in pagesToPost["results"]:
            print(f"Title found: {page['properties']['Name']['title'][0]['text']['content']}")
            page_id = page['id']
            pageBlocks = notionService.getPageBlocks(page_id)

            if not pageBlocks or "results" not in pageBlocks or len(pageBlocks["results"]) == 0:
                print("No pages blocks found.")
            else:
                post_folder_name = f"{page['properties']['Name']['title'][0]['text']['content']}".replace(' ','-')
                #delete in case of rebuilding
                fileService.delete_folder(post_folder_name)
                #create post structure 
                fileService.create_post_root_folder(post_folder_name)
                fileService.create_post_images_folder(post_folder_name)
                # convert to MD 
                markdown_content = markdownService.convert_to_markdown(pageBlocks.get("results"),post_folder_name)
                if markdown_content != "":
                    # save file to configured location
                    fileService.create_post(post_folder_name,markdown_content) 

if __name__ == "__main__":
    Main()
