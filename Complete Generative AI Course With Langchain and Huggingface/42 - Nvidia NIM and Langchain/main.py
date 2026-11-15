import streamlit as st
import os
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings, ChatNVIDIA
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
os.environ['NVIDIA_API_KEY'] = os.getenv("NVIDIA_API_KEY")  # Set NVIDIA API Key from .env file

# Get the project root directory dynamically
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the PDF directory
PDF_DIR = os.path.join(PROJECT_DIR, "us_census")

# Streamlit App Title
st.title("Nvidia NIM Demo with FAISS Vector DB")

# Function to check if PDFs exist in the folder
def check_pdfs():
    if not os.path.exists(PDF_DIR):  # Check if the folder exists
        st.error(f"Folder '{PDF_DIR}' does not exist. Please create it and add PDFs.")
        return False

    pdf_files = [f for f in os.listdir(PDF_DIR) if f.endswith(".pdf")]  # List all PDF files in the folder
    
    if not pdf_files:
        st.error(f"No PDFs found in '{PDF_DIR}'. Please add files.")
        return False
    
    st.write(f"Found PDF files: {pdf_files}")  # Show the list of found PDFs
    return True

# Function to Embed and Store Documents
def vector_embedding():
    if "vectors" not in st.session_state:
        if not check_pdfs():  # Ensure PDFs exist before proceeding
            return

        st.session_state.embeddings = NVIDIAEmbeddings()  # Initialize NVIDIA Embeddings

        # Load PDFs from the specified directory
        st.session_state.loader = PyPDFDirectoryLoader(PDF_DIR)
        st.session_state.docs = st.session_state.loader.load()
        
        if not st.session_state.docs:
            st.error("Failed to load PDFs. Please check the files and try again.")
            return

        # Split Documents into Chunks for better processing
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=50)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:30])

        if not st.session_state.final_documents:
            st.error("Document splitting failed. Try adjusting chunk size or check the PDFs.")
            return

        # Check NVIDIA Embeddings by testing with a sample query
        try:
            test_embedding = st.session_state.embeddings.embed_query("Test query")
            if not test_embedding:
                st.error("NVIDIA Embeddings are not working. Check your API key and model settings.")
                return
        except Exception as e:
            st.error(f"NVIDIA Embeddings Error: {e}")
            return

        # Create FAISS vector store from document embeddings
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)
        st.success("Vector Store DB is initialized successfully!")

# Create the Chat Model (Llama3-70B from NVIDIA NIM)
llm = ChatNVIDIA(model="meta/llama3-70b-instruct")

# Define Prompt Template for answering questions
prompt = ChatPromptTemplate.from_template(
"""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question.

<context>
{context}
<context>

Question: {input}
"""
)

# Input box for user to enter a query
prompt1 = st.text_input("🔍 Enter Your Question From Documents")

# Button to Create Embeddings
if st.button("Create Document Embeddings"):
    vector_embedding()

# Query Processing & Response Generation
if prompt1:
    if "vectors" not in st.session_state:
        st.error("No vector store found. Please click 'Create Document Embeddings' first.")
    else:
        document_chain = create_stuff_documents_chain(llm, prompt)  # Create a document processing chain
        retriever = st.session_state.vectors.as_retriever()  # Retrieve relevant documents
        retrieval_chain = create_retrieval_chain(retriever, document_chain)  # Create the final retrieval chain
        
        start_time = time.process_time()
        response = retrieval_chain.invoke({'input': prompt1})  # Get response from the AI model
        elapsed_time = time.process_time() - start_time
        
        st.write(f"Response Time: {elapsed_time:.2f} seconds")
        st.write("### AI Response:")
        st.write(response['answer'])

        # Show Relevant Document Chunks for transparency
        with st.expander("Document Similarity Search Results"):
            for i, doc in enumerate(response["context"]):
                st.write(f"**Chunk {i+1}:**")
                st.write(doc.page_content)
                st.write("---")