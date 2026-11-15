# Import necessary libraries
import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Check if GROQ API key is available
if not groq_api_key:
    st.error("GROQ API Key not found! Please add it to your .env file.")

# Initialize Arxiv and Wikipedia tools
# Arxiv tool for querying research papers
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

# Wikipedia tool for querying Wikipedia content
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)

# DuckDuckGo search tool for general web searches
search = DuckDuckGoSearchRun(name="Search")

# Streamlit UI setup
st.title("🔎 LangChain - Chat with Search")
"""
In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
Try more LangChain 🤝 Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
"""

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

# Display chat messages from history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Process user input
if prompt := st.chat_input(placeholder="What is machine learning?"):
    # Add user's message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Check if GROQ API key is available
    if not groq_api_key:
        st.error("🚨 Cannot proceed without a GROQ API Key.")
    else:
        # Initialize the Groq language model with streaming enabled
        llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192", streaming=True)
        
        # Define the tools available for the agent
        tools = [search, arxiv, wiki]

        # Initialize the agent with the tools and Groq model
        search_agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True)

        # Display assistant's response in the chat
        with st.chat_message("assistant"):
            # Use StreamlitCallbackHandler to display agent's thoughts and actions
            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            # Run the agent with the chat history and callbacks
            response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
            # Add assistant's response to chat history
            st.session_state.messages.append({'role': 'assistant', "content": response})
            # Display the response
            st.write(response)
