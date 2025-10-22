# Demo 5: RAG System

## Overview
This demo demonstrates building a Retrieval Augmented Generation (RAG) system using LangChain.

## What You'll Learn
- How to create and split documents
- How to generate embeddings
- How to use vector stores (ChromaDB)
- How to build a retrieval-based QA system
- How RAG improves LLM responses with context

## Running the Demo
```bash
python rag_demo.py
```

## Key Concepts
- **RAG**: Retrieval Augmented Generation
- **Embeddings**: Numerical representations of text
- **Vector Store**: Database for storing and searching embeddings
- **Retriever**: Component that fetches relevant documents
- **QA Chain**: Question-answering chain with retrieval

## How It Works
1. Documents are split into chunks
2. Chunks are converted to embeddings
3. Embeddings are stored in a vector database
4. When queried, relevant chunks are retrieved
5. Retrieved context is used to generate answers
