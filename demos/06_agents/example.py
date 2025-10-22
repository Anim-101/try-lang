"""
Demo 6: Agents and Tools

This script demonstrates how to build agents that can use tools
to autonomously solve problems.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain.tools import tool
from langchain import hub
from datetime import datetime
import json

# Load environment variables
load_dotenv()


def example_simple_tools():
    """Demonstrates creating simple custom tools"""
    
    print("💬 Example 1: Creating Simple Tools")
    print("-" * 50)
    
    # Method 1: Using the @tool decorator
    @tool
    def get_current_time() -> str:
        """Returns the current time. Use this when you need to know what time it is."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @tool
    def calculate_square(number: int) -> int:
        """Calculates the square of a number. Use this when you need to square a number."""
        return number ** 2
    
    @tool
    def reverse_string(text: str) -> str:
        """Reverses a string. Use this when you need to reverse text."""
        return text[::-1]
    
    # Test the tools
    print("Tool 1: Get Current Time")
    print(f"  Name: {get_current_time.name}")
    print(f"  Description: {get_current_time.description}")
    print(f"  Result: {get_current_time.invoke({})}")
    print()
    
    print("Tool 2: Calculate Square")
    print(f"  Name: {calculate_square.name}")
    print(f"  Description: {calculate_square.description}")
    print(f"  Result: {calculate_square.invoke({'number': 7})}")
    print()
    
    print("Tool 3: Reverse String")
    print(f"  Name: {reverse_string.name}")
    print(f"  Description: {reverse_string.description}")
    print(f"  Result: {reverse_string.invoke({'text': 'Hello'})}")
    print()


def example_tool_with_logic():
    """Demonstrates tools with complex logic"""
    
    print("💬 Example 2: Tools with Complex Logic")
    print("-" * 50)
    
    @tool
    def analyze_text(text: str) -> str:
        """Analyzes text and returns statistics. Use this to get text analysis."""
        word_count = len(text.split())
        char_count = len(text)
        sentence_count = text.count('.') + text.count('!') + text.count('?')
        
        analysis = {
            "word_count": word_count,
            "character_count": char_count,
            "sentence_count": sentence_count,
            "average_word_length": round(char_count / word_count if word_count > 0 else 0, 2)
        }
        
        return json.dumps(analysis, indent=2)
    
    @tool
    def temperature_converter(temperature: float, from_unit: str, to_unit: str) -> str:
        """Converts temperature between Celsius and Fahrenheit. 
        Args:
            temperature: The temperature value
            from_unit: 'C' or 'F'
            to_unit: 'C' or 'F'
        """
        if from_unit == 'C' and to_unit == 'F':
            result = (temperature * 9/5) + 32
            return f"{temperature}°C = {result}°F"
        elif from_unit == 'F' and to_unit == 'C':
            result = (temperature - 32) * 5/9
            return f"{temperature}°F = {result}°C"
        else:
            return "Please use 'C' or 'F' for units"
    
    # Test the tools
    sample_text = "LangChain is amazing. It makes building AI apps easy!"
    print(f"Analyzing: '{sample_text}'")
    print(analyze_text.invoke({"text": sample_text}))
    print()
    
    print("Converting 100°F to Celsius:")
    print(temperature_converter.invoke({
        "temperature": 100,
        "from_unit": "F",
        "to_unit": "C"
    }))
    print()


def example_basic_agent():
    """Demonstrates a basic agent with tools"""
    
    print("💬 Example 3: Basic Agent with Tools")
    print("-" * 50)
    
    # Create tools
    @tool
    def get_word_count(text: str) -> int:
        """Returns the number of words in the text."""
        return len(text.split())
    
    @tool
    def make_uppercase(text: str) -> str:
        """Converts text to uppercase."""
        return text.upper()
    
    @tool
    def count_vowels(text: str) -> int:
        """Counts the number of vowels in the text."""
        vowels = 'aeiouAEIOU'
        return sum(1 for char in text if char in vowels)
    
    # Create LLM
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    
    # Create list of tools
    tools = [get_word_count, make_uppercase, count_vowels]
    
    # Get the ReAct prompt template
    prompt = hub.pull("hwchase17/react")
    
    # Create agent
    agent = create_react_agent(llm, tools, prompt)
    
    # Create agent executor
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,  # Show agent reasoning
        handle_parsing_errors=True
    )
    
    # Run the agent
    print("Task: Count the vowels in 'Hello World' and tell me the count\n")
    
    result = agent_executor.invoke({
        "input": "Count the vowels in 'Hello World' and tell me the count"
    })
    
    print(f"\nFinal Answer: {result['output']}")
    print()


def example_agent_reasoning():
    """Demonstrates agent multi-step reasoning"""
    
    print("💬 Example 4: Agent Multi-Step Reasoning")
    print("-" * 50)
    
    # Create calculator tools
    @tool
    def add(a: float, b: float) -> float:
        """Adds two numbers together."""
        return a + b
    
    @tool
    def multiply(a: float, b: float) -> float:
        """Multiplies two numbers."""
        return a * b
    
    @tool
    def divide(a: float, b: float) -> float:
        """Divides first number by second number."""
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
    
    # Create LLM
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    
    # Create tools list
    tools = [add, multiply, divide]
    
    # Get prompt
    prompt = hub.pull("hwchase17/react")
    
    # Create and execute agent
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True
    )
    
    # Complex math problem
    print("Task: Calculate (10 + 5) * 3 / 5\n")
    
    result = agent_executor.invoke({
        "input": "Calculate the result of (10 + 5) * 3 / 5. Break it down step by step."
    })
    
    print(f"\nFinal Answer: {result['output']}")
    print()


def example_information_lookup_agent():
    """Demonstrates agent that looks up information"""
    
    print("💬 Example 5: Information Lookup Agent")
    print("-" * 50)
    
    # Create a knowledge base (in real app, this could be a database)
    knowledge_base = {
        "langchain": "LangChain is a framework for developing applications powered by language models",
        "python": "Python is a high-level programming language known for its simplicity",
        "ai": "Artificial Intelligence is the simulation of human intelligence by machines",
        "embeddings": "Embeddings are vector representations of text that capture semantic meaning"
    }
    
    @tool
    def lookup_information(topic: str) -> str:
        """Looks up information about a topic in the knowledge base."""
        topic_lower = topic.lower()
        if topic_lower in knowledge_base:
            return knowledge_base[topic_lower]
        return f"No information found about '{topic}'"
    
    @tool
    def list_available_topics() -> str:
        """Lists all available topics in the knowledge base."""
        return ", ".join(knowledge_base.keys())
    
    # Create LLM and agent
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    tools = [lookup_information, list_available_topics]
    prompt = hub.pull("hwchase17/react")
    
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True
    )
    
    # Ask the agent
    print("Task: What is LangChain?\n")
    
    result = agent_executor.invoke({
        "input": "What is LangChain? Use the lookup tool to find information."
    })
    
    print(f"\nFinal Answer: {result['output']}")
    print()


def example_conditional_tool_use():
    """Demonstrates agent choosing between tools conditionally"""
    
    print("💬 Example 6: Conditional Tool Selection")
    print("-" * 50)
    
    @tool
    def check_if_prime(number: int) -> str:
        """Checks if a number is prime."""
        if number < 2:
            return f"{number} is not prime"
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return f"{number} is not prime (divisible by {i})"
        return f"{number} is prime"
    
    @tool
    def check_if_even(number: int) -> str:
        """Checks if a number is even or odd."""
        return f"{number} is {'even' if number % 2 == 0 else 'odd'}"
    
    @tool
    def get_factors(number: int) -> str:
        """Gets all factors of a number."""
        factors = [i for i in range(1, number + 1) if number % i == 0]
        return f"Factors of {number}: {factors}"
    
    # Create agent
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    tools = [check_if_prime, check_if_even, get_factors]
    prompt = hub.pull("hwchase17/react")
    
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True
    )
    
    # Ask the agent
    print("Task: Analyze the number 17\n")
    
    result = agent_executor.invoke({
        "input": "Tell me everything about the number 17: is it prime? Is it even or odd? What are its factors?"
    })
    
    print(f"\nFinal Answer: {result['output']}")
    print()


def main():
    """Run all agent examples"""
    
    print("=" * 50)
    print("Demo 6: Agents and Tools")
    print("=" * 50)
    print()
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found")
        return
    
    # Run all examples
    print("⚠️  Note: Some examples show verbose output to demonstrate agent reasoning\n")
    
    example_simple_tools()
    example_tool_with_logic()
    example_basic_agent()
    example_agent_reasoning()
    example_information_lookup_agent()
    example_conditional_tool_use()
    
    print("=" * 50)
    print("✨ Demo Complete!")
    print("=" * 50)
    print()
    print("💡 Key Learnings:")
    print("   1. Tools extend agent capabilities")
    print("   2. Agents autonomously choose which tools to use")
    print("   3. ReAct pattern combines reasoning and action")
    print("   4. Agents can solve multi-step problems")
    print("   5. Tools should have clear descriptions")
    print("   6. Verbose mode helps understand agent thinking")
    print()
    print("🎉 Congratulations! You've completed all LangChain demos!")
    print()
    print("📚 Next Steps:")
    print("   - Build your own LangChain project")
    print("   - Combine concepts from multiple demos")
    print("   - Explore advanced features in LangChain docs")
    print("   - Share your learning experience!")
    print()


if __name__ == "__main__":
    main()
