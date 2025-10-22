"""
Demo 3: Chains and Sequential Operations

This script demonstrates how to chain multiple LLM operations together
to create more complex workflows.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough

# Load environment variables
load_dotenv()


def example_basic_lcel_chain():
    """Demonstrates basic LCEL chain using | operator"""
    
    print("💬 Example 1: Basic LCEL Chain")
    print("-" * 50)
    
    # Create a prompt template
    prompt = ChatPromptTemplate.from_template(
        "Tell me a {adjective} joke about {topic}"
    )
    
    # Create LLM
    llm = ChatOpenAI(temperature=0.9)
    
    # Create output parser
    output_parser = StrOutputParser()
    
    # Chain them together using LCEL (|) operator
    # This is the modern LangChain way
    chain = prompt | llm | output_parser
    
    print("Chain structure: prompt | llm | output_parser")
    print()
    
    # Invoke the chain
    result = chain.invoke({
        "adjective": "funny",
        "topic": "programming"
    })
    
    print(f"Input: adjective='funny', topic='programming'")
    print(f"Output: {result}")
    print()


def example_sequential_chain():
    """Demonstrates sequential operations in a chain"""
    
    print("💬 Example 2: Sequential Chain")
    print("-" * 50)
    
    # Step 1: Generate a topic
    topic_prompt = ChatPromptTemplate.from_template(
        "Suggest a random {category} topic. Only respond with the topic, nothing else."
    )
    
    # Step 2: Write about that topic
    writing_prompt = ChatPromptTemplate.from_template(
        "Write a brief 2-sentence explanation about: {topic}"
    )
    
    llm = ChatOpenAI(temperature=0.7)
    output_parser = StrOutputParser()
    
    # Create first chain to get topic
    topic_chain = topic_prompt | llm | output_parser
    
    # Get a topic
    topic = topic_chain.invoke({"category": "technology"})
    print(f"Generated Topic: {topic}")
    print()
    
    # Create second chain to write about it
    writing_chain = writing_prompt | llm | output_parser
    
    # Write about the topic
    explanation = writing_chain.invoke({"topic": topic})
    print(f"Explanation: {explanation}")
    print()


def example_chain_with_multiple_inputs():
    """Demonstrates chain with multiple input transformations"""
    
    print("💬 Example 3: Chain with Multiple Inputs")
    print("-" * 50)
    
    # Create a chain that processes multiple inputs
    prompt = ChatPromptTemplate.from_template(
        """Given the following information:
        
        Name: {name}
        Role: {role}
        Company: {company}
        
        Write a professional introduction for this person."""
    )
    
    llm = ChatOpenAI(temperature=0.7)
    output_parser = StrOutputParser()
    
    chain = prompt | llm | output_parser
    
    # Invoke with multiple inputs
    result = chain.invoke({
        "name": "Sarah Chen",
        "role": "Senior Software Engineer",
        "company": "TechCorp"
    })
    
    print(f"Professional Introduction:\n{result}")
    print()


def example_chain_with_passthrough():
    """Demonstrates using RunnablePassthrough to preserve inputs"""
    
    print("💬 Example 4: Chain with Passthrough")
    print("-" * 50)
    
    # Create a summary chain
    summary_prompt = ChatPromptTemplate.from_template(
        "Summarize this in one sentence: {text}"
    )
    
    llm = ChatOpenAI(temperature=0.3)
    
    # Chain that preserves original input and adds summary
    chain = (
        RunnablePassthrough.assign(
            summary=(summary_prompt | llm | StrOutputParser())
        )
    )
    
    input_text = "LangChain is a framework for developing applications powered by language models. It provides tools for prompt management, chains, agents, and more."
    
    result = chain.invoke({"text": input_text})
    
    print(f"Original Text: {result['text']}")
    print()
    print(f"Summary: {result['summary']}")
    print()


def example_translation_chain():
    """Demonstrates a practical translation chain"""
    
    print("💬 Example 5: Translation Chain")
    print("-" * 50)
    
    # Create prompts for each step
    detect_prompt = ChatPromptTemplate.from_template(
        "What language is this text in? Only respond with the language name: {text}"
    )
    
    translate_prompt = ChatPromptTemplate.from_template(
        "Translate the following {source_language} text to {target_language}:\n\n{text}"
    )
    
    llm = ChatOpenAI(temperature=0.3)
    output_parser = StrOutputParser()
    
    # First chain: detect language
    detect_chain = detect_prompt | llm | output_parser
    
    text = "Bonjour, comment allez-vous?"
    
    # Detect language
    source_lang = detect_chain.invoke({"text": text})
    print(f"Original Text: {text}")
    print(f"Detected Language: {source_lang}")
    print()
    
    # Second chain: translate
    translate_chain = translate_prompt | llm | output_parser
    
    translation = translate_chain.invoke({
        "source_language": source_lang,
        "target_language": "English",
        "text": text
    })
    
    print(f"Translation: {translation}")
    print()


def example_analysis_chain():
    """Demonstrates a multi-step analysis chain"""
    
    print("💬 Example 6: Multi-Step Analysis Chain")
    print("-" * 50)
    
    llm = ChatOpenAI(temperature=0.5)
    
    # Step 1: Extract key points
    extract_prompt = ChatPromptTemplate.from_template(
        "Extract 3 key points from this text: {text}"
    )
    
    # Step 2: Rate sentiment
    sentiment_prompt = ChatPromptTemplate.from_template(
        "Rate the sentiment of these key points as positive, negative, or neutral: {points}"
    )
    
    extract_chain = extract_prompt | llm | StrOutputParser()
    sentiment_chain = sentiment_prompt | llm | StrOutputParser()
    
    text = "The new software update brings exciting features and improvements. However, some users reported minor bugs. Overall, the development team did a great job."
    
    print(f"Original Text: {text}")
    print()
    
    # Extract key points
    key_points = extract_chain.invoke({"text": text})
    print(f"Key Points:\n{key_points}")
    print()
    
    # Analyze sentiment
    sentiment = sentiment_chain.invoke({"points": key_points})
    print(f"Sentiment Analysis:\n{sentiment}")
    print()


def main():
    """Run all chain examples"""
    
    print("=" * 50)
    print("Demo 3: Chains and Sequential Operations")
    print("=" * 50)
    print()
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found")
        return
    
    # Run all examples
    example_basic_lcel_chain()
    example_sequential_chain()
    example_chain_with_multiple_inputs()
    example_chain_with_passthrough()
    example_translation_chain()
    example_analysis_chain()
    
    print("=" * 50)
    print("✨ Demo Complete!")
    print("=" * 50)
    print()
    print("💡 Key Learnings:")
    print("   1. LCEL (|) operator makes chains clean and composable")
    print("   2. Chains can have single or multiple steps")
    print("   3. RunnablePassthrough preserves data through chains")
    print("   4. Chains enable complex workflows")
    print("   5. Each step can transform the data for the next")
    print()
    print("📚 Next: Demo 4 - Memory and Conversations")
    print()


if __name__ == "__main__":
    main()
