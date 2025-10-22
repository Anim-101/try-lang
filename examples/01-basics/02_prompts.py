"""
02_prompts.py
Working with Prompt Templates - Making prompts dynamic and reusable
"""

import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

def basic_prompt_template():
    """
    Basic prompt template with variables
    """
    print("🎯 Basic Prompt Template Example")
    print("=" * 40)
    
    # Create a prompt template
    template = """
    You are a helpful {role} assistant.
    Please explain {topic} to someone who is a {experience_level}.
    Make your explanation {tone} and {length}.
    
    Topic: {topic}
    """
    
    prompt = PromptTemplate(
        input_variables=["role", "topic", "experience_level", "tone", "length"],
        template=template
    )
    
    # Format the prompt with specific values
    formatted_prompt = prompt.format(
        role="programming",
        topic="Python decorators",
        experience_level="beginner",
        tone="friendly and encouraging",
        length="concise"
    )
    
    print("📝 Formatted Prompt:")
    print(formatted_prompt)
    return formatted_prompt

def few_shot_prompting():
    """
    Few-shot prompting with examples
    """
    print("\n🎯 Few-Shot Prompting Example")
    print("=" * 40)
    
    template = """
    You are a sentiment analyzer. Classify the sentiment as Positive, Negative, or Neutral.
    
    Examples:
    Text: "I love this product!"
    Sentiment: Positive
    
    Text: "This is terrible quality."
    Sentiment: Negative
    
    Text: "The weather is okay today."
    Sentiment: Neutral
    
    Now classify this text:
    Text: "{text}"
    Sentiment:"""
    
    prompt = PromptTemplate(
        input_variables=["text"],
        template=template
    )
    
    return prompt

def main():
    """
    Demonstrate different prompt techniques
    """
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Please set your OPENAI_API_KEY in .env file")
        return
    
    # Initialize LLM
    llm = OpenAI(temperature=0.3)
    
    # 1. Basic prompt template
    formatted_prompt = basic_prompt_template()
    
    try:
        print("\n🤖 LLM Response:")
        response = llm.invoke(formatted_prompt)
        print(response)
        
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # 2. Few-shot prompting
    few_shot_prompt = few_shot_prompting()
    
    # Test with different texts
    test_texts = [
        "This movie was absolutely amazing!",
        "I hate waiting in long lines.",
        "The book was published in 2020."
    ]
    
    print("\n🎯 Few-Shot Classification Results:")
    print("=" * 40)
    
    for text in test_texts:
        try:
            formatted = few_shot_prompt.format(text=text)
            result = llm.invoke(formatted)
            print(f"Text: '{text}'")
            print(f"Result: {result.strip()}")
            print("-" * 20)
            
        except Exception as e:
            print(f"❌ Error processing '{text}': {e}")

if __name__ == "__main__":
    main()