#!/bin/bash

# Discord AI Server Setup Bot - Quick Start Script

set -e

echo "🤖 Discord AI Server Setup Bot"
echo "================================"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "❌ Error: .env file not found!"
    echo ""
    echo "Please create a .env file with your Discord bot token:"
    echo "  cp .env.example .env"
    echo "  nano .env  # or use your preferred editor"
    echo ""
    exit 1
fi

# Check if running in Docker or native Python
if command -v docker &> /dev/null && [ "$1" == "docker" ]; then
    echo "🐳 Running with Docker..."
    docker-compose up --build
else
    echo "🐍 Running with Python..."
    
    # Check if virtual environment exists
    if [ ! -d "venv" ]; then
        echo "Creating virtual environment..."
        python3 -m venv venv
    fi
    
    # Activate virtual environment
    source venv/bin/activate
    
    # Install dependencies
    echo "Installing dependencies..."
    pip install -q -r requirements.txt
    
    # Run the bot
    echo ""
    echo "✅ Starting bot..."
    echo "================================"
    echo ""
    python setup_bot.py
fi
