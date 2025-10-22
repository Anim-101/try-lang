"""
Utility functions for LangChain demos

This module contains helper functions used across different demos.
"""

import os
from typing import List, Dict, Any


def check_api_key() -> bool:
    """
    Check if OpenAI API key is configured
    
    Returns:
        bool: True if API key is set, False otherwise
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not found in environment variables")
        print("Please create a .env file with your API key")
        return False
    return True


def print_section(title: str, width: int = 50) -> None:
    """
    Print a formatted section header
    
    Args:
        title: The section title
        width: Width of the separator line
    """
    print()
    print("=" * width)
    print(title)
    print("=" * width)
    print()


def print_subsection(title: str, width: int = 50) -> None:
    """
    Print a formatted subsection header
    
    Args:
        title: The subsection title
        width: Width of the separator line
    """
    print()
    print(title)
    print("-" * width)
    print()


def format_response(response: Any) -> str:
    """
    Format an LLM response for display
    
    Args:
        response: The response object from LLM
    
    Returns:
        str: Formatted response content
    """
    if hasattr(response, 'content'):
        return response.content
    return str(response)


def count_tokens(text: str) -> int:
    """
    Rough estimate of token count (approximation)
    
    Args:
        text: The text to count tokens for
    
    Returns:
        int: Approximate token count
    """
    # Rough approximation: ~4 characters per token
    return len(text) // 4


def truncate_text(text: str, max_length: int = 100) -> str:
    """
    Truncate text to specified length
    
    Args:
        text: The text to truncate
        max_length: Maximum length
    
    Returns:
        str: Truncated text with ellipsis if needed
    """
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."


def display_sources(sources: List[Dict[str, Any]]) -> None:
    """
    Display source documents in a formatted way
    
    Args:
        sources: List of source documents
    """
    print("\n📚 Sources:")
    for i, source in enumerate(sources, 1):
        print(f"\n{i}. {source.get('metadata', {}).get('source', 'Unknown source')}")
        content = source.get('page_content', '')
        print(f"   {truncate_text(content, 100)}")


def create_demo_header(demo_number: int, demo_name: str) -> None:
    """
    Create a consistent header for demos
    
    Args:
        demo_number: The demo number
        demo_name: The name of the demo
    """
    print_section(f"Demo {demo_number}: {demo_name}")
    print("🚀 Starting demo...")
    print()


def create_demo_footer(demo_number: int) -> None:
    """
    Create a consistent footer for demos
    
    Args:
        demo_number: The demo number
    """
    print()
    print_section("✨ Demo Complete!")
    print(f"📚 Demo {demo_number} finished successfully!")
    print()
