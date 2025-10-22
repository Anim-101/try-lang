"""
Demo 6: Custom Tools
This demo shows how to create more advanced custom tools for agents.
"""

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, Tool
from langchain.tools import tool
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()


@tool
def word_counter(text: str) -> str:
    """Counts words in a given text. Input should be a string."""
    words = text.split()
    return f"Word count: {len(words)}"


@tool
def json_parser(json_string: str) -> str:
    """Parses a JSON string and returns formatted output. Input should be a JSON string."""
    try:
        data = json.loads(json_string)
        return f"Parsed JSON: {json.dumps(data, indent=2)}"
    except json.JSONDecodeError:
        return "Invalid JSON format"


@tool
def text_analyzer(text: str) -> str:
    """Analyzes text and returns statistics. Input should be a string."""
    words = text.split()
    chars = len(text)
    sentences = text.count('.') + text.count('!') + text.count('?')
    
    stats = {
        "characters": chars,
        "words": len(words),
        "sentences": max(sentences, 1),
        "avg_word_length": round(chars / max(len(words), 1), 2)
    }
    
    return json.dumps(stats, indent=2)


class CustomCalculator:
    """Custom calculator tool as a class"""
    
    @staticmethod
    def calculate(expression: str) -> str:
        """Evaluates a mathematical expression. Input should be a valid Python expression."""
        try:
            # Note: eval is used here for demo purposes only
            # In production, use a safe math parser
            result = eval(expression, {"__builtins__": {}}, {})
            return f"Result: {result}"
        except Exception as e:
            return f"Error: {str(e)}"


def custom_tools_demo():
    """Demo using custom tools with an agent"""
    print("=== Custom Tools Demo ===\n")
    
    # Initialize the LLM
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    
    # Create tools list
    tools = [
        word_counter,
        json_parser,
        text_analyzer,
        Tool(
            name="Calculator",
            func=CustomCalculator.calculate,
            description="Evaluates mathematical expressions like '2 + 2' or '10 * 5'"
        )
    ]
    
    # Initialize the agent
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    
    # Test queries
    queries = [
        "How many words are in 'LangChain is an amazing framework for building AI applications'?",
        "Analyze the text 'Python is great. It is easy to learn. Many people use it.'",
        "Calculate 25 * 4 + 10"
    ]
    
    for i, query in enumerate(queries, 1):
        print(f"\nQuery {i}: {query}")
        print("-" * 70)
        result = agent.run(query)
        print(f"Result: {result}\n")
        print("=" * 70 + "\n")


def main():
    """Run custom tools demo"""
    custom_tools_demo()


if __name__ == "__main__":
    main()
