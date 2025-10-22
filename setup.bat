@echo off
REM Setup script for LangChain Demo Projects (Windows)
REM This script helps set up the environment for running the demos

echo ======================================
echo LangChain Demo Projects - Setup
echo ======================================
echo.

REM Check Python version
echo Checking Python version...
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed. Please install Python 3.8 or higher.
    exit /b 1
)

python --version
echo.

REM Create virtual environment
echo Creating virtual environment...
if exist venv (
    echo Virtual environment already exists. Skipping creation.
) else (
    python -m venv venv
    echo Virtual environment created successfully!
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo Virtual environment activated!
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip --quiet
echo pip upgraded!
echo.

REM Install requirements
echo Installing dependencies...
pip install -r requirements.txt
echo Dependencies installed successfully!
echo.

REM Setup .env file
echo Setting up environment variables...
if exist .env (
    echo .env file already exists. Skipping creation.
) else (
    copy .env.example .env
    echo .env file created from .env.example
    echo.
    echo WARNING: Please edit .env and add your API keys!
)
echo.

echo ======================================
echo Setup Complete!
echo ======================================
echo.
echo Next steps:
echo 1. Edit .env and add your OpenAI API key
echo 2. Activate the virtual environment: venv\Scripts\activate
echo 3. Run your first demo: cd demos\01-basic-llm-chains ^&^& python basic_chain.py
echo.
echo For more details, see QUICKSTART.md
echo.

pause
