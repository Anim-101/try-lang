#!/usr/bin/env python3
"""
Setup script for LangChain Learning Repository

This script helps set up the development environment.
"""

import os
import sys
import subprocess


def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
    return True


def check_venv():
    """Check if running in a virtual environment"""
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    if not in_venv:
        print("⚠️  Warning: Not running in a virtual environment")
        print("   It's recommended to use a virtual environment")
        response = input("   Continue anyway? (y/n): ")
        if response.lower() != 'y':
            return False
    else:
        print("✅ Running in virtual environment")
    return True


def install_dependencies():
    """Install required dependencies"""
    print("\n📦 Installing dependencies...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False


def setup_env_file():
    """Set up .env file"""
    if os.path.exists('.env'):
        print("\n✅ .env file already exists")
        return True
    
    if os.path.exists('.env.example'):
        print("\n📝 Setting up .env file...")
        with open('.env.example', 'r') as example:
            with open('.env', 'w') as env_file:
                env_file.write(example.read())
        print("✅ Created .env file from .env.example")
        print("⚠️  Please edit .env and add your API keys")
        return True
    else:
        print("❌ .env.example not found")
        return False


def main():
    """Main setup function"""
    print("=" * 50)
    print("LangChain Learning Repository - Setup")
    print("=" * 50)
    print()
    
    # Check Python version
    if not check_python_version():
        return
    
    # Check virtual environment
    if not check_venv():
        return
    
    # Install dependencies
    if not install_dependencies():
        return
    
    # Setup .env file
    setup_env_file()
    
    print("\n" + "=" * 50)
    print("✨ Setup Complete!")
    print("=" * 50)
    print()
    print("Next steps:")
    print("1. Edit .env and add your OpenAI API key")
    print("2. Run a demo: cd demos/01_basic_llm && python example.py")
    print("3. Follow the learning path in README.md")
    print()


if __name__ == "__main__":
    main()
