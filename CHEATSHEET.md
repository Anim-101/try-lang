# LangChain Cheat Sheet

Quick reference for common LangChain patterns and code snippets.

## Basic LLM Usage

### Initialize LLM
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    max_tokens=150
)
```

### Simple Completion
```python
response = llm.invoke("What is LangChain?")
print(response.content)
```

## Prompt Templates

### Basic Template
```python
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write about {topic}"
)
formatted = prompt.format(topic="AI")
```

### Chat Template
```python
from langchain.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a {role}"),
    ("user", "{input}")
])
```

### Few-Shot Template
```python
from langchain.prompts.few_shot import FewShotPromptTemplate

examples = [
    {"input": "happy", "output": "I'm joyful!"},
    {"input": "sad", "output": "I'm feeling down."}
]

few_shot = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Respond to emotions:",
    suffix="Emotion: {input}\nResponse:",
    input_variables=["input"]
)
```

## Chains

### LCEL Chain (Modern)
```python
from langchain.schema.output_parser import StrOutputParser

chain = prompt | llm | StrOutputParser()
result = chain.invoke({"topic": "Python"})
```

### Sequential Chain
```python
# Chain 1
chain1 = prompt1 | llm | StrOutputParser()

# Chain 2 uses output from chain1
chain2 = prompt2 | llm | StrOutputParser()

# Execute
result1 = chain1.invoke({"input": "data"})
result2 = chain2.invoke({"input": result1})
```

## Memory

### Buffer Memory
```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(llm=llm, memory=memory)

response = conversation.predict(input="My name is Alice")
```

### Window Memory (Last K)
```python
from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(
    k=2,  # Keep last 2 interactions
    return_messages=True
)
```

### Summary Memory
```python
from langchain.memory import ConversationSummaryMemory

memory = ConversationSummaryMemory(
    llm=llm,
    return_messages=True
)
```

## Document Q&A

### Load and Split Documents
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

# Create documents
docs = [Document(page_content="text", metadata={"source": "file.txt"})]

# Split
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = splitter.split_documents(docs)
```

### Create Vector Store
```python
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="my_docs"
)
```

### Q&A Chain
```python
from langchain.chains import RetrievalQA

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(),
    return_source_documents=True
)

result = qa.invoke({"query": "What is this about?"})
print(result['result'])
```

### Similarity Search
```python
# Find similar documents
docs = vectorstore.similarity_search("query text", k=3)
```

## Agents and Tools

### Create Tool
```python
from langchain.tools import tool

@tool
def my_tool(input: str) -> str:
    """Tool description for the agent."""
    return f"Processed: {input}"
```

### Create Agent
```python
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

# Get ReAct prompt
prompt = hub.pull("hwchase17/react")

# Create agent
agent = create_react_agent(llm, tools, prompt)

# Create executor
executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

# Run
result = executor.invoke({"input": "What is 2+2?"})
```

### Tool from Function
```python
from langchain.agents import Tool

def calculator(input: str) -> str:
    return str(eval(input))

tool = Tool(
    name="Calculator",
    func=calculator,
    description="Useful for math calculations"
)
```

## Common Patterns

### Environment Setup
```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

### Error Handling
```python
try:
    response = llm.invoke(prompt)
except Exception as e:
    print(f"Error: {e}")
```

### Streaming Responses
```python
for chunk in llm.stream("Write a story"):
    print(chunk.content, end="", flush=True)
```

### Custom Callbacks
```python
from langchain.callbacks import StreamingStdOutCallbackHandler

llm = ChatOpenAI(
    callbacks=[StreamingStdOutCallbackHandler()],
    streaming=True
)
```

## Model Parameters

| Parameter | Description | Range |
|-----------|-------------|-------|
| `temperature` | Randomness (0=deterministic, 1=creative) | 0.0-1.0 |
| `max_tokens` | Maximum response length | 1-4096+ |
| `top_p` | Nucleus sampling | 0.0-1.0 |
| `frequency_penalty` | Reduce repetition | -2.0-2.0 |
| `presence_penalty` | Encourage new topics | -2.0-2.0 |

## Best Practices

1. **API Keys**: Never commit API keys to version control
2. **Error Handling**: Always handle API errors gracefully
3. **Token Management**: Monitor usage to control costs
4. **Prompt Engineering**: Clear, specific prompts get better results
5. **Memory**: Choose appropriate memory type for your use case
6. **Chunking**: Proper document chunking improves retrieval
7. **Caching**: Cache embeddings and responses when possible
8. **Testing**: Test with various inputs before production

## Useful Commands

```bash
# Install LangChain
pip install langchain langchain-openai

# Update dependencies
pip install --upgrade langchain

# Check version
python -c "import langchain; print(langchain.__version__)"
```

## Resources

- [LangChain Docs](https://python.langchain.com/)
- [API Reference](https://api.python.langchain.com/)
- [GitHub](https://github.com/langchain-ai/langchain)
- [Discord](https://discord.gg/langchain)

---

For full examples, see the demo folders in this repository!
