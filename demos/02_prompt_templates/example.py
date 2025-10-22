"""
Demo 2: Prompt Templates with LangChain

This script demonstrates how to create reusable, dynamic prompts using templates.
Templates help you build maintainable and flexible prompts.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate, FewShotPromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate

# Load environment variables
load_dotenv()


def example_basic_template():
    """Demonstrates basic prompt templates with variables"""
    
    print("💬 Example 1: Basic Prompt Template")
    print("-" * 50)
    
    # Create a template with a variable placeholder
    template = """You are a helpful assistant. 
    
    Please answer the following question: {question}
    
    Provide a concise answer."""
    
    # Create the PromptTemplate
    prompt = PromptTemplate(
        input_variables=["question"],
        template=template
    )
    
    # Format the template with a specific question
    question = "What is Python?"
    formatted_prompt = prompt.format(question=question)
    
    print(f"Template: {template[:50]}...")
    print(f"Question: {question}")
    print(f"Formatted Prompt:\n{formatted_prompt}")
    print()
    
    # Use with LLM
    llm = ChatOpenAI(temperature=0.7)
    response = llm.invoke(formatted_prompt)
    print(f"Response: {response.content}")
    print()


def example_chat_template():
    """Demonstrates chat prompt templates with different message roles"""
    
    print("💬 Example 2: Chat Prompt Template")
    print("-" * 50)
    
    # Create a chat template with system and user messages
    chat_template = ChatPromptTemplate.from_messages([
        ("system", "You are a {role} who speaks in a {style} manner."),
        ("user", "{user_input}")
    ])
    
    # Format the template
    messages = chat_template.format_messages(
        role="pirate captain",
        style="friendly but adventurous",
        user_input="Tell me about your ship"
    )
    
    print("Template Messages:")
    for msg in messages:
        print(f"  {msg.__class__.__name__}: {msg.content}")
    print()
    
    # Use with LLM
    llm = ChatOpenAI(temperature=0.8)
    response = llm.invoke(messages)
    print(f"Response: {response.content}")
    print()


def example_multi_variable_template():
    """Demonstrates templates with multiple variables"""
    
    print("💬 Example 3: Multi-Variable Template")
    print("-" * 50)
    
    # Create a template for generating product descriptions
    template = """Create a {length} product description for:

Product Name: {product_name}
Category: {category}
Key Features: {features}
Target Audience: {audience}

Description:"""
    
    prompt = PromptTemplate(
        input_variables=["length", "product_name", "category", "features", "audience"],
        template=template
    )
    
    # Format with specific product details
    formatted = prompt.format(
        length="short and catchy",
        product_name="CodeMaster Pro",
        category="IDE/Code Editor",
        features="AI autocomplete, syntax highlighting, debugging",
        audience="software developers"
    )
    
    print(f"Formatted Prompt:\n{formatted}")
    print()
    
    llm = ChatOpenAI(temperature=0.7, max_tokens=150)
    response = llm.invoke(formatted)
    print(f"Response: {response.content}")
    print()


def example_few_shot_template():
    """Demonstrates few-shot learning with examples"""
    
    print("💬 Example 4: Few-Shot Template")
    print("-" * 50)
    
    # Examples to guide the model
    examples = [
        {
            "input": "happy",
            "output": "I'm feeling joyful and energetic! 😊"
        },
        {
            "input": "tired",
            "output": "I could really use some rest right now. 😴"
        },
    ]
    
    # Template for each example
    example_template = """
    Emotion: {input}
    Response: {output}
    """
    
    example_prompt = PromptTemplate(
        input_variables=["input", "output"],
        template=example_template
    )
    
    # Create few-shot template
    few_shot_prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        prefix="Given an emotion, respond as if you're feeling that way:\n",
        suffix="\nEmotion: {input}\nResponse:",
        input_variables=["input"]
    )
    
    # Format with new input
    formatted = few_shot_prompt.format(input="excited")
    
    print("Few-Shot Prompt:")
    print(formatted)
    print()
    
    llm = ChatOpenAI(temperature=0.7)
    response = llm.invoke(formatted)
    print(f"Response: {response.content}")
    print()


def example_template_composition():
    """Demonstrates composing templates together"""
    
    print("💬 Example 5: Template Composition")
    print("-" * 50)
    
    # Create multiple templates that work together
    context_template = "Context: {context}"
    question_template = "Question: {question}"
    instruction_template = "Please answer based on the context provided."
    
    full_template = f"""{context_template}

{question_template}

{instruction_template}

Answer:"""
    
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=full_template
    )
    
    formatted = prompt.format(
        context="LangChain is a framework for developing applications powered by language models.",
        question="What is LangChain used for?"
    )
    
    print(f"Composed Template:\n{formatted}")
    print()
    
    llm = ChatOpenAI(temperature=0.3)
    response = llm.invoke(formatted)
    print(f"Response: {response.content}")
    print()


def main():
    """Run all prompt template examples"""
    
    print("=" * 50)
    print("Demo 2: Prompt Templates")
    print("=" * 50)
    print()
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found")
        return
    
    # Run all examples
    example_basic_template()
    example_chat_template()
    example_multi_variable_template()
    example_few_shot_template()
    example_template_composition()
    
    print("=" * 50)
    print("✨ Demo Complete!")
    print("=" * 50)
    print()
    print("💡 Key Learnings:")
    print("   1. Templates make prompts reusable")
    print("   2. Variables allow dynamic content")
    print("   3. Chat templates support role-based messages")
    print("   4. Few-shot examples guide model behavior")
    print("   5. Templates can be composed together")
    print()
    print("📚 Next: Demo 3 - Chains")
    print()


if __name__ == "__main__":
    main()
