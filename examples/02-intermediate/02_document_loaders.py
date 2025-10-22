"""
02_document_loaders.py
Loading and Processing Documents - Working with different file types
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Text content for demonstration
SAMPLE_TEXT = """
LangChain is a framework for developing applications powered by language models. 
It provides several key components:

1. LLMs and Chat Models: Interfaces to language models
2. Prompt Templates: Dynamic prompt creation
3. Chains: Sequences of calls to models and utilities
4. Agents: Systems that use LLMs to decide actions
5. Memory: Maintaining state between chain/agent calls
6. Document Loaders: Loading documents from various sources

LangChain enables developers to build context-aware and reasoning applications
that can connect language models to other sources of data and computation.
"""

def text_loader_demo():
    """
    Demonstrate loading text from strings and files
    """
    print("📄 Text Loader Demo")
    print("=" * 25)
    
    # Create a sample text file
    sample_file = "/tmp/langchain_sample.txt"
    with open(sample_file, "w") as f:
        f.write(SAMPLE_TEXT)
    
    print(f"✅ Created sample file: {sample_file}")
    print(f"📊 File size: {len(SAMPLE_TEXT)} characters")
    
    # Load from file
    with open(sample_file, "r") as f:
        content = f.read()
    
    print(f"📖 Loaded content preview:")
    print(content[:200] + "...")
    
    return content

def csv_loader_demo():
    """
    Demonstrate loading CSV data
    """
    print("\n📊 CSV Loader Demo")
    print("=" * 22)
    
    # Create sample CSV
    csv_content = """name,age,occupation,location
Alice,28,Engineer,San Francisco
Bob,34,Teacher,New York
Charlie,22,Student,Boston
Diana,31,Doctor,Chicago
Eve,27,Designer,Seattle"""
    
    csv_file = "/tmp/sample_data.csv"
    with open(csv_file, "w") as f:
        f.write(csv_content)
    
    print(f"✅ Created CSV file: {csv_file}")
    
    # Load and parse CSV
    import csv
    data = []
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    
    print(f"📊 Loaded {len(data)} records:")
    for record in data[:3]:  # Show first 3
        print(f"   {record['name']}: {record['occupation']} in {record['location']}")
    
    return data

def web_content_demo():
    """
    Simulate loading web content
    """
    print("\n🌐 Web Content Demo")
    print("=" * 25)
    
    # Simulate web content (in real scenario, use requests or langchain web loaders)
    web_content = """
    <html>
    <head><title>LangChain Tutorial</title></head>
    <body>
        <h1>Getting Started with LangChain</h1>
        <p>LangChain is a powerful framework for building AI applications.</p>
        <h2>Key Features</h2>
        <ul>
            <li>Easy integration with LLMs</li>
            <li>Modular design</li>
            <li>Rich ecosystem of tools</li>
        </ul>
    </body>
    </html>
    """
    
    # Simple HTML text extraction (in real scenario, use BeautifulSoup)
    import re
    
    # Remove HTML tags
    clean_text = re.sub(r'<[^>]+>', '', web_content)
    # Clean up whitespace
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    
    print("🧹 Extracted text from HTML:")
    print(clean_text)
    
    return clean_text

def directory_loader_demo():
    """
    Demonstrate loading multiple files from a directory
    """
    print("\n📁 Directory Loader Demo")
    print("=" * 30)
    
    # Create sample directory structure
    import tempfile
    import shutil
    
    temp_dir = tempfile.mkdtemp()
    print(f"📂 Created temp directory: {temp_dir}")
    
    # Create sample files
    files_content = {
        "doc1.txt": "This is the first document about Python programming.",
        "doc2.txt": "This is the second document about machine learning.",
        "doc3.txt": "This is the third document about web development.",
        "readme.md": "# Project README\n\nThis project demonstrates document loading."
    }
    
    loaded_docs = []
    for filename, content in files_content.items():
        filepath = os.path.join(temp_dir, filename)
        with open(filepath, "w") as f:
            f.write(content)
        
        # Load document
        loaded_docs.append({
            "filename": filename,
            "content": content,
            "path": filepath
        })
    
    print(f"📄 Loaded {len(loaded_docs)} documents:")
    for doc in loaded_docs:
        print(f"   📝 {doc['filename']}: {len(doc['content'])} chars")
    
    # Cleanup
    shutil.rmtree(temp_dir)
    print("🧹 Cleaned up temp directory")
    
    return loaded_docs

def main():
    """
    Demonstrate different document loaders
    """
    
    print("📚 Document Loaders Demo")
    print("=" * 30)
    
    try:
        # 1. Text loading
        text_content = text_loader_demo()
        
        # 2. CSV loading  
        csv_data = csv_loader_demo()
        
        # 3. Web content
        web_text = web_content_demo()
        
        # 4. Directory loading
        directory_docs = directory_loader_demo()
        
        print("\n✅ Document loading demonstrations completed!")
        print("\n💡 Document Loader Types:")
        print("   📄 TextLoader: Plain text files")
        print("   📊 CSVLoader: Structured data")
        print("   🌐 WebBaseLoader: Web pages")
        print("   📁 DirectoryLoader: Multiple files")
        print("   📄 PDFLoader: PDF documents")
        print("   📊 UnstructuredLoader: Various formats")
        
        print(f"\n📊 Summary:")
        print(f"   Text content: {len(text_content)} chars")
        print(f"   CSV records: {len(csv_data)} rows")
        print(f"   Web content: {len(web_text)} chars")
        print(f"   Directory docs: {len(directory_docs)} files")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()