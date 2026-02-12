from deepagents import create_deep_agent
from langchain.agents.middleware import wrap_tool_call
from dotenv import load_dotenv
load_dotenv()

counter = 0

def INR_to_USD(amount: float) -> float:
    '''Convert INR to USD'''
    return round(amount/91.5, 2)



@wrap_tool_call
def custom_middleware(request, handler) -> dict:
    global counter
    counter += 1
    print("Custom middleware called before tool call:", request.tool_call["name"], ":", counter)
    result = handler(request)
    print("[Middleware] Result after tool call:", result.content)
    if counter > 3:
        print("You have reached the maximum number of calls")
    else:
        print("tool used", counter)
    return result

agent = create_deep_agent(
    name = "currency_converter",
    model = "gpt-4o-mini",
    tools = [INR_to_USD],
    middleware=[custom_middleware])

result = agent.invoke({"messages": [{"role": "user", "content": "Convert 1000, 2000, 3000, 4000, 5000 and 6000 INR to USD "}]})
