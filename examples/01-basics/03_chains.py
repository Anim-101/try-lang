"""
03_chains.py
Understanding Chains - Connecting prompts and LLMs in sequences
"""

import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

def simple_chain():
    """
    Create a simple chain with prompt + LLM + output parser
    """
    print("🔗 Simple Chain Example")
    print("=" * 30)
    
    # Components of the chain
    prompt = PromptTemplate.from_template(
        "Write a short {adjective} story about {subject} in exactly {word_count} words."
    )
    
    llm = OpenAI(temperature=0.8)
    output_parser = StrOutputParser()
    
    # Create the chain using LCEL (LangChain Expression Language)
    chain = prompt | llm | output_parser
    
    # Use the chain
    result = chain.invoke({
        "adjective": "mysterious",
        "subject": "a lost cat",
        "word_count": "50"
    })
    
    print("📖 Generated Story:")
    print(result)
    return chain

def sequential_chain():
    """
    Create a chain where output of one step feeds into the next
    """
    print("\n🔗 Sequential Chain Example")
    print("=" * 35)
    
    # Step 1: Generate a topic
    topic_prompt = PromptTemplate.from_template(
        "Generate a random {category} topic for a beginner tutorial:"
    )
    
    # Step 2: Create tutorial outline
    outline_prompt = PromptTemplate.from_template(
        "Create a simple 3-point outline for a tutorial on: {topic}"
    )
    
    # Step 3: Write introduction
    intro_prompt = PromptTemplate.from_template(
        "Write a brief introduction paragraph for a tutorial with this outline:\n{outline}"
    )
    
    llm = OpenAI(temperature=0.7)
    
    # Create individual chains
    topic_chain = topic_prompt | llm | StrOutputParser()
    outline_chain = outline_prompt | llm | StrOutputParser()
    intro_chain = intro_prompt | llm | StrOutputParser()
    
    return topic_chain, outline_chain, intro_chain

def main():
    """
    Demonstrate different types of chains
    """
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Please set your OPENAI_API_KEY in .env file")
        return
    
    try:
        # 1. Simple chain
        simple_chain()
        
        # 2. Sequential chain
        topic_chain, outline_chain, intro_chain = sequential_chain()
        
        # Execute the sequential chain step by step
        print("Step 1: Generating topic...")
        topic = topic_chain.invoke({"category": "programming"})
        print(f"📋 Topic: {topic.strip()}")
        
        print("\nStep 2: Creating outline...")
        outline = outline_chain.invoke({"topic": topic})
        print(f"📝 Outline:\n{outline}")
        
        print("\nStep 3: Writing introduction...")
        introduction = intro_chain.invoke({"outline": outline})
        print(f"✍️ Introduction:\n{introduction}")
        
        # Alternative: Chain them together in one go
        print("\n🔗 Combined Chain Example")
        print("=" * 30)
        
        # Recreate prompts for the combined chain
        topic_prompt_combined = PromptTemplate.from_template(
            "Generate a random {category} topic for a beginner tutorial:"
        )
        outline_prompt_combined = PromptTemplate.from_template(
            "Create a simple 3-point outline for a tutorial on: {topic}"
        )
        
        # Create a mega-chain that does all steps
        combined_chain = (
            topic_prompt_combined 
            | OpenAI(temperature=0.7) 
            | StrOutputParser() 
            | (lambda topic: {"topic": topic}) 
            | outline_prompt_combined 
            | OpenAI(temperature=0.7) 
            | StrOutputParser()
        )
        
        result = combined_chain.invoke({"category": "data science"})
        print(f"🎯 Combined Result:\n{result}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()