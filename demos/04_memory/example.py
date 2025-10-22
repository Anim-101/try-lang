"""
Demo 4: Memory and Conversation Management

This script demonstrates how to add memory to LLM conversations,
enabling stateful chatbots that remember previous interactions.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import (
    ConversationBufferMemory,
    ConversationBufferWindowMemory,
    ConversationSummaryMemory
)
from langchain.chains import ConversationChain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

# Load environment variables
load_dotenv()


def example_basic_conversation_memory():
    """Demonstrates basic conversation with memory"""
    
    print("💬 Example 1: Basic Conversation Memory")
    print("-" * 50)
    
    # Create LLM
    llm = ChatOpenAI(temperature=0.7)
    
    # Create memory to store conversation
    memory = ConversationBufferMemory(return_messages=True)
    
    # Create conversation chain
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=False  # Set to True to see what's happening
    )
    
    # First message
    print("User: My name is Alice")
    response1 = conversation.predict(input="My name is Alice")
    print(f"AI: {response1}")
    print()
    
    # Second message - AI should remember the name
    print("User: What's my name?")
    response2 = conversation.predict(input="What's my name?")
    print(f"AI: {response2}")
    print()
    
    # Check conversation history
    print("📝 Conversation History:")
    print(memory.load_memory_variables({}))
    print()


def example_buffer_window_memory():
    """Demonstrates conversation with window memory (limited history)"""
    
    print("💬 Example 2: Buffer Window Memory")
    print("-" * 50)
    print("(Keeps only the last K messages)")
    print()
    
    llm = ChatOpenAI(temperature=0.7)
    
    # Keep only last 2 interactions (4 messages: 2 user, 2 assistant)
    memory = ConversationBufferWindowMemory(
        k=2,  # Number of interactions to remember
        return_messages=True
    )
    
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=False
    )
    
    # Multiple interactions
    messages = [
        "Hi, I'm learning Python",
        "I also like JavaScript",
        "What programming languages did I mention?"  # Should remember only the last 2
    ]
    
    for msg in messages:
        print(f"User: {msg}")
        response = conversation.predict(input=msg)
        print(f"AI: {response}")
        print()
    
    print("📝 Memory Buffer (last 2 interactions):")
    print(memory.load_memory_variables({}))
    print()


def example_summary_memory():
    """Demonstrates conversation with summary memory"""
    
    print("💬 Example 3: Summary Memory")
    print("-" * 50)
    print("(Summarizes old conversations to save tokens)")
    print()
    
    llm = ChatOpenAI(temperature=0.7)
    
    # Create summary memory
    memory = ConversationSummaryMemory(
        llm=llm,
        return_messages=True
    )
    
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=False
    )
    
    # Have a longer conversation
    print("User: I work as a software engineer")
    response1 = conversation.predict(input="I work as a software engineer")
    print(f"AI: {response1}")
    print()
    
    print("User: I specialize in backend development with Python")
    response2 = conversation.predict(input="I specialize in backend development with Python")
    print(f"AI: {response2}")
    print()
    
    print("User: What do you know about me?")
    response3 = conversation.predict(input="What do you know about me?")
    print(f"AI: {response3}")
    print()
    
    # Show the summary
    print("📝 Conversation Summary:")
    print(memory.load_memory_variables({}))
    print()


def example_custom_memory_prompt():
    """Demonstrates custom prompt with memory"""
    
    print("💬 Example 4: Custom Memory Prompt")
    print("-" * 50)
    
    llm = ChatOpenAI(temperature=0.7)
    
    # Create a custom prompt with memory placeholder
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful coding assistant. Be concise and friendly."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    
    memory = ConversationBufferMemory(return_messages=True, memory_key="history")
    
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        prompt=prompt,
        verbose=False
    )
    
    # Conversation about coding
    print("User: How do I create a list in Python?")
    response1 = conversation.predict(input="How do I create a list in Python?")
    print(f"AI: {response1}")
    print()
    
    print("User: Can you show me an example?")
    response2 = conversation.predict(input="Can you show me an example?")
    print(f"AI: {response2}")
    print()
    
    print("User: What was my first question?")
    response3 = conversation.predict(input="What was my first question?")
    print(f"AI: {response3}")
    print()


def example_chatbot_simulation():
    """Demonstrates a practical chatbot simulation"""
    
    print("💬 Example 5: Interactive Chatbot Simulation")
    print("-" * 50)
    print("(Simulating a customer support chatbot)")
    print()
    
    llm = ChatOpenAI(temperature=0.7)
    
    # Custom prompt for customer support
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful customer support agent for TechStore.
        Be friendly, professional, and helpful. Keep track of customer issues
        and provide relevant solutions."""),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    
    memory = ConversationBufferMemory(return_messages=True, memory_key="history")
    
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        prompt=prompt,
        verbose=False
    )
    
    # Simulate customer conversation
    customer_messages = [
        "Hi, I'm having trouble with my recent order",
        "My order number is #12345",
        "The product arrived damaged",
        "What are my options?"
    ]
    
    for msg in customer_messages:
        print(f"Customer: {msg}")
        response = conversation.predict(input=msg)
        print(f"Support: {response}")
        print()
    
    print("📝 Full Conversation Context Available for Agent")
    print()


def example_memory_clearing():
    """Demonstrates how to clear and manage memory"""
    
    print("💬 Example 6: Managing and Clearing Memory")
    print("-" * 50)
    
    llm = ChatOpenAI(temperature=0.7)
    memory = ConversationBufferMemory(return_messages=True)
    
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=False
    )
    
    # First conversation
    print("--- First Conversation ---")
    print("User: Remember that I like pizza")
    response1 = conversation.predict(input="Remember that I like pizza")
    print(f"AI: {response1}")
    print()
    
    print("User: What do I like?")
    response2 = conversation.predict(input="What do I like?")
    print(f"AI: {response2}")
    print()
    
    # Clear memory
    print("🧹 Clearing memory...")
    memory.clear()
    print()
    
    # New conversation (should not remember)
    print("--- New Conversation (after clearing) ---")
    print("User: What do I like?")
    response3 = conversation.predict(input="What do I like?")
    print(f"AI: {response3}")
    print()


def main():
    """Run all memory examples"""
    
    print("=" * 50)
    print("Demo 4: Memory and Conversation Management")
    print("=" * 50)
    print()
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found")
        return
    
    # Run all examples
    example_basic_conversation_memory()
    example_buffer_window_memory()
    example_summary_memory()
    example_custom_memory_prompt()
    example_chatbot_simulation()
    example_memory_clearing()
    
    print("=" * 50)
    print("✨ Demo Complete!")
    print("=" * 50)
    print()
    print("💡 Key Learnings:")
    print("   1. Memory enables stateful conversations")
    print("   2. ConversationBufferMemory stores all messages")
    print("   3. BufferWindowMemory limits context size")
    print("   4. SummaryMemory summarizes to save tokens")
    print("   5. Custom prompts can integrate with memory")
    print("   6. Memory can be cleared between conversations")
    print()
    print("📚 Next: Demo 5 - Document Q&A with Embeddings")
    print()


if __name__ == "__main__":
    main()
