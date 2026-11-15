import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import os

import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")  # Set Langchain API Key
os.environ["LANGCHAIN_TRACING_V2"] = "true"  # Enable Langsmith tracing
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With Ollama"  # Set project name

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question:{question}")
    ]
)

# Function to generate response from Ollama model
def generate_response(question, llm, temperature, max_tokens):
    llm = Ollama(model=llm)  # Initialize Ollama model
    output_parser = StrOutputParser()  # Create output parser
    chain = prompt | llm | output_parser  # Chain together prompt, model, and output parser
    answer = chain.invoke({'question': question})  # Generate response based on user question
    return answer  # Return the generated response

## Title of the app
st.title("Enhanced Q&A Chatbot With Gemma2:2B")

## Sidebar settings
st.sidebar.title("Settings")  # Sidebar title

## Select the Open Source model
llm = st.sidebar.selectbox("Select Open Source model", ["gemma2:2b"])  # Model selection dropdown

## Adjust response parameters
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)  # Set temperature for response generation
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)  # Set max tokens limit

## Main interface for user input
st.write("Go ahead and ask any question")  # Display prompt for user
user_input = st.text_input("You:")  # Text input field for user question

# Process user input and generate response
if user_input:
    response = generate_response(user_input, llm, temperature, max_tokens)  # Call function to get response
    st.write(response)  # Display response
else:
    st.write("Please provide the user input")  # Prompt user to enter input if empty