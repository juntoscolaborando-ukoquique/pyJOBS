#!/bin/bash

# ==============================================================================
# Job Organizer (Reflex) - Startup Script
# ==============================================================================
# Starts both the FastAPI backend and Reflex frontend
# ==============================================================================

# Colors
C_RESET='\033[0m'
C_GREEN='\033[0;32m'
C_BLUE='\033[0;34m'
C_YELLOW='\033[0;33m'

print_info() {
    echo -e "${C_BLUE}[INFO]${C_RESET} $1"
}

print_success() {
    echo -e "${C_GREEN}[SUCCESS]${C_RESET} $1"
}

print_warning() {
    echo -e "${C_YELLOW}[WARNING]${C_RESET} $1"
}

echo ""
print_info "Starting Job Organizer (Reflex Edition)..."
echo ""

# Check if reflex is installed
if ! command -v reflex &> /dev/null; then
    echo "Error: Reflex is not installed."
    echo "Please install it with: pip install reflex"
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "rxconfig.py" ]; then
    echo "Error: rxconfig.py not found."
    echo "Please run this script from the project root directory."
    exit 1
fi

# Initialize Reflex if needed (first time setup)
if [ ! -d ".web" ]; then
    print_info "First time setup - initializing Reflex..."
    reflex init
fi

# Check if FastAPI backend is running
print_info "Checking FastAPI backend status..."
if curl -s http://localhost:8000/api/stats > /dev/null 2>&1; then
    print_success "FastAPI backend is already running on port 8000"
else
    print_warning "FastAPI backend not detected on port 8000"
    
    # Try to find and start the backend
    BACKEND_DIR="/root/ORGANIZER-Python/Organiz_Py-00/backend"
    
    if [ -d "$BACKEND_DIR" ]; then
        print_info "Found backend at: $BACKEND_DIR"
        print_info "Starting FastAPI backend..."
        
        # Start backend in background
        cd "$BACKEND_DIR"
        
        # Check if using relative import (needs fixing)
        if grep -q "from \.app\.main import app" main.py 2>/dev/null; then
            print_info "Fixing backend import statement..."
            sed -i 's/from \.app\.main import app/from app.main import app/' main.py
        fi
        
        nohup uvicorn main:app --host 0.0.0.0 --port 8000 --reload > /tmp/fastapi-backend.log 2>&1 &
        BACKEND_PID=$!
        
        # Wait a moment for backend to start
        sleep 3
        
        # Check if backend started successfully
        if curl -s http://localhost:8000/api/stats > /dev/null 2>&1; then
            print_success "FastAPI backend started successfully (PID: $BACKEND_PID)"
            echo "$BACKEND_PID" > /tmp/fastapi-backend.pid
        else
            print_warning "Backend may not have started correctly. Check logs: /tmp/fastapi-backend.log"
        fi
        
        # Return to original directory
        cd - > /dev/null
    else
        print_warning "Backend directory not found at: $BACKEND_DIR"
        print_warning "Please start the FastAPI backend manually:"
        echo "  cd /path/to/backend"
        echo "  uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"
        echo ""
    fi
fi

# Start the Reflex app
print_info "Starting Reflex application..."
echo ""
print_success "Reflex is starting up..."
echo ""
echo "  🗄️  FastAPI Backend: http://localhost:8000"
echo "  📱 Frontend: http://localhost:3000"
echo "  🔧 Reflex Backend: http://localhost:8001"
echo ""
echo "  Press Ctrl+C to stop the server"
echo ""

reflex run
