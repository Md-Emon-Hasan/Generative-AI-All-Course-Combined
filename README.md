# Generative AI: All Courses Combined

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-Workflows-1C3C3C?logo=langchain&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Models-FFD21E?logo=huggingface&logoColor=black)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?logo=googlegemini&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Apps-FF4B4B?logo=streamlit&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Apps-000000?logo=flask&logoColor=white)
![Chroma](https://img.shields.io/badge/Chroma-Vector%20Database-5B43D6)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-0467DF)
![MCP](https://img.shields.io/badge/MCP-Tool%20Integration-6A5ACD)

<p align="center">
  <img src="banner.png" alt="Generative AI learning and project collection" width="100%">
</p>

> A curated learning repository bringing together seven hands-on collections on generative AI, Python, machine learning, LangChain, LangGraph, RAG, and AI agents.

## About

This repository combines course notes, Jupyter notebooks, Python examples, and small application projects in one place. It is organized into independent course folders so you can follow a curriculum or jump directly to a topic. Materials range from Python and NLP foundations through LLM applications, retrieval-augmented generation (RAG), and agent workflows.

The folders are course collections, not a single installable application. Dependencies, model providers, and setup steps vary by lesson. Some examples call hosted model APIs; others use local models or notebooks. Check the lesson's code and any local README or requirements file before running it.

## Contents

- [Choose a learning path](#choose-a-learning-path)
- [Course collections](#course-collections)
- [Technology overview](#technology-overview)
- [Getting started](#getting-started)
- [API keys and environment variables](#api-keys-and-environment-variables)
- [Working with notebooks](#working-with-notebooks)
- [Repository layout](#repository-layout)
- [Contributing](#contributing)
- [License](#license)
- [Connect with me](#connect-with-me)

## Choose a learning path

| If you want to learn… | Start here |
| --- | --- |
| Python and practical Gemini-powered apps | [12+ Generative AI Apps with Gemini Pro](./12-Plus-Generative-AI-App-with-Gemini-Pro/) |
| Machine learning, NLP, and a broad LangChain/Hugging Face course | [Generative AI Course with LangChain and Hugging Face](./Complete%20Generative%20AI%20Course%20With%20Langchain%20and%20Huggingface/) |
| LLM fundamentals, vector databases, and applied generative AI projects | [Complete Generative AI Mastery](./Complete%20Generative%20AI%20Mastery/) |
| Agent design, LangChain, LangGraph, and human-in-the-loop flows | [Complete Agentic AI with LangChain and LangGraph](./Complete-Agentic-AI-With-LangChain-and-LangGraph/) |
| A topic-by-topic introduction from data preparation through MCP | [Generative AI: Basic to Advanced](./Complete-Generative-AI-with-Basic-to-Advanced/) |
| LangChain components, RAG, tools, and agents | [LangChain from CampusX](./Complete-LangChain-From-CampusX/) |
| LangGraph workflows, state, persistence, and tool calling | [LangGraph from CampusX](./Complete-LangGraph-From-CampusX/) |

## Course collections

### 1. [12+ Generative AI Apps with Gemini Pro](./12-Plus-Generative-AI-App-with-Gemini-Pro/)

Begins with Python programming, control flow, data structures, functions, modules, file handling, exceptions, and object-oriented programming. The later lessons contain practical Gemini-focused applications, including:

- Image analysis with a question-and-answer chatbot
- Conversational Q&A chatbot
- Multilingual invoice extraction
- Chat with multiple PDF documents
- Document Q&A using Gemini and the Groq API
- Natural-language-to-SQL conversion
- Applicant tracking and resume analysis
- Nutrition breakdown and health insights
- YouTube transcript-to-notes conversion

The folder contains notebooks and individual app scripts. Follow each app's code for its model/API configuration and launch command.

### 2. [Complete Generative AI Course with LangChain and Hugging Face](./Complete%20Generative%20AI%20Course%20With%20Langchain%20and%20Huggingface/)

A broad curriculum spanning Python foundations, Streamlit, classical machine learning for NLP, neural network examples, and LLM applications. Included topics and projects cover:

- Python basics, control flow, data structures, functions, modules, file handling, exceptions, and OOP
- Streamlit fundamentals
- NLP preprocessing, bag-of-words, TF-IDF, Word2Vec, and named-entity recognition
- ANN, simple RNN, and LSTM/GRU examples
- LangChain components, data ingestion, text splitting, embeddings, and vector stores
- Gemma and Ollama, LCEL, conversation history, chatbots, and agents
- RAG with Groq/Llama, Astra DB, and LangGraph
- Text summarization, website/YouTube summarization, and a math problem solver
- NVIDIA NIM and model fine-tuning examples

Some course numbers are intentionally absent in the original material. The linked folder is the source of truth for the lessons currently included.

### 3. [Complete Generative AI Mastery](./Complete%20Generative%20AI%20Mastery/)

Explores data preprocessing and vectorization before moving into embeddings, text classification, Hugging Face tasks, tokenization, and fine-tuning. Later folders include:

- Text summarization, image generation, text-to-speech, and audio transcription
- Vector databases and LangChain
- An exam question-and-answer generator
- Llama 2 and Falcon examples
- RAG and LlamaIndex
- Financial stock analysis and medical chatbot projects

### 4. [Complete Agentic AI with LangChain and LangGraph](./Complete-Agentic-AI-With-LangChain-and-LangGraph/)

Covers Python prerequisites and Pydantic, then progresses through LangChain and agent concepts into graph-based applications:

- Basic LLM applications with LCEL
- Agents with conversation history
- LangGraph fundamentals, components, and workflows
- Debugging with LangSmith
- Human-in-the-loop patterns
- RAG with LangGraph

### 5. [Complete Generative AI: Basic to Advanced](./Complete-Generative-AI-with-Basic-to-Advanced/)

An indexed sequence of 23 modules, starting with data preprocessing and vectorization and extending through modern LLM application patterns:

1. Data preprocessing and cleaning
2. Data representation and vectorization
3. How ChatGPT is trained and an introduction to Hugging Face
4. Tokenization and fine-tuning with Hugging Face
5. Text summarization with Hugging Face
6. Text-to-image and speech generation
7. Vector database practicals
8–13. LangChain, LCEL, memory, and the LangChain ecosystem
14. LlamaIndex
15–18. Open-source LLMs, website chatbots, and fine-tuning
19. Medical chatbot project
20. Multimodal RAG development
21. AI agents with Agno
22. AI agents with LangGraph
23. MCP agent with MCP-USE

### 6. [Complete LangChain from CampusX](./Complete-LangChain-From-CampusX/)

Focused examples for LangChain building blocks, in lesson order:

1. Models
2. Prompts
3. Structured output
4. Output parsers
5. Chains
6–7. Runnables
8. Document loaders
9. Text splitters
10. Vector stores
11. Retrievers
12. RAG system
13. Tools
14. Tool calling
15. Agents

The collection includes Python scripts and notebooks. A shared `requirements.txt` is provided in this folder; individual lessons may still need provider credentials or additional local setup.

### 7. [Complete LangGraph from CampusX](./Complete-LangGraph-From-CampusX/)

Practical LangGraph examples illustrating graph control flow, persistence, and interactive applications:

- Sequential, parallel, and conditional workflows
- Chatbot construction and persistence
- Streamlit chat UI and token streaming
- Multi-thread conversations and database persistence
- Tool-calling agents and MCP clients
- RAG with LangGraph
- Human-in-the-loop interaction
- Hallucination-related examples

## Technology overview

The badges above highlight the major tools visible across the course material. Depending on the lesson, you may also encounter:

- **Languages and formats:** Python, SQL, Jupyter notebooks
- **LLM frameworks:** LangChain, LangGraph, LlamaIndex, Agno, MCP-USE
- **Models and providers:** Google Gemini, Hugging Face models, Groq, Ollama, OpenAI, Llama, Gemma, Mistral, and others
- **ML and NLP:** NumPy, pandas, scikit-learn, TensorFlow/Keras, NLTK, and Transformers
- **Apps and interfaces:** Streamlit, Flask, Chainlit
- **Retrieval and storage:** Chroma, FAISS, Astra DB, SQLite, and other vector database examples

This is a summary of technologies represented in the lessons, not a promise that every package is installed or configured at the repository root.

## Getting started

### Prerequisites

- Python 3.8 or later for many examples; check the target lesson for its exact version requirements.
- Git, if you want to clone the repository.
- JupyterLab or Jupyter Notebook for `.ipynb` lessons.
- API credentials or a local model runtime only when the selected lesson requires them.

### Clone the repository

```bash
git clone https://github.com/Md-Emon-Hasan/Generative-AI-All-Course-Combined.git
cd Generative-AI-All-Course-Combined
```

### Open a lesson

Choose a course folder and then open a notebook or app within the relevant lesson directory. For example, to work with the shared LangChain course dependencies:

```bash
cd Complete-LangChain-From-CampusX
python -m venv .venv
```

Activate the environment and install that course's shared requirements:

```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

For other courses, inspect the selected app's imports and any lesson-specific `requirements.txt` before installing packages. There is no root-level requirements file because the collections use different dependency sets and model providers. Avoid installing every course's dependencies into one environment.

To run a notebook, launch Jupyter from the relevant course folder:

```bash
python -m pip install jupyterlab
jupyter lab
```

For a Streamlit app, run the app's own script from its directory:

```bash
streamlit run app.py
```

Use the actual script name in the lesson if it is not `app.py`.

## API keys and environment variables

Some examples use hosted services such as Google Gemini, Groq, OpenAI, Hugging Face, or other providers. Create credentials with the provider you choose, then follow the variable names expected by that specific lesson. Where an app uses `python-dotenv`, place secrets in a local `.env` file in the working directory, for example:

```dotenv
GOOGLE_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
```

These are examples only; not every project uses these exact names. Never commit real API keys, tokens, or private data. Many examples can also require a local model runtime, downloads, database files, or external data.

## Working with notebooks

- Run notebooks from their own lesson directory when they read local files using relative paths.
- Review the imports and setup cells before executing a notebook.
- Model downloads and API calls may require internet access, credentials, or substantial memory/compute.
- Notebook outputs may contain generated data or environment-specific paths; rerun cells in your own environment when needed.
- Treat included datasets and model artifacts according to their original licenses and usage terms.

## Repository layout

```text
.
├── 12-Plus-Generative-AI-App-with-Gemini-Pro/
├── Complete Generative AI Course With Langchain and Huggingface/
├── Complete Generative AI Mastery/
├── Complete-Agentic-AI-With-LangChain-and-LangGraph/
├── Complete-Generative-AI-with-Basic-to-Advanced/
├── Complete-LangChain-From-CampusX/
├── Complete-LangGraph-From-CampusX/
├── banner.png
├── LICENSE
└── README.md
```

Course folders contain their own numbered lesson directories and may include notebooks, Python source files, screenshots, datasets, and sample databases.

## Contributing

Contributions that make the learning material clearer and easier to reproduce are welcome. Before opening a pull request:

1. Keep changes scoped to the relevant course or lesson.
2. Include clear setup notes when adding dependencies, credentials, or data files.
3. Do not commit secrets, virtual environments, caches, or large generated artifacts.
4. Update the relevant course README when lesson instructions change.
5. Describe what changed and which lesson or workflow you checked.

## License

This repository includes a [LICENSE](./LICENSE). Course materials, datasets, model weights, and third-party assets may have additional terms; check their original sources before reuse or redistribution.

## Connect with me

- **Portfolio:** [emonlabs-ai.hitechparks.com](https://emonlabs-ai.hitechparks.com)
- **GitHub:** [Md-Emon-Hasan](https://github.com/Md-Emon-Hasan)
- **LinkedIn:** [Md Emon Hasan](https://www.linkedin.com/in/md-emon-hasan-695483237/)
- **Hugging Face:** [emonHasan01](https://huggingface.co/emonHasan01)
- **Email:** [emon.mlengineer@gmail.com](mailto:emon.mlengineer@gmail.com)
- **WhatsApp:** [+8801834363533](https://wa.me/8801834363533)

---

Made by [Md Emon Hasan](https://github.com/Md-Emon-Hasan).
