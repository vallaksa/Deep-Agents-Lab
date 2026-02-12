# Deep-Agents-Lab

A lab for learning [DeepAgents](https://github.com/deepagents/deepagents) — building AI agents with custom tools and web search.

## Setup

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
```

Create a `.env` file with:

- `OPENAI_API_KEY` — for GPT models
- `TAVILY_API_KEY` — for the search agent (02_search_agent.py)

## Project Structure

| File | Description |
|------|-------------|
| `01_basic_agent.py` | Basic agent with custom tools: INR→USD, even/odd, trip cost |
| `02_search_agent.py` | Web search agent powered by Tavily |
| `03_middleware.py` | Agent with custom tool-call middleware (logging, call limits) |

## Usage

**Basic agent** (custom tools):

```bash
python 01_basic_agent.py
```

**Search agent** (web search via Tavily):

```bash
python 02_search_agent.py
```

**Middleware agent** (tool-call middleware with `wrap_tool_call`):

```bash
python 03_middleware.py
```
