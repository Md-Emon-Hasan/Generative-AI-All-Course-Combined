# Import necessary libraries
import os  # For environment variables
import streamlit as st
from dotenv import load_dotenv  # Load environment variables
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler

# Load environment variables from .env file
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Streamlit app setup
st.set_page_config(page_title="Text to Math Problem Solver and Data Search Assistant", page_icon="🧮")
st.title("Text to Math Problem Solver Using Google Gemma 2")

# Check if API key is available
if not groq_api_key:
    st.error("Missing API Key! Please set GROQ_API_KEY in the .env file.")
    st.stop()

# Initialize LLM model
llm = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

# Initialize the Wikipedia search tool
wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="A tool for searching Wikipedia to find various information on mentioned topics."
)

# Initialize the Math solver tool
math_chain = LLMMathChain.from_llm(llm=llm)
calculator = Tool(
    name="Calculator",
    func=math_chain.run,
    description="A tool for solving math-related questions. Input should contain only mathematical expressions."
)

# Define prompt for reasoning tool
prompt = """
You are an AI assistant that solves mathematical questions. 
Logically arrive at the solution and provide a detailed explanation, displaying it point-wise.

Question: {question}
Answer:
"""

prompt_template = PromptTemplate(
    input_variables=["question"],
    template=prompt
)

# Create a reasoning tool
chain = LLMChain(llm=llm, prompt=prompt_template)
reasoning_tool = Tool(
    name="Reasoning Tool",
    func=chain.run,
    description="A tool for answering logic-based and reasoning questions."
)

# Initialize the agent with all tools
assistant_agent = initialize_agent(
    tools=[wikipedia_tool, calculator, reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi! I'm a math chatbot. I can help you solve math problems and search for information."}
    ]

# Display chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input field
question = st.text_area("Enter your question:", 
                        "A jar contains 100 candies. I take out 25 candies and give 15 to my friends. Later, I buy another 50 candies and put them in the jar. My sister eats 10 candies. How many candies are in the jar now?")

# Process the user query
if st.button("Find my answer"):
    if question:
        with st.spinner("Generating response... Please wait."):
            # Store user message
            st.session_state.messages.append({"role": "user", "content": question})
            st.chat_message("user").write(question)

            # Generate response
            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = assistant_agent.run(st.session_state.messages, callbacks=[st_cb])

            # Store assistant response
            st.session_state.messages.append({"role": "assistant", "content": response})

            # Display response
            st.write("### Response:")
            st.success(response)
    else:
        st.warning("Please enter a question.")