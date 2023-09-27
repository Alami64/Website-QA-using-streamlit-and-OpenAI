import streamlit as st
import openai
from webcrawler import crawl
from dataprocessing import remove_newlines, process_crawled_data, tokenize_data, split_into_many, shorten_text_based_on_tokens, generate_text_embeddings, process_loaded_embeddings, create_context, answer_question
from urllib.parse import urlparse
from dotenv import load_dotenv
import os


def main():

    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    st.title("Website Content Question Answering")
   
    # Initialize session state variables
    if 'processed' not in st.session_state:
        st.session_state.processed = False
    if 'df' not in st.session_state:
        st.session_state.df = None

    # 1. A text input for users to enter the website URL.
    website_url = st.text_input("Enter the website URL:")

    # 2. A button to initiate the processing of the website content.
    if st.button("Process Website"):

         # The code to process the website content will go here...
        crawl(website_url)
        domain = ".".join(urlparse(website_url).netloc.split(".")[-2:])
        df = process_crawled_data(domain)
        df = tokenize_data(df)
        st.session_state.df = df
        st.session_state.processed = True
        st.success("Website Crawled Successfully")

    if st.session_state.processed:
        # 3. An input area for users to ask questions about the website content.
        question = st.text_input("Ask a question about the website:")

        # 4. Display the answer to the user's question.
        if question:
            df = st.session_state.df
            df = generate_text_embeddings(df)
            df = process_loaded_embeddings(df)
            answer = answer_question(df,question=question)
            st.write(f"Answer: {answer}")


if __name__ == "__main__":
    main()
