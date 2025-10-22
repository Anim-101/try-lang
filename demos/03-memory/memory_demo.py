"""
Demo 3: Memory
This demo shows how to use different types of memory in LangChain conversations.
"""

from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import (
    ConversationBufferMemory,
    ConversationBufferWindowMemory,
    ConversationSummaryMemory
)
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def buffer_memory_demo():
    """Demo using conversation buffer memory"""
    print("=== Buffer Memory Demo ===")
    
    llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")
    memory = ConversationBufferMemory()
    
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )
    
    print("First interaction:")
    print(conversation.predict(input="Hi, my name is Alice"))
    print("\nSecond interaction:")
    print(conversation.predict(input="What's my name?"))
    print("\n")


def window_memory_demo():
    """Demo using conversation buffer window memory"""
    print("=== Window Memory Demo (keeps last 2 interactions) ===")
    
    llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")
    memory = ConversationBufferWindowMemory(k=2)
    
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )
    
    print("First interaction:")
    print(conversation.predict(input="I like Python"))
    print("\nSecond interaction:")
    print(conversation.predict(input="I also like JavaScript"))
    print("\nThird interaction:")
    print(conversation.predict(input="What programming languages do I like?"))
    print("\n")


def main():
    """Run all memory demos"""
    buffer_memory_demo()
    print("\n" + "="*50 + "\n")
    window_memory_demo()


if __name__ == "__main__":
    main()
