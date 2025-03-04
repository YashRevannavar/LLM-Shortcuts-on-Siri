# LLM-Shortcuts-on-Siri

## Overview

**LLM-Shortcuts-on-Siri** is a project that enables Siri to deliver **daily AI-generated news summaries** using *
*Mistral AI**. It scrapes top AI-related headlines, extracts content, and generates a human-like spoken summary
optimized for Siri Shortcuts.

## Features

- **Automated News Fetching**: Extracts top headlines from websites like TechCrunch.
- **Summarization with Mistral AI**: Converts articles into concise, natural-sounding news reports.
- **Siri Integration**: Fetch and listen to AI news by triggering a Siri Shortcut.
- **Optimized for Audio**: Generates human-like spoken summaries instead of structured text.

## How It Works

1. **Headline Extraction**: Uses `BeautifulSoup` to scrape top AI news URLs.
2. **Content Processing**: Loads full articles via `WebBaseLoader`, truncates content.
3. **AI Summarization**: Mistral AI generates a personalized, spoken summary.
4. **Siri Shortcut**: iPhone Shortcuts fetch the summary via an API and read it aloud.

## Tech Stack

- **Python** (FastAPI for Lambda API, BeautifulSoup for scraping)
- **AWS Lambda** (serverless function to process and serve news)
- **API Gateway** (secure endpoint for Siri Shortcuts)
- **Mistral AI** (for AI-generated summaries)
- **Langchain** (for LLM model handling)

## Usage

1. Deploy the **AWS Lambda function** and expose it via API Gateway.
2. Set up an **iPhone Shortcut** to call the API.
3. Siri will **fetch, process, and read** the latest AI news to you.

