# Demo 3: Memory

## Overview
This demo shows how to add memory to your LangChain applications to maintain conversation context.

## What You'll Learn
- ConversationBufferMemory (stores entire conversation)
- ConversationBufferWindowMemory (stores last k interactions)
- How memory affects conversation flow

## Running the Demo
```bash
python memory_demo.py
```

## Key Concepts
- **Memory**: Stores conversation history
- **Buffer Memory**: Keeps all messages
- **Window Memory**: Keeps only recent k messages
- **Context**: How the model maintains awareness of previous interactions
