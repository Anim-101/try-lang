# Quick Start Guide

Get started with LangChain in 5 minutes!

## Step 1: Clone the Repository

```bash
git clone https://github.com/Anim-101/try-lang.git
cd try-lang
```

## Step 2: Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

## Step 3: Install Dependencies

```bash
# Option A: Use setup script (recommended)
python setup.py

# Option B: Manual installation
pip install -r requirements.txt
```

## Step 4: Configure API Key

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your OpenAI API key
# Get your key from: https://platform.openai.com/api-keys
```

Your `.env` file should look like:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

## Step 5: Run Your First Demo

```bash
cd demos/01_basic_llm
python example.py
```

You should see output demonstrating basic LLM interactions!

## What's Next?

Follow the learning path in order:

1. **Demo 1**: Basic LLM - Understanding models and parameters
2. **Demo 2**: Prompt Templates - Creating reusable prompts
3. **Demo 3**: Chains - Building sequential workflows
4. **Demo 4**: Memory - Adding conversation context
5. **Demo 5**: Document Q&A - Building knowledge bases
6. **Demo 6**: Agents - Creating autonomous AI systems

## Troubleshooting

### API Key Not Found
Make sure:
- `.env` file exists in the root directory
- `OPENAI_API_KEY` is set correctly
- No extra spaces around the API key

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Python Version Issues
This project requires Python 3.8+:
```bash
python --version  # Should be 3.8 or higher
```

## Cost Considerations

The demos use OpenAI's API which has costs:
- Most demos use very few tokens
- Estimated cost per demo: $0.01 - $0.05
- Set usage limits in your OpenAI account

## Learning Tips

1. **Read Before Running**: Check each demo's README first
2. **Experiment**: Modify the code and see what happens
3. **Use Verbose Mode**: Many demos have verbose options for learning
4. **Check Comments**: Code is heavily commented for learning
5. **Start Simple**: Don't skip ahead - each demo builds on previous ones

## Getting Help

- Check the main [README.md](README.md)
- Review [CONTRIBUTING.md](CONTRIBUTING.md)
- Read demo-specific README files
- Check LangChain [documentation](https://python.langchain.com/)

## Ready to Go!

You're all set! Start with Demo 1 and enjoy learning LangChain! 🚀

```bash
cd demos/01_basic_llm
python example.py
```

Happy Learning! 🎓
