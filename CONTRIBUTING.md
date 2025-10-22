# Contributing to LangChain Learning Repository

Thank you for your interest in contributing to this learning repository! 🎉

## How to Contribute

### Adding New Demos

If you'd like to add a new demo:

1. Create a new folder in `demos/` with a descriptive name
2. Include:
   - `README.md` - Explanation of concepts
   - `example.py` - Runnable example code
   - Clear comments in the code
3. Follow the existing demo structure and style
4. Update the main README.md with your demo

### Improving Existing Demos

- Fix bugs or typos
- Improve explanations
- Add more examples
- Enhance code comments
- Update dependencies

### Documentation

- Improve README files
- Add troubleshooting guides
- Create tutorials
- Fix documentation errors

## Code Style

- Follow PEP 8 for Python code
- Use clear, descriptive variable names
- Add docstrings to functions
- Keep code simple and educational
- Comment complex logic

## Demo Guidelines

Each demo should:

1. **Be Self-Contained**: Work independently of other demos
2. **Be Educational**: Focus on teaching, not just showing
3. **Include Examples**: Multiple examples showing different aspects
4. **Have Clear Output**: Print informative messages
5. **Handle Errors**: Check for API keys, handle exceptions
6. **Be Documented**: Both in README and code comments

## Example Demo Structure

```python
"""
Demo X: [Topic Name]

Brief description of what this demo teaches.
"""

import os
from dotenv import load_dotenv
# Other imports

load_dotenv()


def example_1():
    """Clear description of this example"""
    print("💬 Example 1: [Name]")
    print("-" * 50)
    
    # Code with comments
    # ...
    
    print()


def main():
    """Run all examples"""
    print("=" * 50)
    print("Demo X: [Topic]")
    print("=" * 50)
    print()
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found")
        return
    
    example_1()
    # Other examples...
    
    print("✨ Demo Complete!")


if __name__ == "__main__":
    main()
```

## Pull Request Process

1. Fork the repository
2. Create a branch for your changes
3. Make your changes
4. Test your changes thoroughly
5. Submit a pull request with a clear description

## Questions?

Feel free to open an issue for:
- Questions about the demos
- Suggestions for improvements
- Bug reports
- New demo ideas

## Code of Conduct

- Be respectful and constructive
- Help others learn
- Share knowledge generously
- Give credit where due

Thank you for helping make this learning resource better! 🙏
