#!/usr/bin/env python3
"""
Getting Started Script for LangChain Learning
Run this to test your setup and see a quick demo
"""

import os
import sys
from dotenv import load_dotenv

def check_setup():
    """Check if everything is set up correctly"""
    print("🔧 Checking LangChain Setup...")
    print("=" * 35)
    
    # Check Python version
    python_version = sys.version_info
    print(f"🐍 Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version < (3, 8):
        print("❌ Python 3.8+ required")
        return False
    
    # Check for .env file
    env_file = ".env"
    if os.path.exists(env_file):
        print("✅ .env file found")
        load_dotenv()
    else:
        print("⚠️  .env file not found - copy .env.example to .env and add your keys")
        return False
    
    # Check API key
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        masked_key = api_key[:8] + "..." + api_key[-4:]
        print(f"✅ OpenAI API key found: {masked_key}")
    else:
        print("❌ OPENAI_API_KEY not set in .env file")
        return False
    
    # Check imports
    try:
        import langchain
        print(f"✅ LangChain installed: version {langchain.__version__}")
    except ImportError:
        print("❌ LangChain not installed - run: pip install -r requirements.txt")
        return False
    
    try:
        from langchain_openai import OpenAI
        print("✅ OpenAI integration available")
    except ImportError:
        print("❌ OpenAI integration not available")
        return False
    
    return True

def quick_demo():
    """Run a quick LangChain demo"""
    print("\n🚀 Quick LangChain Demo")
    print("=" * 25)
    
    try:
        from langchain_openai import OpenAI
        
        # Initialize LLM
        llm = OpenAI(temperature=0.7, max_tokens=100)
        
        # Simple test
        prompt = "In one sentence, explain what makes LangChain useful:"
        print(f"📝 Prompt: {prompt}")
        
        response = llm.invoke(prompt)
        print(f"🤖 Response: {response.strip()}")
        
        print("\n✅ Demo successful! LangChain is working correctly.")
        
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        return False
    
    return True

def show_next_steps():
    """Show recommended next steps"""
    print("\n📚 Recommended Learning Path:")
    print("=" * 35)
    
    print("1. 📁 Start with basics:")
    print("   cd examples/01-basics")
    print("   python 01_hello_langchain.py")
    
    print("\n2. 🎯 Learn core concepts:")
    print("   python 02_prompts.py")
    print("   python 03_chains.py") 
    print("   python 04_output_parsers.py")
    
    print("\n3. 🧠 Explore intermediate topics:")
    print("   cd ../02-intermediate")
    print("   python 01_memory.py")
    print("   python 02_document_loaders.py")
    
    print("\n4. 🚀 Try advanced examples:")
    print("   cd ../03-advanced")
    print("   python 02_rag_system.py")
    
    print("\n💡 Additional Resources:")
    print("   📖 Read the updated README.md")
    print("   🌐 Visit: https://python.langchain.com/")
    print("   💬 Join: https://discord.gg/langchain")

def main():
    """Main function"""
    print("🎉 Welcome to LangChain Learning!")
    print("=" * 40)
    
    # Check setup
    if not check_setup():
        print("\n❌ Setup incomplete. Please fix the issues above.")
        return
    
    print("\n✅ Setup looks good!")
    
    # Run demo
    if quick_demo():
        show_next_steps()
    else:
        print("\n❌ Demo failed. Check your API key and internet connection.")

if __name__ == "__main__":
    main()