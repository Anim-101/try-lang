"""
Demo 4: Agents
This demo shows how to create and use agents with tools in LangChain.
"""

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, Tool
from langchain.tools import tool
from dotenv import load_dotenv
import datetime

# Load environment variables
load_dotenv()


# Define custom tools
@tool
def get_current_time(query: str) -> str:
    """Returns the current time. Input should be an empty string."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@tool
def calculate_age(birth_year: str) -> str:
    """Calculates age given a birth year. Input should be a year as a string."""
    try:
        year = int(birth_year)
        current_year = datetime.datetime.now().year
        age = current_year - year
        return f"Age: {age} years old"
    except ValueError:
        return "Invalid year format"


@tool
def reverse_string(text: str) -> str:
    """Reverses a given string. Input should be a string."""
    return text[::-1]


def agent_demo():
    """Demo using an agent with custom tools"""
    print("=== Agent with Tools Demo ===\n")
    
    # Initialize the LLM
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    
    # Create tools list
    tools = [
        get_current_time,
        calculate_age,
        reverse_string
    ]
    
    # Initialize the agent
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    
    # Test the agent
    print("Query 1: What time is it?")
    result1 = agent.run("What is the current time?")
    print(f"Result: {result1}\n")
    
    print("\n" + "="*50 + "\n")
    
    print("Query 2: Calculate age")
    result2 = agent.run("If someone was born in 1990, how old are they?")
    print(f"Result: {result2}\n")
    
    print("\n" + "="*50 + "\n")
    
    print("Query 3: Reverse string")
    result3 = agent.run("Can you reverse the string 'LangChain'?")
    print(f"Result: {result3}\n")


def main():
    """Run agent demo"""
    agent_demo()


if __name__ == "__main__":
    main()
