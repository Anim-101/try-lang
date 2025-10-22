"""
01_hello_langchain.py
Your first LangChain program - Basic LLM interaction
"""

import os
from dotenv import load_dotenv
from langchain_openai import OpenAI

# Load environment variables
load_dotenv()

def main():
    """
    Simple example of using LangChain with OpenAI
    """
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Please set your OPENAI_API_KEY in .env file")
        print("Copy .env.example to .env and add your API key")
        return
    
    # Initialize the LLM
    llm = OpenAI(temperature=0.7)
    
    # Simple text generation
    prompt = "Explain what LangChain is in simple terms:"
    
    print("🤖 Asking the LLM:", prompt)
    print("=" * 50)
    
    try:
        # Generate response
        response = llm.invoke(prompt)
        print("📝 Response:")
        print(response)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure your API key is valid and you have credits")

if __name__ == "__main__":
    main()