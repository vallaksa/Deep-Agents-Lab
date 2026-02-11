from deepagents import create_deep_agent
from dotenv import load_dotenv
load_dotenv()

def inr_to_usd(amount: float) -> float:
    ''' Convert INR to USD '''
    return round(amount / 91.5, 2)

def even_odd(number: int) -> str:
    '''Check if a given number is even or odd'''
    return "even" if number % 2 == 0 else "odd"
    
def trip_cost(distance: float) -> float:
    '''Calculate the cost of a trip'''
    return round(distance * 5, 2)

agent = create_deep_agent(
    name="basic_agent",
    model="gpt-4o-mini",
    tools=[inr_to_usd, even_odd, trip_cost],
)

result = agent.invoke({
    "messages": 
    [{
            "role": "user", 
            "content": "Convert 1000 INR to USD"
        },
        {
            "role": "assistant",
            "content": "is number 10 even or odd?"
        },
        {
            "role": "user",
            "content": "is number 11 even or odd?"
        },
        {
            "role": "assistant",
            "content": "11 is odd"
        },
        {
            "role": "user",
            "content": "How much will it cost to travel 100 km?"
        },
        ]
    })
print(result["messages"][-1].content)