# Contributing to LangChain Demo Projects

Thank you for your interest in contributing to this LangChain learning repository!

## How to Contribute

### Adding New Demos

1. **Choose a Topic**: Select a LangChain concept not yet covered
2. **Create Directory**: Follow the naming convention `demos/XX-topic-name/`
3. **Write Demo Code**: Create well-commented, runnable examples
4. **Add Documentation**: Include a comprehensive README.md
5. **Test Thoroughly**: Ensure the demo works as expected
6. **Update Main README**: Add your demo to the learning path

### Demo Structure

Each demo should include:
```
demos/XX-topic-name/
├── README.md           # Explanation and key concepts
└── demo_script.py      # Runnable code with comments
```

### Code Style

- Follow PEP 8 Python style guide
- Include type hints where helpful
- Add docstrings to functions
- Keep code simple and readable
- Comment complex sections

### Documentation Style

Each README.md should include:
- **Overview**: Brief description
- **What You'll Learn**: Key takeaways
- **Running the Demo**: How to execute
- **Key Concepts**: Important terms explained

### Example Demo Template

```python
"""
Demo X: [Topic Name]
This demo shows [brief description].
"""

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def main():
    """Run [topic] demo"""
    # Your demo code here
    pass


if __name__ == "__main__":
    main()
```

### Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-demo`
3. Make your changes
4. Test your demo
5. Commit with clear messages
6. Push to your fork
7. Create a Pull Request

### Commit Message Guidelines

- Use present tense: "Add demo" not "Added demo"
- Be descriptive but concise
- Reference issues if applicable

### Testing Your Demo

Before submitting:
- [ ] Demo runs without errors
- [ ] All dependencies in requirements.txt
- [ ] Documentation is clear
- [ ] Code is well-commented
- [ ] Follows existing patterns

### Ideas for New Demos

Potential topics:
- Streaming responses
- Custom chains
- Output parsers
- Multi-agent systems
- LangChain Expression Language (LCEL)
- Document loaders
- Custom embeddings
- Callbacks and monitoring
- LangServe deployment

## Questions?

Feel free to open an issue for:
- Clarification on existing demos
- Suggestions for improvements
- Ideas for new demos
- Bug reports

## Code of Conduct

- Be respectful and constructive
- Help others learn
- Keep discussions focused
- Share knowledge generously

Thank you for contributing! 🙌
