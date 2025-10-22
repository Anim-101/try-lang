# Demo 4: Agents

## Overview
This demo demonstrates how to create agents that can use tools to solve tasks.

## What You'll Learn
- How to create custom tools
- How to initialize an agent
- How agents decide which tools to use
- The ReAct (Reasoning + Acting) pattern

## Running the Demo
```bash
python agent_demo.py
```

## Key Concepts
- **Agent**: An LLM that can use tools to accomplish tasks
- **Tools**: Functions the agent can call
- **ReAct**: Reasoning and Acting pattern
- **Zero-Shot**: Agent decides tool usage without examples

## Custom Tools
The demo includes three custom tools:
1. `get_current_time`: Returns current date/time
2. `calculate_age`: Calculates age from birth year
3. `reverse_string`: Reverses a string
