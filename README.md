# 🦜🔗 LangChain Learning Repository

A hands-on learning repository for mastering LangChain through practical demo projects.

## 📚 About

This repository contains a progressive series of demo projects to help you learn LangChain from basics to advanced concepts. Each demo is self-contained and builds upon previous concepts.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenAI API key (or other LLM provider key)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Anim-101/try-lang.git
   cd try-lang
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

## 📖 Learning Path

The demos are organized in a progressive learning path:

### Demo 1: Basic LLM Interaction
**Location:** `demos/01_basic_llm/`
- Connect to OpenAI/LLM
- Make simple completions
- Understanding models and parameters

### Demo 2: Prompt Templates
**Location:** `demos/02_prompt_templates/`
- Create reusable prompt templates
- Use variables in prompts
- Build prompt chains

### Demo 3: Chains and Sequential Operations
**Location:** `demos/03_chains/`
- Create simple chains
- Build sequential workflows
- Combine multiple operations

### Demo 4: Memory and Conversations
**Location:** `demos/04_memory/`
- Add conversation memory
- Build chatbots
- Manage conversation context

### Demo 5: Document Q&A
**Location:** `demos/05_document_qa/`
- Load and process documents
- Create vector embeddings
- Build Q&A systems

### Demo 6: Agents and Tools
**Location:** `demos/06_agents/`
- Create custom tools
- Build agents
- Autonomous decision making

## 🛠️ Project Structure

```
try-lang/
├── demos/                  # All demo projects
│   ├── 01_basic_llm/
│   ├── 02_prompt_templates/
│   ├── 03_chains/
│   ├── 04_memory/
│   ├── 05_document_qa/
│   └── 06_agents/
├── resources/             # Shared resources
│   ├── sample_docs/       # Sample documents for demos
│   └── utils/             # Utility functions
├── .env.example           # Environment variables template
├── .gitignore
├── requirements.txt       # Python dependencies
└── README.md
```

## 📝 Usage

Each demo folder contains:
- `README.md` - Explanation of concepts
- `example.py` - Runnable example code
- `exercises.py` - Practice exercises (optional)

To run a demo:
```bash
cd demos/01_basic_llm
python example.py
```

## 🔑 API Keys

You'll need API keys from LLM providers:
- **OpenAI**: https://platform.openai.com/api-keys
- **Anthropic** (optional): https://console.anthropic.com/
- **HuggingFace** (optional): https://huggingface.co/settings/tokens

## 🤝 Contributing

Feel free to:
- Add more demo projects
- Improve existing examples
- Fix bugs or typos
- Share your learning experience

## 📚 Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangChain Tutorials](https://python.langchain.com/docs/tutorials/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)

## 📄 License

MIT License - see LICENSE file for details

## 🎯 Learning Tips

1. **Start with Demo 1** - Don't skip ahead, each demo builds on previous concepts
2. **Experiment** - Modify the code, break things, learn by doing
3. **Read Comments** - Each demo has detailed comments explaining the code
4. **Check API Costs** - Be mindful of API usage to avoid unexpected costs
5. **Use .env** - Never commit API keys to version control

Happy Learning! 🚀
