"""
01_memory.py
Conversation Memory Systems - Maintaining context across interactions
"""

import os
from dotenv import load_dotenv
from langchain_openai import OpenAI

# Load environment variables
load_dotenv()

class SimpleMemory:
    """Simple memory implementation to demonstrate concepts"""
    
    def __init__(self, max_messages=10):
        self.messages = []
        self.max_messages = max_messages
    
    def add_message(self, role, content):
        """Add a message to memory"""
        self.messages.append({"role": role, "content": content})
        
        # Keep only last max_messages
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]
    
    def get_history(self):
        """Get conversation history as string"""
        history = ""
        for msg in self.messages:
            history += f"{msg['role']}: {msg['content']}\n"
        return history

def simple_memory_demo():
    """
    Demonstrate simple conversation with memory
    """
    print("💭 Simple Memory Conversation Demo")
    print("=" * 40)
    
    llm = OpenAI(temperature=0.7)
    memory = SimpleMemory(max_messages=6)  # Keep last 6 messages
    
    # Conversation steps
    conversation_steps = [
        "Hi, my name is Sarah and I'm a teacher.",
        "I teach 5th grade mathematics.",
        "I'm looking for fun ways to teach fractions.",
        "What's my name and what do I teach?"
    ]
    
    for i, user_input in enumerate(conversation_steps, 1):
        print(f"\n--- Turn {i} ---")
        print(f"👤 User: {user_input}")
        
        # Add user message to memory
        memory.add_message("Human", user_input)
        
        # Get history and create prompt
        history = memory.get_history()
        prompt = f"""You are a helpful educational assistant. Here's our conversation:

{history}

Please respond helpfully to the latest message."""

        # Get AI response
        try:
            response = llm.invoke(prompt)
            print(f"🤖 Assistant: {response.strip()}")
            
            # Add AI response to memory
            memory.add_message("Assistant", response.strip())
            
        except Exception as e:
            print(f"❌ Error: {e}")
        
        # Show current memory state
        print(f"📊 Memory contains {len(memory.messages)} messages")

def window_memory_demo():
    """
    Demonstrate memory with limited window
    """
    print("\n🪟 Window Memory Demo (max 4 messages)")
    print("=" * 45)
    
    llm = OpenAI(temperature=0.7)
    memory = SimpleMemory(max_messages=4)  # Very small window
    
    inputs = [
        "I love pizza",
        "My favorite color is blue", 
        "I work as a programmer",
        "I have a cat named Whiskers",
        "What do you know about me?"  # Should have forgotten early info
    ]
    
    for i, user_input in enumerate(inputs, 1):
        print(f"\n--- Exchange {i} ---")
        print(f"👤 {user_input}")
        
        memory.add_message("Human", user_input)
        
        # Simple prompt for this demo
        prompt = f"Based on our conversation: {memory.get_history()}\nRespond to: {user_input}"
        
        try:
            response = llm.invoke(prompt)
            print(f"🤖 {response.strip()[:100]}...")
            memory.add_message("Assistant", response.strip()[:50])
            
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    """
    Run memory demonstrations
    """
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Please set your OPENAI_API_KEY in .env file")
        return
    
    try:
        # Demo 1: Simple memory conversation
        simple_memory_demo()
        
        # Demo 2: Window memory (limited)
        window_memory_demo()
        
        print("\n✅ Memory demonstrations completed!")
        print("\n💡 Key Memory Concepts:")
        print("   🧠 Buffer Memory: Stores all conversation history")
        print("   🪟 Window Memory: Keeps only recent N messages") 
        print("   📄 Summary Memory: Summarizes old conversations")
        print("   💾 Persistent Memory: Saves across sessions")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
