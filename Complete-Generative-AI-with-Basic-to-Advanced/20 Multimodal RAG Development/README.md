# Multimodal RAG

This lesson explores retrieval-augmented generation over documents that contain more than plain text. The notebook demonstrates working with text, tables, and images from a financial report, with figures in `figures/` for reference.

## Requirements

- Python 3.11 is the environment used in the original setup instructions.
- Jupyter Notebook or JupyterLab.
- API credentials for the model services used in the notebook. Review its setup cells before execution.
- System dependencies may be needed for PDF parsing and OCR (including Tesseract for OCR examples).

## Set up an environment

From this directory:

```bash
python -m venv .venv
```

Activate the environment, then install the project requirements:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install jupyter ipykernel
```

Open the notebook:

```bash
jupyter lab multimodal_rag.ipynb
```

Add any additional package required by a notebook cell to this environment. Keep provider API keys in environment variables or a local, untracked `.env` file; consult the notebook for the exact names.

## Included files

- `multimodal_rag.ipynb` — the lesson notebook.
- `startupai-financial-report-v2.pdf` — sample document used by the example.
- `figures/` — document figures used for reference.
- `requirements.txt` — project-level Python dependencies.
- `requirements-dev.txt` — an exported development environment that contains machine-local `file://` package URLs. It is not portable and should not be installed on another computer.

The notebook uses external model APIs and may incur provider charges. Treat its output as an educational example and verify current model access and SDK requirements with the provider.
