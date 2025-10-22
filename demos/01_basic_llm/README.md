# Demo 1: Basic LLM Interaction

## 🎯 Learning Objectives

In this demo, you'll learn:
- How to set up LangChain with OpenAI
- Make basic LLM calls
- Understand model parameters (temperature, max_tokens, etc.)
- Handle responses

## 📋 Prerequisites

- Python environment set up
- OpenAI API key configured in `.env`
- Dependencies installed from `requirements.txt`

## 🔑 Concepts Covered

### 1. LLM Initialization
Learn how to initialize an LLM (Language Learning Model) with LangChain.

### 2. Simple Completions
Make basic text completions and understand how the model responds.

### 3. Model Parameters
- **temperature**: Controls randomness (0 = deterministic, 1 = creative)
- **max_tokens**: Maximum length of response
- **model**: Which model to use (gpt-3.5-turbo, gpt-4, etc.)

## 🚀 Running the Demo

```bash
cd demos/01_basic_llm
python example.py
```

## 📝 What You'll Build

A simple script that:
1. Connects to OpenAI through LangChain
2. Sends prompts to the LLM
3. Receives and displays responses
4. Experiments with different parameters

## 💡 Try This

After running the example, try:
- Changing the temperature value
- Using different prompts
- Adjusting max_tokens
- Testing different models (if available)

## 🔗 Next Steps

Once you're comfortable with basic LLM calls, move on to:
- **Demo 2**: Prompt Templates - Learn to create reusable, dynamic prompts
