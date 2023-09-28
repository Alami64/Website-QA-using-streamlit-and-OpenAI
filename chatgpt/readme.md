# Website Content Question Answering

A Streamlit-based web application designed to allow users to input a website URL, process its content, and then ask questions about the content. The application then provides answers to these questions using OpenAI's GPT-3.5 model.

## Overview

- Streamlit-based web application
- Input a website URL
- Process and analyze its content
- Ask questions and get answers

## Features

- **Website URL Input**: Users can input the URL of any website they wish to analyze.
- **Web Crawling**: After a URL is provided, the application crawls the website's content.
- **Question & Answering**: Users can ask questions about the website's content, and the application provides relevant answers.

## Key Modules

- **Web Crawling**: Uses `BeautifulSoup` from the `beautifulsoup4` library to extract content from websites.
- **Data Processing**: Processes the crawled data, tokenizes the content, and creates embeddings using OpenAI's API.
- **HTML Parsing**: Extracts hyperlinks from HTML content to guide the web crawling process.

## Dependencies

Ensure you have the following libraries installed:

- `streamlit`
- `openai`
- `beautifulsoup4`
- `numpy` & `pandas`
- `requests`

To install all dependencies, run:

`pip install -r requirements.txt`

## How to Run

1. Clone the repository:

   `git clone https://github.com/Alami64/ChatGPT.git`

2. Navigate to the project directory:

   `cd chatgpt`
   `cd chatgpt`

3. Set up the `.env` file with the necessary keys. Use a text editor to add the following line:

   `OPENAI_API_KEY=YOUR_KEY_HERE`

4. Run the Streamlit app:

   `streamlit run app.py`

