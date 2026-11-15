import streamlit as st
from groq import Groq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

# Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With Groq"

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user's queries."),
        ("user", "Question: {question}")
    ]
)

def generate_response(question, api_key, engine, temperature, max_tokens):
    client = Groq(api_key=api_key)
    
    response = client.chat.completions.create(
        model=engine,
        messages=[{"role": "user", "content": question}],
        temperature=temperature,
        max_tokens=max_tokens
    )
    
    return response.choices[0].message.content

# Title of the app
st.title("Enhanced Q&A Chatbot With Groq")

# Sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

# Select the Groq model
engine = st.sidebar.selectbox("Select Groq model", ["gemma2-9b-it","llama-3.3-70b-versatile", "mistral-saba-24b"])  # Update with actual Groq-supported models

# Adjust response parameters
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

# Main interface for user input
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input and api_key:
    response = generate_response(user_input, api_key, engine, temperature, max_tokens)
    st.write(response)

elif user_input:
    st.warning("Please enter the Groq API Key in the sidebar.")
else:
    st.write("Please provide user input.")