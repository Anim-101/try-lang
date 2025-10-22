#!/bin/bash

# Setup script for LangChain Demo Projects
# This script helps set up the environment for running the demos

set -e

echo "======================================"
echo "LangChain Demo Projects - Setup"
echo "======================================"
echo ""

# Check Python version
echo "Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "Found Python version: $PYTHON_VERSION"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
if [ -d "venv" ]; then
    echo "Virtual environment already exists. Skipping creation."
else
    python3 -m venv venv
    echo "Virtual environment created successfully!"
fi
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "Virtual environment activated!"
echo ""

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip --quiet
echo "pip upgraded!"
echo ""

# Install requirements
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Dependencies installed successfully!"
echo ""

# Setup .env file
echo "Setting up environment variables..."
if [ -f ".env" ]; then
    echo ".env file already exists. Skipping creation."
else
    cp .env.example .env
    echo ".env file created from .env.example"
    echo ""
    echo "⚠️  IMPORTANT: Please edit .env and add your API keys!"
fi
echo ""

echo "======================================"
echo "Setup Complete! 🎉"
echo "======================================"
echo ""
echo "Next steps:"
echo "1. Edit .env and add your OpenAI API key"
echo "2. Activate the virtual environment: source venv/bin/activate"
echo "3. Run your first demo: cd demos/01-basic-llm-chains && python basic_chain.py"
echo ""
echo "For more details, see QUICKSTART.md"
echo ""
