"""
Demo 5: RAG System (Retrieval Augmented Generation)
This demo shows how to build a simple RAG system using LangChain.
"""

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def create_sample_documents():
    """Create sample documents for the demo"""
    documents = [
        Document(
            page_content="LangChain is a framework for developing applications powered by language models.",
            metadata={"source": "langchain_intro"}
        ),
        Document(
            page_content="RAG stands for Retrieval Augmented Generation. It combines retrieval of relevant documents with generation.",
            metadata={"source": "rag_concept"}
        ),
        Document(
            page_content="Vector databases store embeddings and enable semantic search for similar content.",
            metadata={"source": "vector_db"}
        ),
        Document(
            page_content="Python is a popular programming language used for AI and machine learning applications.",
            metadata={"source": "python_info"}
        ),
        Document(
            page_content="Embeddings are numerical representations of text that capture semantic meaning.",
            metadata={"source": "embeddings"}
        )
    ]
    return documents


def rag_demo():
    """Demo using RAG with vector store"""
    print("=== RAG System Demo ===\n")
    
    # Create sample documents
    documents = create_sample_documents()
    print(f"Created {len(documents)} sample documents\n")
    
    # Split documents (not necessary for our small docs, but shown for completeness)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    splits = text_splitter.split_documents(documents)
    print(f"Split into {len(splits)} chunks\n")
    
    # Create embeddings and vector store
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings
    )
    print("Created vector store\n")
    
    # Create retriever
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
    
    # Create QA chain
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        verbose=True
    )
    
    # Ask questions
    queries = [
        "What is RAG?",
        "What is LangChain?",
        "Tell me about embeddings"
    ]
    
    for query in queries:
        print(f"\nQuery: {query}")
        print("-" * 50)
        result = qa_chain({"query": query})
        print(f"Answer: {result['result']}\n")
        print("Source documents:")
        for i, doc in enumerate(result['source_documents']):
            print(f"  {i+1}. {doc.metadata['source']}")
        print("\n" + "="*50 + "\n")


def main():
    """Run RAG demo"""
    rag_demo()


if __name__ == "__main__":
    main()
