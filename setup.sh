#!/bin/bash
# Setup script for GenAI Course
# This script helps set up the local development environment

echo "🚀 Setting up GenAI Course Environment"
echo "=================================="

# Check if Python is installed
if command -v python3 &> /dev/null; then
    echo "✅ Python3 is installed"
    python3 --version
else
    echo "❌ Python3 is not installed. Please install Python3 to use image generation features."
    echo "   Visit: https://www.python.org/downloads/"
fi

# Check if pip is available
if command -v pip3 &> /dev/null || command -v pip &> /dev/null; then
    echo "✅ pip is available"
    
    # Install Python dependencies
    echo ""
    echo "📦 Installing Python dependencies..."
    
    if command -v pip3 &> /dev/null; then
        pip3 install -r requirements.txt --user
    else
        pip install -r requirements.txt --user
    fi
    
    if [ $? -eq 0 ]; then
        echo "✅ Python dependencies installed successfully"
    else
        echo "⚠️  Some dependencies might not have installed correctly"
    fi
else
    echo "❌ pip is not available. Python package installation skipped."
fi

# Test the OG image generator
echo ""
echo "🖼️  Testing Open Graph image generator..."
if python3 create_og_image.py; then
    echo "✅ Open Graph image generator is working"
    if [ -f "og-image.png" ]; then
        echo "   Generated: og-image.png"
    fi
else
    echo "⚠️  Open Graph image generator test failed"
fi

# Check if we can open the course
echo ""
echo "🌐 Course Access Information"
echo "============================"
echo "To start the course:"
echo "1. Open index.html in your web browser"
echo "2. Or use a local server:"
echo "   - Python: python3 -m http.server 8000"
echo "   - Node.js: npx serve ."
echo "   - Live Server extension in VS Code"
echo ""
echo "📚 Course Files:"
echo "   - index.html         - Main course website"
echo "   - course-outline.md  - Weekly breakdown"
echo "   - course-syllabus.md - Detailed syllabus"
echo "   - README.md          - Project documentation"
echo ""
echo "🎯 Ready to start learning! Open index.html to begin."