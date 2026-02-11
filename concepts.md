# Deep Agents — Concepts Learned

Key takeaways from each lesson. Updated when a lesson is completed.

---

## Lesson 0 — Project Setup ✓

- Virtual environment: `python3 -m venv venv`
- Activate: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
- Dependencies: `deepagents`, `langchain[openai]`, `duckduckgo-search`, `langchain-community`, `python-dotenv`, `pydantic`
- Load API keys from `.env` with `load_dotenv()` and `os.getenv("KEY")`

---

## Lesson 1 — First Agent ✓

- **Tools** = Python functions with type hints + docstring; agent auto-discovers name, description, params
- `create_deep_agent(model=..., tools=[...])` — factory for the agent
- `invoke({"messages": [{"role": "user", "content": "..."}]})` — state must use `"messages"` key, not `"message"`
- Last response: `result["messages"][-1].content` — `AIMessage` uses `.content` attribute, not `["content"]`
- Built-in tools (glob, file system) are available even when you add custom tools

---

## Lesson 2 — Search Agent ✓

- **System prompt** — instructions that steer agent behavior; can be passed to `create_deep_agent()` or `invoke()`
- **Community tools** — e.g. `DuckDuckGoSearchRun`, `TavilyClient`; instantiate and pass as tools
- `load_dotenv()` loads `.env`; it does NOT return a key's value — use `os.getenv("KEY")` after
- Tavily requires `TAVILY_API_KEY`; DuckDuckGo/ddgs are free (install `ddgs` if needed)

---

## Lesson 3 — Middleware

*In progress*

---

## Lesson 4 — Subagents

*Pending*

---

## Lesson 5 — Human-in-the-Loop

*Pending*

---

## Lesson 6 — Structured Output

*Pending*

---

## Lesson 7 — Memory

*Pending*

---

## Lesson 8 — Skills

*Pending*

---

## Lesson 9 — Full Showcase

*Pending*
