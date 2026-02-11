import os
from deepagents import create_deep_agent
from tavily import TavilyClient
from dotenv import load_dotenv
load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


agent = create_deep_agent (
    name="search_agent",
    model="gpt-4o-mini",
    tools=[tavily_client.search],
)

system_prompt = """
You are a helpful assistant that can search the web for information.
You can use the TavilyClient tool to search the web.
You are also a helpful assistant that can answer questions.
You can use the tools to answer questions.
You can also use the tools to search the web for information.
Gaurdrail: You are not allowed to use the tools to search the web for information that is not related to the user's question.
Gaurdrail: Response shouldbe concise and to the point.
gaurdrail: dont generate morethan 100 words.
"""

result = agent.invoke({
    "messages":[{
    "role": "user", 
    "content": "What is the capital of France? and Latest news about Virat Kohli"
    }],
    "system_prompt": system_prompt
    })
print(result["messages"][-1].content)