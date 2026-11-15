# MCP Browser Agent

An interactive command-line chat example that connects a Groq chat model to MCP tools. The included `browser_mcp.json` configures Airbnb, Playwright, and DuckDuckGo MCP servers. The agent keeps conversation memory during the session.

## Requirements

- Python 3.11 or newer
- Node.js and `npx` for the configured MCP servers
- A Groq API key
- Network access to download and start the MCP servers

## Setup

Run commands from this directory:

```bash
python -m venv .venv
```

Activate the environment and install the Python dependencies:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Set `GROQ_API_KEY` in your shell or create a local `.env` file in this directory:

```dotenv
GROQ_API_KEY=your_groq_api_key
```

Review `browser_mcp.json` and install/configure the MCP servers you intend to use. The config is passed to MCP Use at runtime; server availability depends on Node.js, network access, and the packages named in the config.

## Run

```bash
python main.py
```

Enter a prompt in the terminal. Type `clear` to reset the conversation history, or `exit` / `quit` to close the session.

## Files

- `main.py` — interactive MCP agent.
- `browser_mcp.json` — MCP server definitions.
- `requirements.txt` — Python dependencies.
- `pyproject.toml` — project metadata and Python version requirement.

Only connect MCP servers and tools you trust. Do not commit API keys or other secrets.
