# TecnooseNotionExporter

A project to export Notion content to Markdown and save it to the file system.

## Notion

    To ensure the correct execution of the program, the following properties must be available in your Notion database:

    - **Title**: The main title of the page.
    - **Content**: The content of the page, which will be exported to Markdown.
    - **Tags**: Multi-select property to filter the post to process. The program will request all the notion pages where the multi select property Tags contains the word Post  
    - **Last Edited Time**: The timestamp of the last edit, used to track changes.

    Make sure these properties are defined in your Notion database schema to allow the exporter to function correctly.

## Setup

    Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Configuration

    To configure the project, open the `global_configuration.py` file in the config directory of the project and apply the following configuration:

    ```python
    # global_configuration.py
    
    # Add your configuration variables here
    api_key: str = 'your_notion_api_key'
    database_id: str = "your_notion_database_id"
    export_path = 'path to export the markdown file'
    ```

## Run

    Run the main script:

    ```sh
    python -m tecnoose_notion_exporter.main
    ```
