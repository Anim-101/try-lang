# Demo 6: Custom Tools

## Overview
This demo shows how to create advanced custom tools for LangChain agents.

## What You'll Learn
- How to create tools using the @tool decorator
- How to create tools using the Tool class
- How to create stateful tools
- Best practices for tool descriptions
- How agents select and use tools

## Running the Demo
```bash
python custom_tools_demo.py
```

## Key Concepts
- **@tool decorator**: Easy way to create tools from functions
- **Tool class**: More flexible tool creation
- **Tool descriptions**: Critical for agent decision-making
- **Error handling**: Making tools robust

## Custom Tools in This Demo
1. **word_counter**: Counts words in text
2. **json_parser**: Parses and formats JSON
3. **text_analyzer**: Provides text statistics
4. **Calculator**: Evaluates mathematical expressions

## Best Practices
- Clear, descriptive tool names
- Detailed descriptions for the agent
- Input validation and error handling
- Return meaningful, formatted results
