"""
Demo 5: Document Q&A with Embeddings

This script demonstrates how to build a Q&A system over documents
using embeddings and vector stores.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document
from langchain.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()


def create_sample_documents():
    """Create sample documents for demonstration"""
    
    documents = [
        Document(
            page_content="""
            LangChain is a framework for developing applications powered by language models.
            It provides tools for prompt management, chains, memory, agents, and more.
            LangChain makes it easy to build LLM-powered applications.
            """,
            metadata={"source": "langchain_intro.txt", "topic": "overview"}
        ),
        Document(
            page_content="""
            Embeddings are vector representations of text. They capture semantic meaning
            and allow for similarity search. OpenAI provides embeddings through their API.
            Embeddings are crucial for building search and Q&A systems.
            """,
            metadata={"source": "embeddings_guide.txt", "topic": "embeddings"}
        ),
        Document(
            page_content="""
            Vector stores like Chroma, Pinecone, and FAISS allow you to store and search
            embeddings efficiently. They enable semantic search by finding similar vectors.
            Vector databases are essential for RAG (Retrieval Augmented Generation) systems.
            """,
            metadata={"source": "vector_stores.txt", "topic": "vector_stores"}
        ),
        Document(
            page_content="""
            Agents in LangChain can use tools to accomplish tasks. They can reason about
            which tools to use and in what order. Agents enable autonomous behavior in
            LLM applications. Common tools include search, calculators, and APIs.
            """,
            metadata={"source": "agents_overview.txt", "topic": "agents"}
        ),
        Document(
            page_content="""
            Memory in LangChain allows conversations to maintain context. Types include
            ConversationBufferMemory, ConversationSummaryMemory, and more. Memory is
            essential for building chatbots and stateful applications.
            """,
            metadata={"source": "memory_guide.txt", "topic": "memory"}
        )
    ]
    
    return documents


def example_text_splitting():
    """Demonstrates document splitting"""
    
    print("💬 Example 1: Text Splitting")
    print("-" * 50)
    
    # Create a long document
    long_text = """
    LangChain is a powerful framework for building LLM applications. It provides many
    components including chains, agents, memory, and more. When working with long documents,
    it's important to split them into chunks. This allows for better retrieval and ensures
    that we don't exceed token limits. The RecursiveCharacterTextSplitter is a good choice
    for most use cases as it tries to keep related text together.
    """
    
    # Create text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,  # Maximum chunk size
        chunk_overlap=20,  # Overlap between chunks
        length_function=len
    )
    
    # Split the text
    chunks = text_splitter.split_text(long_text)
    
    print(f"Original text length: {len(long_text)} characters")
    print(f"Number of chunks: {len(chunks)}")
    print()
    
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}:")
        print(chunk.strip())
        print()


def example_embeddings_creation():
    """Demonstrates creating embeddings"""
    
    print("💬 Example 2: Creating Embeddings")
    print("-" * 50)
    
    # Initialize embeddings
    embeddings = OpenAIEmbeddings()
    
    # Create embeddings for sample texts
    texts = [
        "LangChain is a framework for LLM applications",
        "Python is a programming language",
        "LangChain helps build AI applications"
    ]
    
    print("Creating embeddings for sample texts...")
    print()
    
    # Get embeddings
    text_embeddings = embeddings.embed_documents(texts)
    
    print(f"Number of texts: {len(texts)}")
    print(f"Embedding dimension: {len(text_embeddings[0])}")
    print()
    
    # Show first few values of first embedding
    print(f"First embedding (first 5 values): {text_embeddings[0][:5]}")
    print()
    
    # Embed a query
    query = "What is LangChain?"
    query_embedding = embeddings.embed_query(query)
    print(f"Query: '{query}'")
    print(f"Query embedding (first 5 values): {query_embedding[:5]}")
    print()


def example_vector_store():
    """Demonstrates using vector store"""
    
    print("💬 Example 3: Vector Store with Chroma")
    print("-" * 50)
    
    # Create sample documents
    documents = create_sample_documents()
    
    # Initialize embeddings
    embeddings = OpenAIEmbeddings()
    
    print("Creating vector store from documents...")
    
    # Create vector store
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name="demo_collection"
    )
    
    print(f"✅ Vector store created with {len(documents)} documents")
    print()
    
    # Search for similar documents
    query = "Tell me about embeddings"
    print(f"Query: '{query}'")
    print()
    
    # Similarity search
    similar_docs = vectorstore.similarity_search(query, k=2)
    
    print(f"Found {len(similar_docs)} relevant documents:")
    print()
    
    for i, doc in enumerate(similar_docs):
        print(f"Document {i+1}:")
        print(f"Content: {doc.page_content.strip()}")
        print(f"Metadata: {doc.metadata}")
        print()


def example_qa_chain():
    """Demonstrates Q&A chain over documents"""
    
    print("💬 Example 4: Q&A Chain over Documents")
    print("-" * 50)
    
    # Create documents and vector store
    documents = create_sample_documents()
    embeddings = OpenAIEmbeddings()
    
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name="qa_demo"
    )
    
    # Create LLM
    llm = ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo")
    
    # Create Q&A chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",  # "stuff" puts all docs in context
        retriever=vectorstore.as_retriever(search_kwargs={"k": 2})
    )
    
    # Ask questions
    questions = [
        "What is LangChain?",
        "How do embeddings work?",
        "What are vector stores used for?",
        "Tell me about agents"
    ]
    
    print("Asking questions about the documents:")
    print()
    
    for question in questions:
        print(f"Q: {question}")
        answer = qa_chain.invoke({"query": question})
        print(f"A: {answer['result']}")
        print()


def example_qa_with_sources():
    """Demonstrates Q&A with source attribution"""
    
    print("💬 Example 5: Q&A with Source Citations")
    print("-" * 50)
    
    # Create documents and vector store
    documents = create_sample_documents()
    embeddings = OpenAIEmbeddings()
    
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name="qa_sources"
    )
    
    # Create LLM
    llm = ChatOpenAI(temperature=0.3)
    
    # Create Q&A chain that returns sources
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        return_source_documents=True
    )
    
    # Ask a question
    question = "What types of memory are available in LangChain?"
    print(f"Question: {question}")
    print()
    
    result = qa_chain.invoke({"query": question})
    
    print(f"Answer: {result['result']}")
    print()
    
    print("Sources:")
    for i, doc in enumerate(result['source_documents']):
        print(f"\n{i+1}. {doc.metadata['source']}")
        print(f"   {doc.page_content.strip()[:100]}...")


def example_custom_qa_prompt():
    """Demonstrates custom Q&A prompt"""
    
    print("💬 Example 6: Q&A with Custom Prompt")
    print("-" * 50)
    
    # Create documents and vector store
    documents = create_sample_documents()
    embeddings = OpenAIEmbeddings()
    
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name="custom_qa"
    )
    
    # Create LLM
    llm = ChatOpenAI(temperature=0.5)
    
    # Create custom prompt
    custom_prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful assistant answering questions about LangChain.
        Use the following context to answer the question. If you don't know the answer,
        say so - don't make up information.
        
        Context: {context}"""),
        ("human", "{question}")
    ])
    
    # Create Q&A chain with custom prompt
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": custom_prompt}
    )
    
    # Ask a question
    question = "How can I build a chatbot?"
    print(f"Question: {question}")
    print()
    
    answer = qa_chain.invoke({"query": question})
    print(f"Answer: {answer['result']}")
    print()


def main():
    """Run all document Q&A examples"""
    
    print("=" * 50)
    print("Demo 5: Document Q&A with Embeddings")
    print("=" * 50)
    print()
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found")
        return
    
    # Run all examples
    example_text_splitting()
    example_embeddings_creation()
    example_vector_store()
    example_qa_chain()
    example_qa_with_sources()
    example_custom_qa_prompt()
    
    print("=" * 50)
    print("✨ Demo Complete!")
    print("=" * 50)
    print()
    print("💡 Key Learnings:")
    print("   1. Documents must be split into chunks")
    print("   2. Embeddings capture semantic meaning")
    print("   3. Vector stores enable fast similarity search")
    print("   4. RetrievalQA chains answer questions from docs")
    print("   5. Source attribution builds trust")
    print("   6. Custom prompts improve responses")
    print()
    print("📚 Next: Demo 6 - Agents and Tools")
    print()


if __name__ == "__main__":
    main()
