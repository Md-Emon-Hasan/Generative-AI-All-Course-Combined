# Complete Generative AI: From Basics to Advanced

<!-- Technologies used across the lessons and projects -->
<p align="center">
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch">
  <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="Hugging Face">
  <img src="https://img.shields.io/badge/Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="Transformers">
  <img src="https://img.shields.io/badge/Diffusers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="Diffusers">
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge" alt="LangChain">
  <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge" alt="LangGraph">
  <img src="https://img.shields.io/badge/LlamaIndex-7B61FF?style=for-the-badge" alt="LlamaIndex">
  <img src="https://img.shields.io/badge/ChromaDB-5B4BDB?style=for-the-badge" alt="ChromaDB">
  <img src="https://img.shields.io/badge/Pinecone-00A98F?style=for-the-badge" alt="Pinecone">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
</p>
<p align="center">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI">
  <img src="https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" alt="Google Gemini">
  <img src="https://img.shields.io/badge/Groq-F55036?style=for-the-badge" alt="Groq">
  <img src="https://img.shields.io/badge/Agno-000000?style=for-the-badge" alt="Agno">
  <img src="https://img.shields.io/badge/Model%20Context%20Protocol-5B5BD6?style=for-the-badge" alt="Model Context Protocol">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/NLTK-154F3C?style=for-the-badge" alt="NLTK">
</p>

<p align="center">
  <img src="banner.png" alt="Complete Generative AI learning roadmap banner" width="100%">
</p>

> A hands-on learning repository covering the path from text processing and language models to retrieval-augmented generation, fine-tuning, multimodal AI, and agent workflows.

## About

This repository is a collection of practical lessons, Jupyter notebooks, and focused applications for learning generative AI. The material progresses from foundational NLP and vectorization through Hugging Face, open-source language models, LangChain, vector databases, RAG, and modern AI agent patterns.

The numbered folders preserve the course sequence. The available lessons are numbered consecutively in the order shown below. Notebook dependencies and external services vary by lesson, so there is no single root-level installation that runs every example.

## Learning roadmap

### Foundations and Hugging Face

| Lesson | Folder | What you will find |
| --- | --- | --- |
| 01 | [Data Preprocessing & Cleaning](01%20Data%20Preprocessing%20%26%20Cleaning/) | Text normalization, lowercasing, HTML and URL cleanup, and other preprocessing steps. |
| 02 | [Data Representation & Vectorization](02%20Data%20Representation%20%26%20Vectorization/) | One-hot encoding, bag of words, n-grams, and vector representations for text. |
| 03 | [How ChatGPT Is Trained & Hugging Face](03%20How%20ChatGPT%20is%20Trained%20%26%20Hugging%20Face%20Platform%20Explained/) | Hugging Face tasks and platform basics, model training concepts, and fine-tuning introduction. |
| 04 | [Tokenization & Fine-Tuning with Hugging Face](04%20Tokenization%20%26%20Fine-Tuning%20with%20Hugging%20Face/) | Tokenization and fine-tuning a language model on custom data. |
| 05 | [Text Summarization with Hugging Face](05%20Generative%20AI%20Project%20Text%20Summarization%20with%20Hugging%20Face/) | A practical text summarization project. |
| 06 | [Text, Image & Speech Generation](06%20Text%20to%20Image%20%26%20Speech%20Generation%20with%20Hugging%20Face/) | Text-to-image generation with Diffusers and Stable Diffusion, image-generation parameters, and text-to-speech. |

### Frameworks, retrieval, and open-source models

| Lesson | Folder | What you will find |
| --- | --- | --- |
| 07 | [Vector Databases Practical Tutorial](07%20Vector%20Databases%20Practical%20Tutorial/) | A ChromaDB notebook introducing vector database setup, collections, and storage. |
| 08 | [LangChain Explained](08%20LangChain%20Explained/) | Introductory LangChain and chat-model concepts. |
| 09 | [Mastering LangChain, Part 2](09%20Mastering%20LangChain%20Part-2/) | Prompting, few-shot examples, and chains. |
| 10 | [Mastering LangChain, Part 3](10%20Mastering%20LangChain%20Part-3/) | Document loading, text splitting, embeddings, RAG components, and a basic RAG implementation. |
| 11 | [LangChain Expression Language (LCEL)](11%20Mastering%20LangChain%20Expression%20Language%20%28LCEL%29/) | LCEL chains and built-in runnables, including parallel, lambda, and passthrough patterns. |
| 12 | [LangChain Memory & LCEL](12%20Mastering%20LangChain%20Memory%20%26%20LCEL/) | Composing LCEL chains and exploring conversational memory. |
| 13 | [LangChain Ecosystem](13%20LangChain%20Ecosystem/) | Introductory LangGraph and LangSmith examples. |
| 14 | [LlamaIndex Explained](14%20LlamaIndex%20Explained/) | Indexing private documents, querying data, and deeper LlamaIndex concepts. |
| 15 | [Introduction to Open-Source LLMs](15%20Introduction%20to%20Open%20Source%20LLMs/) | An introductory Llama 2 model walkthrough. |
| 16 | [Open-Source LLMs with LangChain](16%20Open%20Source%20LLM%20with%20LangChain/) | Connecting an open-source LLM workflow with LangChain. |
| 17 | [Custom Website Chatbot](17%20Custom%20Website%20Chatbot%20with%20Open%20Source%20LLMs/) | Crawling website content, preparing documents, and building a chatbot with an open model. |
| 18 | [Fine-Tuning Open-Source LLMs](18%20Fine-Tuning%20Open%20Source%20LLMs%20with%20Custom%20Data/) | Fine-tuning experiments and model testing with custom data. |

### Applied RAG and agent projects

| Lesson | Folder | What you will find |
| --- | --- | --- |
| 19 | [End-to-End Medical Chatbot](19%20End%20to%20End%20Medical%20Chatbot%20Project/) | A Flask chat app that retrieves context from a Pinecone index and uses an OpenAI chat model. Includes a PDF data source, ingestion script, templates, and project-specific instructions. |
| 20 | [Multimodal RAG Development](20%20Multimodal%20RAG%20Development/) | A notebook exploring document content that combines text, tables, and images, with supporting figures and a sample financial report. |
| 21 | [AI Agents with Agno](21%20Build%20AI%20Agents%20with%20Agno/) | A team of web-search and financial agents using Groq, Gemini, DuckDuckGo, and YFinance tools. |
| 22 | [AI Agent with LangGraph](22%20AI%20agent%20using%20LangGraph/) | A ReAct-style LangGraph agent using Gemini and Tavily web search. |
| 23 | [AI Agent with MCP](23%20AI%20Agent%20with%20MCP%20using%20MCP-USE/) | An MCP-use chat agent with Groq and browser MCP configuration. Review its configuration file and update the local path before running. |

## Repository structure

```text
.
├── 03–10   NLP foundations, Hugging Face, and generation notebooks
├── 16–22   Vector databases, LangChain, LCEL, and LangSmith/LangGraph
├── 26–31   LlamaIndex, open models, chatbots, and fine-tuning
├── 32      Medical chatbot application
├── 36–38   Multimodal RAG and agent examples
├── 44      MCP agent project
├── banner.png
├── LICENSE
└── README.md
```

Most lesson folders contain one or more `.ipynb` notebooks. Applied projects include their own source code and may include a local README and requirements file. The root does not currently contain a shared `requirements.txt` or a single application entry point.

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/Md-Emon-Hasan/Complete-Generative-AI-with-Basic-to-Advanced.git
cd Complete-Generative-AI-with-Basic-to-Advanced
```

### 2. Create a Python environment

Python 3.10 or newer is a reasonable starting point for the notebooks. Individual projects may require a different version; check that project's own configuration before installing dependencies.

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

Install Jupyter for notebook-based lessons:

```bash
python -m pip install --upgrade pip
python -m pip install jupyter ipykernel
```

### 3. Open a lesson

Start Jupyter from the repository root and open the notebook for the lesson you want to follow:

```bash
jupyter lab
```

Install the packages needed by that notebook in the active environment. Notebooks may use hosted APIs, model downloads, or local GPU resources; read the setup cells before running them.

### 4. Run a standalone project

For projects that include a `requirements.txt`, change into that project directory and install its dependencies there. For example, the medical chatbot has its own setup guide:

```bash
cd "19 End to End Medical Chatbot Project"
python -m pip install -r requirements.txt
```

Follow the project README for required credentials, data ingestion, and launch commands. Avoid installing requirements from unrelated project folders into one shared environment because their dependency versions differ.

## API keys and configuration

Several notebooks and applications call hosted model or search services. Create credentials with the relevant provider and configure only the keys required by the lesson you are running. A local `.env` file is a common option:

```dotenv
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

These names are examples drawn from the included projects; not every project needs every key. Keep real credentials private, do not commit `.env` files, and check each notebook or project's README for its exact configuration. Some model examples also require access to model weights, a compatible GPU, or external services.

## Selected project guides

- [Medical chatbot project README](19%20End%20to%20End%20Medical%20Chatbot%20Project/README.md): Flask app, PDF ingestion, Pinecone, and OpenAI configuration.
- [Multimodal RAG project README](20%20Multimodal%20RAG%20Development/README.md): environment notes for the multimodal notebook. Its `requirements-dev.txt` is a machine-generated environment export containing local file URLs, so it is not portable to another machine; use the main requirements file and install any additional notebook dependencies as needed.
- [MCP agent project README](23%20AI%20Agent%20with%20MCP%20using%20MCP-USE/mcp-agent/README.md): MCP agent setup and configuration.

## Notes and limitations

- This is a learning repository: notebooks are exploratory and may need package or API updates to work with current provider SDKs.
- Dependencies are defined per project where available. There is no repository-wide lockfile or automated compatibility matrix.
- Some examples incur charges from third-party model, embedding, vector database, or search providers.
- The MCP example's `browser_mcp.json` and `main.py` include machine-specific configuration assumptions. Update them for your environment before use, and keep credentials out of committed files.
- The medical chatbot demonstrates retrieval over medical reference material; it is an educational example and is not a substitute for professional medical advice.

## Contributing

Contributions that improve explanations, fix notebook issues, or add focused examples are welcome.

1. Fork the repository and create a branch for your change.
2. Keep examples focused and place them in the appropriate numbered lesson or project folder.
3. Document required packages, environment variables, data, and run steps near the example.
4. Remove secrets and machine-specific paths from committed changes.
5. Open a pull request describing what changed and how to follow or run it.

## License

The repository is distributed under the [Apache License 2.0](LICENSE). Individual folders may include their own license files; check those before reusing project-specific material.

## Connect with me

- **Portfolio:** [emonlabs-ai.hitechparks.com](https://emonlabs-ai.hitechparks.com)
- **GitHub:** [Md-Emon-Hasan](https://github.com/Md-Emon-Hasan)
- **LinkedIn:** [Md Emon Hasan](https://www.linkedin.com/in/md-emon-hasan-695483237/)
- **Hugging Face:** [emonHasan01](https://huggingface.co/emonHasan01)
- **Email:** [emon.mlengineer@gmail.com](mailto:emon.mlengineer@gmail.com)
- **WhatsApp:** [+880 1834-363533](https://wa.me/8801834363533)
