
# Research Report Generator at Notion

Research Report Generator at Notion is a program designed to read ideas from an `idea.txt` file and automatically generate detailed reports on a Notion page using Large Language Models (LLMs).

## Requirements

This project requires the following credentials in a `.env` file:

- **Notion API Key**: For interacting with the Notion API to create and update Notion pages.
- **OpenAI API Key**: For generating reports using OpenAI's LLM.

## .env Configuration

Create a `.env` file with the following variables:
```plaintext
# Notion Credentials
NOTION_API_KEY=

# OpenAI Credentials
OPEN_AI=
```

## Running the Program

To start the program, use the following command:

```bash
python3 index.sh
```

This script reads ideas from `idea.txt`, generates a report using OpenAI’s LLM, and posts the report to a Notion page.

## Attribution

This project is a **DRJSLAB creation**, aimed at simplifying the process of generating structured research reports based on initial ideas.