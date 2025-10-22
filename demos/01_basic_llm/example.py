"""
Demo 1: Basic LLM Interaction with LangChain

This script demonstrates the fundamentals of using LangChain with OpenAI.
You'll learn how to initialize an LLM and make basic completions.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

def main():
    """
    Main function demonstrating basic LLM usage
    """
    
    print("=" * 50)
    print("Demo 1: Basic LLM Interaction")
    print("=" * 50)
    print()
    
    # Step 1: Initialize the LLM
    # The ChatOpenAI class connects to OpenAI's chat models
    print("📡 Initializing connection to OpenAI...")
    
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",  # The model to use
        temperature=0.7,         # Controls randomness (0-1)
        max_tokens=150,          # Maximum length of response
        api_key=os.getenv("OPENAI_API_KEY")  # Your API key
    )
    
    print("✅ Connection established!")
    print()
    
    # Step 2: Make a simple completion
    print("💬 Example 1: Simple Question")
    print("-" * 50)
    
    prompt1 = "What is LangChain and why is it useful?"
    print(f"Prompt: {prompt1}")
    print()
    
    # Invoke the LLM with a prompt
    response1 = llm.invoke(prompt1)
    print(f"Response: {response1.content}")
    print()
    
    # Step 3: Try with different temperature
    print("💬 Example 2: Creative Response (Higher Temperature)")
    print("-" * 50)
    
    creative_llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.9,  # Higher temperature = more creative/random
        max_tokens=100
    )
    
    prompt2 = "Write a creative haiku about programming"
    print(f"Prompt: {prompt2}")
    print()
    
    response2 = creative_llm.invoke(prompt2)
    print(f"Response: {response2.content}")
    print()
    
    # Step 4: Try with lower temperature (more deterministic)
    print("💬 Example 3: Deterministic Response (Lower Temperature)")
    print("-" * 50)
    
    deterministic_llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.0,  # Lower temperature = more focused/deterministic
        max_tokens=100
    )
    
    prompt3 = "What is 2 + 2?"
    print(f"Prompt: {prompt3}")
    print()
    
    response3 = deterministic_llm.invoke(prompt3)
    print(f"Response: {response3.content}")
    print()
    
    # Step 5: Understanding the response object
    print("🔍 Understanding the Response Object")
    print("-" * 50)
    
    response = llm.invoke("Say hello!")
    print(f"Response content: {response.content}")
    print(f"Response type: {type(response)}")
    print(f"Response metadata: {response.response_metadata}")
    print()
    
    print("=" * 50)
    print("✨ Demo Complete!")
    print("=" * 50)
    print()
    print("💡 Next Steps:")
    print("   1. Try changing the temperature values")
    print("   2. Experiment with different prompts")
    print("   3. Try different models (if you have access)")
    print("   4. Move on to Demo 2: Prompt Templates")
    print()


if __name__ == "__main__":
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in environment variables")
        print("Please create a .env file and add your OpenAI API key")
        print("Example: OPENAI_API_KEY=sk-...")
    else:
        main()
