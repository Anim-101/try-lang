# LangChain Learning Repository

A collection of demo projects for learning the LangChain framework through hands-on examples.

## Overview

This repository contains structured demo projects covering fundamental to advanced LangChain concepts. Each demo is self-contained with its own README and runnable code.

## Setup

### Prerequisites
- Python 3.8 or higher
- OpenAI API key (or other LLM provider API key)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Anim-101/try-lang.git
cd try-lang
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your API keys
```

## Demo Projects

### 1. Basic LLM Chains
**Location**: `demos/01-basic-llm-chains/`

Learn the fundamentals of creating and using LLM chains.
- Initialize LLMs
- Create prompt templates
- Chain components together

### 2. Prompt Templates
**Location**: `demos/02-prompt-templates/`

Explore different types of prompt templates.
- Simple templates with variables
- Chat prompt templates
- System and human message prompts

### 3. Memory
**Location**: `demos/03-memory/`

Add memory to maintain conversation context.
- Buffer memory (stores entire conversation)
- Window memory (stores last k interactions)
- Memory effects on conversation flow

### 4. Agents
**Location**: `demos/04-agents/`

Create agents that can use tools to solve tasks.
- Custom tool creation
- Agent initialization
- ReAct pattern (Reasoning + Acting)

### 5. RAG System
**Location**: `demos/05-rag-system/`

Build a Retrieval Augmented Generation system.
- Document splitting and embeddings
- Vector stores (ChromaDB)
- Retrieval-based QA

### 6. Custom Tools
**Location**: `demos/06-custom-tools/`

Create advanced custom tools for agents.
- Tool decorator usage
- Tool class implementation
- Best practices for tool creation

## Running the Demos

Each demo can be run independently:

```bash
# Navigate to a demo directory
cd demos/01-basic-llm-chains/

# Run the demo
python basic_chain.py
```

## Project Structure

```
try-lang/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
└── demos/
    ├── 01-basic-llm-chains/
    │   ├── README.md
    │   └── basic_chain.py
    ├── 02-prompt-templates/
    │   ├── README.md
    │   └── prompt_templates.py
    ├── 03-memory/
    │   ├── README.md
    │   └── memory_demo.py
    ├── 04-agents/
    │   ├── README.md
    │   └── agent_demo.py
    ├── 05-rag-system/
    │   ├── README.md
    │   └── rag_demo.py
    └── 06-custom-tools/
        ├── README.md
        └── custom_tools_demo.py
```

## Learning Path

For the best learning experience, follow the demos in order:

1. Start with **Basic LLM Chains** to understand core concepts
2. Move to **Prompt Templates** to learn prompt engineering
3. Add **Memory** to create conversational applications
4. Explore **Agents** to build intelligent assistants
5. Implement **RAG Systems** for knowledge-based applications
6. Create **Custom Tools** to extend agent capabilities

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [OpenAI API Documentation](https://platform.openai.com/docs)

## Contributing

Feel free to add more demo projects or improve existing ones. Each demo should:
- Be self-contained
- Include a README with clear explanations
- Follow the existing code style
- Include comments for clarity

## License

MIT License - see LICENSE file for details

## Notes

- Always keep your API keys secure and never commit them to the repository
- The demos use OpenAI by default, but can be adapted for other LLM providers
- Some demos may incur API costs when run
