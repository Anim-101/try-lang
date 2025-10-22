"""
Demo 2: Prompt Templates
This demo shows different ways to use prompt templates in LangChain.
"""

from langchain_openai import ChatOpenAI
from langchain.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate
)
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def simple_template_demo():
    """Demo using simple prompt template"""
    print("=== Simple Template Demo ===")
    
    llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")
    
    template = "What are {num} uses of {technology}?"
    prompt = PromptTemplate(template=template, input_variables=["num", "technology"])
    
    formatted_prompt = prompt.format(num=3, technology="LangChain")
    print(f"Formatted prompt: {formatted_prompt}\n")
    
    response = llm.predict(formatted_prompt)
    print(f"Response: {response}\n")


def chat_template_demo():
    """Demo using chat prompt template"""
    print("=== Chat Template Demo ===")
    
    llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")
    
    system_template = "You are a helpful assistant that explains {subject} concepts."
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    
    human_template = "Explain {concept} in simple terms."
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    
    chat_prompt = ChatPromptTemplate.from_messages([
        system_message_prompt,
        human_message_prompt
    ])
    
    formatted_prompt = chat_prompt.format_messages(
        subject="machine learning",
        concept="neural networks"
    )
    
    response = llm.predict_messages(formatted_prompt)
    print(f"Response: {response.content}\n")


def main():
    """Run all prompt template demos"""
    simple_template_demo()
    print("\n" + "="*50 + "\n")
    chat_template_demo()


if __name__ == "__main__":
    main()
