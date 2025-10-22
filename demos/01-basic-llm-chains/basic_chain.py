"""
Demo 1: Basic LLM Chain
This demo shows how to create a simple LLM chain using LangChain.
"""

from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def main():
    """Run basic LLM chain demo"""
    # Initialize the LLM
    llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")
    
    # Create a simple prompt template
    prompt = PromptTemplate(
        input_variables=["topic"],
        template="Tell me a short fact about {topic}."
    )
    
    # Create the chain
    chain = LLMChain(llm=llm, prompt=prompt)
    
    # Run the chain
    result = chain.run(topic="Python programming")
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
