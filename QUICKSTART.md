# Quick Start Guide

This guide will help you get started with the LangChain demo projects in minutes.

## Step 1: Environment Setup

### Install Python
Make sure you have Python 3.8 or higher installed:
```bash
python --version
```

### Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Step 2: Configure API Keys

### Get an OpenAI API Key
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API keys section
4. Create a new API key

### Set Up Environment Variables
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your API key
# Replace 'your_openai_api_key_here' with your actual key
```

## Step 3: Run Your First Demo

```bash
# Navigate to the first demo
cd demos/01-basic-llm-chains/

# Run the demo
python basic_chain.py
```

## Troubleshooting

### Import Errors
If you get import errors, make sure you've:
1. Activated the virtual environment
2. Installed all dependencies: `pip install -r requirements.txt`

### API Key Errors
If you get authentication errors:
1. Check that your `.env` file exists in the root directory
2. Verify your API key is correct
3. Ensure you have credits/billing set up on OpenAI

### Module Not Found
If Python can't find modules:
```bash
# Make sure you're in the correct directory
cd /path/to/try-lang

# Reinstall dependencies
pip install -r requirements.txt
```

## Next Steps

1. Complete Demo 1 (Basic LLM Chains)
2. Read the README in each demo folder
3. Experiment with the code
4. Modify parameters and see what changes
5. Move to the next demo

## Tips

- Start with simple modifications to understand how things work
- Read the comments in the code
- Check the LangChain documentation for more details
- Experiment with different temperatures and model parameters
- Monitor your API usage to avoid unexpected costs

## Cost Management

- The demos use GPT-3.5-turbo by default (cheaper than GPT-4)
- Each demo typically costs less than $0.01 to run
- Set usage limits in your OpenAI account
- Use the OpenAI dashboard to monitor spending

## Learning Path

```
01-basic-llm-chains     → Understand LangChain fundamentals
02-prompt-templates     → Learn prompt engineering
03-memory               → Add conversation context
04-agents               → Build intelligent assistants
05-rag-system          → Create knowledge-based apps
06-custom-tools        → Extend agent capabilities
```

Happy learning! 🚀
