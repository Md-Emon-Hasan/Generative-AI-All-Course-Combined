# Import necessary libraries
import os  # For environment variable handling
import validators  # For URL validation
import streamlit as st  # For creating the web app
from dotenv import load_dotenv  # For loading .env variables
from langchain.prompts import PromptTemplate  # For creating prompt templates
from langchain_groq import ChatGroq  # For interacting with the Groq API
from langchain.chains.summarize import load_summarize_chain  # For summarization chains
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader  # For loading content from URLs or YouTube

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")  # Read API key from .env file

# Streamlit app configuration
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader('Summarize URL')

# Input field for URL (YouTube or website)
generic_url = st.text_input("Enter URL (YouTube or Website)", label_visibility="visible")

# Initialize the Groq model
if not groq_api_key:
    st.error("Missing API Key! Please set GROQ_API_KEY in the .env file.")
else:
    llm = ChatGroq(model="Llama3-8b-8192", groq_api_key=groq_api_key)

    # Define the prompt template for summarization
    prompt_template = """
    Provide a summary of the following content in 300 words:
    Content:{text}
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

    # Button to trigger summarization
    if st.button("Summarize the Content from YT or Website"):
        if not generic_url.strip():
            st.error("Please enter a valid URL.")
        elif not validators.url(generic_url):  # Validate the URL
            st.error("Invalid URL! Please enter a valid YouTube or Website URL.")
        else:
            try:
                with st.spinner("Processing... Please wait."):
                    # Load content from YouTube or website
                    if "youtube.com" in generic_url:  # Check if the URL is a YouTube video
                        loader = YoutubeLoader.from_youtube_url(generic_url, add_video_info=True)
                    else:  # For website URLs
                        loader = UnstructuredURLLoader(
                            urls=[generic_url],
                            ssl_verify=False,  # Disable SSL verification
                            headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
                        )
                    docs = loader.load()  # Load the content

                    # Create a summarization chain using the 'stuff' method
                    chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                    output_summary = chain.run(docs)  # Generate the summary

                    st.success(output_summary)  # Display the summary
            except Exception as e:
                st.error(f"Error: {e}")  # Handle exceptions
