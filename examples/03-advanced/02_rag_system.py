"""
02_rag_system.py
Retrieval Augmented Generation - Combining document retrieval with LLM generation
"""

import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Sample knowledge base
KNOWLEDGE_BASE = [
    {
        "id": "doc1",
        "title": "LangChain Basics",
        "content": "LangChain is a framework for developing applications powered by language models. It provides modular components like LLMs, prompts, chains, agents, and memory systems."
    },
    {
        "id": "doc2", 
        "title": "Prompt Engineering",
        "content": "Prompt engineering is the practice of designing and optimizing prompts to get better results from language models. Key techniques include few-shot learning, chain-of-thought prompting, and role-based prompts."
    },
    {
        "id": "doc3",
        "title": "Vector Databases",
        "content": "Vector databases store and retrieve data based on vector embeddings. They enable semantic search by finding documents with similar meaning rather than exact keyword matches."
    },
    {
        "id": "doc4",
        "title": "RAG Systems",
        "content": "Retrieval Augmented Generation (RAG) combines information retrieval with text generation. It first retrieves relevant documents, then uses them as context for generating responses."
    },
    {
        "id": "doc5",
        "title": "LangChain Agents",
        "content": "LangChain agents are systems that use LLMs to decide what actions to take. They can use tools, make API calls, and chain multiple operations together autonomously."
    }
]

class SimpleVectorStore:
    """Simple vector store implementation for demonstration"""
    
    def __init__(self):
        self.documents = []
        
    def add_documents(self, docs):
        """Add documents to the store"""
        self.documents.extend(docs)
        print(f"✅ Added {len(docs)} documents to vector store")
    
    def similarity_search(self, query, k=3):
        """Simple keyword-based search (in real implementation, use embeddings)"""
        query_words = query.lower().split()
        
        # Score documents based on keyword overlap
        scored_docs = []
        for doc in self.documents:
            content_words = doc['content'].lower().split()
            title_words = doc['title'].lower().split()
            
            # Count overlapping words
            content_overlap = len(set(query_words) & set(content_words))
            title_overlap = len(set(query_words) & set(title_words)) * 2  # Weight title higher
            
            total_score = content_overlap + title_overlap
            
            if total_score > 0:
                scored_docs.append((doc, total_score))
        
        # Sort by score and return top k
        scored_docs.sort(key=lambda x: x[1], reverse=True)
        return [doc for doc, score in scored_docs[:k]]

class SimpleRAG:
    """Simple RAG implementation"""
    
    def __init__(self, llm, vector_store):
        self.llm = llm
        self.vector_store = vector_store
        
        # RAG prompt template
        self.prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""Use the following pieces of context to answer the question. 
If you don't know the answer based on the context, say that you don't know.

Context:
{context}
Question: {question}

Answer:"""
        )
    
    def query(self, question):
        """Query the RAG system"""
        # 1. Retrieve relevant documents
        relevant_docs = self.vector_store.similarity_search(question, k=2)
        
        # 2. Prepare context
        context = "\n\n".join([f"Document {i+1}: {doc['content']}" 
                              for i, doc in enumerate(relevant_docs)])
        
        # 3. Generate response
        prompt_input = self.prompt.format(context=context, question=question)
        response = self.llm.invoke(prompt_input)
        
        return {
            "answer": response.strip(),
            "sources": [doc['title'] for doc in relevant_docs],
            "retrieved_docs": relevant_docs
        }

def rag_demo():
    """Demonstrate RAG system"""
    print("🔍 RAG System Demo")
    print("=" * 20)
    
    # Setup components
    llm = OpenAI(temperature=0.3)
    vector_store = SimpleVectorStore()
    vector_store.add_documents(KNOWLEDGE_BASE)
    
    # Create RAG system
    rag = SimpleRAG(llm, vector_store)
    
    # Test questions
    questions = [
        "What is LangChain?",
        "How do RAG systems work?",
        "What are LangChain agents?",
        "Tell me about prompt engineering techniques",
        "What is the weather like today?"  # Should say "don't know"
    ]
    
    for i, question in enumerate(questions, 1):
        print(f"\n--- Question {i} ---")
        print(f"❓ {question}")
        
        try:
            result = rag.query(question)
            
            print(f"📖 Sources: {', '.join(result['sources'])}")
            print(f"💬 Answer: {result['answer'][:200]}...")
            
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    """
    Run RAG system demonstration
    """
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Please set your OPENAI_API_KEY in .env file")
        return
    
    try:
        rag_demo()
        
        print("\n✅ RAG demonstration completed!")
        print("\n💡 RAG System Components:")
        print("   📚 Knowledge Base: Collection of documents")
        print("   🔍 Retriever: Finds relevant documents")
        print("   🤖 Generator: LLM that creates responses")
        print("   📊 Vector Store: Stores document embeddings")
        print("   🎯 Prompt: Combines context and question")
        
        print("\n🚀 Next Steps:")
        print("   - Try with real embeddings (OpenAI, Hugging Face)")
        print("   - Use proper vector databases (Chroma, Pinecone)")
        print("   - Add document chunking and preprocessing")
        print("   - Implement advanced retrieval strategies")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
