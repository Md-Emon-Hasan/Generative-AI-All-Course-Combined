# Medical Knowledge Chatbot

A small Flask application that answers questions using retrieved passages from the included medical reference PDF. It uses LangChain for retrieval, Pinecone for vector storage, Hugging Face sentence-transformer embeddings, and OpenAI for answer generation.

> Educational demonstration only. It is not a medical device and must not be used to diagnose, treat, or make healthcare decisions.

## Requirements

- Python 3.10 or newer
- Pinecone account and API key
- OpenAI API key
- Internet access to download the embedding model and call hosted services

## Setup

Run these commands from this project directory:

```bash
python -m venv .venv
```

Activate the environment, then install dependencies:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Create a `.env` file beside `app.py`:

```dotenv
PINECONE_API_KEY=your_pinecone_api_key
OPENAI_API_KEY=your_openai_api_key
```

Do not commit this file. The application uses the Pinecone index `medical-bot`; the ingestion script creates it in AWS `us-east-1` when it does not exist.

## Index the reference document

The `data/` folder contains the PDF used by the example. From this project directory, run:

```bash
python store_index.py
```

This loads PDFs in `data/`, splits the text into chunks, creates 384-dimensional embeddings with `sentence-transformers/all-MiniLM-L6-v2`, and uploads them to Pinecone. Run this again when adding or changing source documents.

## Start the app

```bash
python app.py
```

Open [http://localhost:8080](http://localhost:8080). The Flask development server is configured for local learning and should not be exposed as a production service.

## Project layout

```text
.
├── app.py              # Flask application and retrieval chain
├── store_index.py      # PDF ingestion and Pinecone indexing
├── data/               # Source PDF documents
├── src/                # Embedding, loading, and prompt helpers
├── templates/          # Chat page
└── static/             # Stylesheets
```

## Troubleshooting

- **Missing or invalid API key:** confirm `.env` is beside `app.py` and contains valid Pinecone and OpenAI credentials.
- **No matching index:** run `python store_index.py` and confirm the index name and Pinecone account match.
- **Embedding or PDF errors:** check internet access and verify that the PDF is readable and located in `data/`.
- **Dependency conflicts:** use a fresh virtual environment for this project rather than sharing one with another lesson.
