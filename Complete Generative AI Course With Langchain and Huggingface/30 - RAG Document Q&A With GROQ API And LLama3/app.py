import streamlit as st
import os
import shutil
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load API Keys from the environment variables
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
os.environ['HF_TOKEN'] = os.getenv("HF_TOKEN")

# Initialize the LLM (Language Model) using Groq API and Llama3 model
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="Llama3-8b-8192")

# Initialize Hugging Face Embeddings for vector storage
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Define a structured prompt template for the retrieval-augmented generation (RAG) system
prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question.

    <context>
    {context}
    </context>

    Question: {input}
    """
)

# Create an upload directory for storing uploaded PDF files
UPLOAD_DIR = "uploaded_pdfs"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Streamlit UI Title
st.title("🔍 RAG Document Q&A With Groq and Llama3")

# File Upload Option: Allows users to upload multiple PDFs
uploaded_files = st.file_uploader("📂 Upload one or more PDF files", type=["pdf"], accept_multiple_files=True)

# Save uploaded PDFs to the local directory
if uploaded_files:
    for uploaded_file in uploaded_files:
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())  # Save file content to the disk
    st.success("✅ PDFs uploaded successfully!")  # Display success message

# Function to create FAISS vector embeddings from the uploaded PDFs
def create_vector_embedding():
    if "vectors" not in st.session_state:
        # Get the list of uploaded PDF files
        pdf_files = [os.path.join(UPLOAD_DIR, f) for f in os.listdir(UPLOAD_DIR) if f.endswith(".pdf")]
        if not pdf_files:
            st.error("❌ No PDFs uploaded. Please upload documents first.")
            return
        
        # Load and process each PDF file
        documents = []
        for pdf_file in pdf_files:
            loader = PyPDFLoader(pdf_file)  # Load PDF content
            documents.extend(loader.load())  # Append loaded documents

        # Split large documents into smaller chunks for better processing
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        final_documents = text_splitter.split_documents(documents)

        if not final_documents:
            st.error("❌ No text extracted from PDFs. Check the documents.")
            return

        # Create FAISS vector store from the processed documents
        st.session_state.vectors = FAISS.from_documents(final_documents, embeddings)
        st.success("✅ Vector database created successfully!")  # Show success message

# Button to trigger FAISS vector database creation
if st.button("⚙️ Create Document Embeddings"):
    create_vector_embedding()

# User input box for entering queries based on uploaded research papers
user_prompt = st.text_input("🔎 Enter your query from the research papers")

# Process the user's query if entered
if user_prompt:
    import time
    document_chain = create_stuff_documents_chain(llm, prompt)  # Create document chain for query handling
    
    # Ensure that the FAISS vector database exists before querying
    if "vectors" not in st.session_state or st.session_state.vectors is None:
        st.error("❌ Vector database is not ready. Click 'Create Document Embeddings' first.")
    else:
        retriever = st.session_state.vectors.as_retriever()  # Create retriever from FAISS database
        retrieval_chain = create_retrieval_chain(retriever, document_chain)  # Create retrieval chain

        # Measure response time for performance analysis
        start = time.process_time()
        response = retrieval_chain.invoke({'input': user_prompt})
        elapsed_time = time.process_time() - start

        # Display the AI-generated answer
        st.subheader("💡 Answer:")
        st.write(response['answer'])

        # Display relevant document snippets used for generating the response
        with st.expander("📄 Document Similarity Search"):
            for i, doc in enumerate(response['context']):
                st.write(f"**Document {i+1}:**")  # Show document number
                st.write(doc.page_content)  # Show document content
                st.write('------------------------')  # Separator line
