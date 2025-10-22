# TeachMe LangChain 🦜🔗

*A Complete Guide to Learning LangChain from Scratch*

---

## 📋 Table of Contents

1. [What is LangChain?](#what-is-langchain)
2. [Prerequisites](#prerequisites)
3. [Quick Setup](#quick-setup)
4. [Learning Path](#learning-path)
5. [Core Concepts](#core-concepts)
6. [Hands-On Examples](#hands-on-examples)
7. [Project Structure](#project-structure)
8. [Best Practices](#best-practices)
9. [Troubleshooting](#troubleshooting)
10. [Next Steps](#next-steps)
11. [Resources](#resources)

---

## 🤔 What is LangChain?

LangChain is a powerful Python framework for building applications with Large Language Models (LLMs). Think of it as the "glue" that connects AI models to real-world data and tools.

### Why Learn LangChain?

- **🔗 Connect AI to Everything**: Link LLMs to databases, APIs, documents, and more
- **🧩 Modular Design**: Build complex AI systems with reusable components
- **🚀 Rapid Development**: Get AI applications running quickly
- **🔧 Production Ready**: Scale from prototype to production
- **🌟 Active Community**: Huge ecosystem and continuous development

### Real-World Applications

- **📚 Document Q&A Systems**: Chat with your documents
- **🤖 AI Assistants**: Build custom chatbots and agents
- **🔍 Semantic Search**: Find information by meaning, not keywords
- **📊 Data Analysis**: Query databases in natural language
- **🎯 Content Generation**: Create personalized content at scale

---

## 📋 Prerequisites

### Required Knowledge
- **Python Basics**: Variables, functions, classes, imports
- **API Concepts**: Understanding REST APIs and API keys
- **Basic AI/ML**: What are language models and prompts

### Technical Requirements
- **Python 3.8+** (Check: `python --version`)
- **OpenAI API Key** (Get one at: https://platform.openai.com)
- **Terminal/Command Line** basics
- **Code Editor** (VS Code recommended)

### Optional but Helpful
- Understanding of JSON and data structures
- Basic knowledge of web development
- Familiarity with Git and GitHub

---

## 🚀 Quick Setup

### Step 1: Clone and Navigate
```bash
cd try-lang
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment
```bash
# Copy the environment template
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=sk-your-key-here
```

### Step 4: Test Your Setup
```bash
python start.py
```

If you see ✅ symbols, you're ready to go! If not, check the troubleshooting section.

---

## 📚 Learning Path

### 🎯 Phase 1: Foundations (Week 1-2)
**Goal**: Understand core LangChain concepts

1. **Hello LangChain** (`examples/01-basics/01_hello_langchain.py`)
   - Your first LLM interaction
   - Understanding temperature and tokens
   - Error handling basics

2. **Prompt Engineering** (`examples/01-basics/02_prompts.py`)
   - Dynamic prompts with variables
   - Few-shot learning examples
   - Prompt optimization techniques

3. **Chains** (`examples/01-basics/03_chains.py`)
   - Connecting operations together
   - Sequential processing
   - LCEL (LangChain Expression Language)

4. **Output Parsers** (`examples/01-basics/04_output_parsers.py`)
   - Structured data from text
   - JSON output formatting
   - Custom parsing logic

### 🧠 Phase 2: Building Blocks (Week 3-4)
**Goal**: Learn essential components for real applications

5. **Memory Systems** (`examples/02-intermediate/01_memory.py`)
   - Conversation history management
   - Different memory types
   - Context window optimization

6. **Document Processing** (`examples/02-intermediate/02_document_loaders.py`)
   - Loading various file types
   - Text preprocessing
   - Chunking strategies

### 🚀 Phase 3: Real Applications (Week 5-6)
**Goal**: Build production-ready systems

7. **RAG Systems** (`examples/03-advanced/02_rag_system.py`)
   - Retrieval Augmented Generation
   - Vector databases
   - Semantic search

8. **Build Your Own Project**
   - Apply everything learned
   - Create something useful
   - Share with the community

---

## 🔑 Core Concepts

### 1. Large Language Models (LLMs)
```python
from langchain_openai import OpenAI

# Initialize an LLM
llm = OpenAI(temperature=0.7)  # Higher = more creative
response = llm.invoke("Explain quantum computing simply")
```

**Key Points**:
- Temperature controls randomness (0.0 = deterministic, 1.0 = creative)
- Different models have different strengths
- Cost varies by model and usage

### 2. Prompts and Templates
```python
from langchain_core.prompts import PromptTemplate

# Create reusable prompts
prompt = PromptTemplate(
    input_variables=["topic", "audience"],
    template="Explain {topic} to a {audience} in simple terms"
)

formatted = prompt.format(topic="machine learning", audience="child")
```

**Key Points**:
- Templates make prompts reusable
- Variables allow dynamic content
- Good prompts = better results

### 3. Chains
```python
# Simple chain: Prompt → LLM → Parser
chain = prompt | llm | StrOutputParser()
result = chain.invoke({"topic": "AI", "audience": "beginner"})
```

**Key Points**:
- Chains connect components
- Use `|` operator for simple chaining
- Can create complex workflows

### 4. Memory
```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
# Stores conversation history automatically
```

**Types**:
- **Buffer**: Stores everything
- **Window**: Keeps last N messages
- **Summary**: Summarizes old conversations

### 5. Retrieval Augmented Generation (RAG)
```
[Documents] → [Vector Store] → [Retriever] → [LLM] → [Answer]
     ↑              ↑              ↑
  Upload        Embeddings    Find Relevant
```

**Key Points**:
- Combines your data with LLM knowledge
- Reduces hallucinations
- Enables up-to-date information

---

## 🛠 Hands-On Examples

### Example 1: Simple Q&A Bot
```python
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

# Setup
llm = OpenAI(temperature=0.3)
prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer this question helpfully and concisely: {question}"
)

# Create chain
qa_chain = prompt | llm

# Use it
answer = qa_chain.invoke({"question": "What is Python?"})
print(answer)
```

### Example 2: Document Summarizer
```python
# Load document
with open("document.txt", "r") as f:
    text = f.read()

# Create summarization prompt
summary_prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize this text in 3 bullet points:\n\n{text}"
)

# Summarize
summary_chain = summary_prompt | llm
result = summary_chain.invoke({"text": text})
```

### Example 3: Conversation with Memory
```python
class SimpleChatBot:
    def __init__(self):
        self.llm = OpenAI(temperature=0.7)
        self.history = []
    
    def chat(self, message):
        # Add to history
        self.history.append(f"Human: {message}")
        
        # Create context from history
        context = "\n".join(self.history[-6:])  # Last 6 messages
        
        # Generate response
        prompt = f"Conversation:\n{context}\nAI: "
        response = self.llm.invoke(prompt)
        
        # Add response to history
        self.history.append(f"AI: {response}")
        
        return response

# Usage
bot = SimpleChatBot()
response1 = bot.chat("Hi, I'm learning Python")
response2 = bot.chat("What should I learn next?")
```

---

## 📁 Project Structure

```
try-lang/
├── 📄 README.md                 # Project overview
├── 📄 TeachMe.md               # This comprehensive guide
├── 📄 requirements.txt          # Python dependencies
├── 📄 .env.example             # Environment template
├── 🐍 start.py                 # Setup checker
│
├── 📁 examples/
│   ├── 📁 01-basics/           # Foundation concepts
│   │   ├── 🐍 01_hello_langchain.py      # First LLM interaction
│   │   ├── 🐍 02_prompts.py              # Dynamic prompts
│   │   ├── 🐍 03_chains.py               # Connecting operations
│   │   └── 🐍 04_output_parsers.py       # Structured output
│   │
│   ├── 📁 02-intermediate/     # Building blocks
│   │   ├── 🐍 01_memory.py               # Conversation memory
│   │   └── 🐍 02_document_loaders.py     # File processing
│   │
│   └── 📁 03-advanced/         # Real applications
│       └── 🐍 02_rag_system.py           # Q&A with documents
```

### Running the Examples

```bash
# Start with basics
cd examples/01-basics
python 01_hello_langchain.py

# Progress through each file
python 02_prompts.py
python 03_chains.py
python 04_output_parsers.py

# Move to intermediate
cd ../02-intermediate
python 01_memory.py
python 02_document_loaders.py

# Try advanced examples
cd ../03-advanced
python 02_rag_system.py
```

---

## 💡 Best Practices

### 1. Prompt Design
```python
# ❌ Vague prompt
"Tell me about AI"

# ✅ Specific prompt
"Explain machine learning in 3 paragraphs for someone with no technical background"
```

### 2. Error Handling
```python
try:
    response = llm.invoke(prompt)
    return response
except Exception as e:
    print(f"Error: {e}")
    return "Sorry, I couldn't process that request."
```

### 3. API Key Security
```python
# ✅ Use environment variables
import os
api_key = os.getenv("OPENAI_API_KEY")

# ❌ Never hardcode keys
api_key = "sk-your-actual-key"  # Don't do this!
```

### 4. Cost Management
```python
# Control token usage
llm = OpenAI(
    temperature=0.7,
    max_tokens=150,  # Limit response length
    model="gpt-3.5-turbo"  # Use appropriate model
)
```

### 5. Testing
```python
# Test with different inputs
test_cases = [
    "What is Python?",
    "Explain quantum physics",
    "Tell me a joke"
]

for test in test_cases:
    result = chain.invoke({"question": test})
    print(f"Q: {test}\nA: {result}\n---")
```

---

## 🔧 Troubleshooting

### Common Issues

#### 1. Import Errors
```bash
# Error: ModuleNotFoundError: No module named 'langchain'
# Solution:
pip install -r requirements.txt
```

#### 2. API Key Issues
```bash
# Error: OpenAI API key not found
# Solution: Check your .env file
cat .env  # Should show OPENAI_API_KEY=sk-...
```

#### 3. Rate Limiting
```python
# Error: Rate limit exceeded
# Solution: Add delays between requests
import time
time.sleep(1)  # Wait 1 second between calls
```

#### 4. Memory Issues
```python
# Error: Context too long
# Solution: Limit conversation history
history = history[-10:]  # Keep only last 10 messages
```

### Getting Help

1. **Check the error message** - Often tells you exactly what's wrong
2. **Review the example code** - Compare with working examples
3. **Search the documentation** - https://python.langchain.com/
4. **Ask the community** - Discord, Stack Overflow, GitHub issues

---

## 🚀 Next Steps

### After Completing the Basics

1. **Build a Personal Project**
   - Document Q&A system for your notes
   - AI writing assistant
   - Code explanation tool

2. **Explore Advanced Topics**
   - Vector databases (Pinecone, Chroma)
   - Agent frameworks
   - Custom tool integration
   - Streaming responses

3. **Production Considerations**
   - Error handling and logging
   - Performance optimization
   - Security best practices
   - Monitoring and analytics

### Project Ideas

#### Beginner Projects
- **Recipe Assistant**: Ask questions about cooking
- **Study Buddy**: Quiz yourself on topics
- **Email Helper**: Generate professional emails

#### Intermediate Projects
- **Personal Knowledge Base**: Search your documents
- **Code Reviewer**: Analyze and explain code
- **Meeting Summarizer**: Extract key points from transcripts

#### Advanced Projects
- **Multi-Agent System**: Coordinate multiple AI agents
- **Real-time Chat**: WebSocket-based chat interface
- **API Integration**: Connect to external services

---

## 📚 Resources

### Official Documentation
- **LangChain Docs**: https://python.langchain.com/
- **API Reference**: https://api.python.langchain.com/
- **Cookbook**: https://github.com/langchain-ai/langchain/tree/master/cookbook

### Community
- **Discord**: https://discord.gg/langchain
- **GitHub**: https://github.com/langchain-ai/langchain
- **Twitter**: @LangChainAI

### Learning Materials
- **LangChain Course**: https://www.deeplearning.ai/short-courses/
- **YouTube Tutorials**: Search "LangChain tutorial"
- **Blog Posts**: Medium, Towards Data Science

### Tools and Extensions
- **LangSmith**: Debugging and monitoring
- **LangServe**: Deploy LangChain apps
- **LangGraph**: Build complex workflows

### Related Technologies
- **Vector Databases**: Pinecone, Chroma, Weaviate
- **Embeddings**: OpenAI, Hugging Face, Cohere
- **Deployment**: Streamlit, FastAPI, Docker

---

## 🎯 Learning Checklist

### Phase 1: Foundations
- [ ] Run your first LangChain program
- [ ] Create dynamic prompts with variables
- [ ] Build a simple chain
- [ ] Parse structured output from LLMs
- [ ] Understand temperature and token limits

### Phase 2: Building Blocks
- [ ] Implement conversation memory
- [ ] Load and process different file types
- [ ] Handle errors gracefully
- [ ] Optimize prompts for better results
- [ ] Manage API costs effectively

### Phase 3: Applications
- [ ] Build a RAG system
- [ ] Create a functional chatbot
- [ ] Deploy a simple web interface
- [ ] Handle real user data
- [ ] Implement proper security measures

### Mastery Goals
- [ ] Design effective prompt strategies
- [ ] Choose appropriate memory types
- [ ] Optimize for performance and cost
- [ ] Debug complex chain issues
- [ ] Build production-ready applications

---

## 🎉 Conclusion

Congratulations on starting your LangChain journey! This framework opens up incredible possibilities for building AI-powered applications. Remember:

- **Start Small**: Begin with simple examples
- **Practice Regularly**: Consistency beats intensity
- **Experiment Freely**: Try different approaches
- **Join the Community**: Learn from others
- **Build Real Projects**: Apply your knowledge

The AI landscape is evolving rapidly, and LangChain puts you at the forefront of this revolution. Whether you're building chatbots, document analyzers, or complex AI agents, the fundamentals you learn here will serve you well.

**Happy coding!** 🚀

---

*Last updated: October 2025*
*Created for the try-lang learning repository*