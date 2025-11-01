#!/bin/bash

# ==============================================================================
# Job Organizer (Reflex) - Stop Script
# ==============================================================================
# Gracefully stops both FastAPI backend and Reflex application
# ==============================================================================

# Colors
C_RESET='\033[0m'
C_GREEN='\033[0;32m'
C_BLUE='\033[0;34m'
C_RED='\033[0;31m'

print_info() {
    echo -e "${C_BLUE}[INFO]${C_RESET} $1"
}

print_success() {
    echo -e "${C_GREEN}[SUCCESS]${C_RESET} $1"
}

print_error() {
    echo -e "${C_RED}[ERROR]${C_RESET} $1"
}

echo ""
print_info "Stopping Job Organizer (Reflex Edition)..."
echo ""

# Stop FastAPI backend if it was started by start.sh
if [ -f /tmp/fastapi-backend.pid ]; then
    BACKEND_PID=$(cat /tmp/fastapi-backend.pid)
    print_info "Stopping FastAPI backend (PID: $BACKEND_PID)..."
    kill $BACKEND_PID 2>/dev/null
    rm /tmp/fastapi-backend.pid
    sleep 1
    print_success "FastAPI backend stopped"
else
    # Try to stop any uvicorn process on port 8000
    print_info "Checking for FastAPI backend..."
    if pgrep -f "uvicorn main:app" > /dev/null; then
        print_info "Stopping FastAPI backend..."
        pkill -f "uvicorn main:app" 2>/dev/null
        sleep 1
        print_success "FastAPI backend stopped"
    fi
fi

# Kill Reflex processes
print_info "Stopping Reflex processes..."
pkill -f "reflex run" 2>/dev/null
sleep 1

# Kill any remaining Node processes from Reflex
print_info "Stopping Node.js processes..."
pkill -f "node.*reflex" 2>/dev/null
sleep 1

# Free up ports if they're still in use
print_info "Freeing up ports..."
fuser -k 3000/tcp 2>/dev/null
fuser -k 8000/tcp 2>/dev/null
fuser -k 8001/tcp 2>/dev/null
sleep 1

# Check if processes are still running
if pgrep -f "reflex" > /dev/null; then
    print_error "Some Reflex processes are still running"
    print_info "Force killing remaining processes..."
    pkill -9 -f reflex 2>/dev/null
    sleep 1
    if pgrep -f "reflex" > /dev/null; then
        print_error "Failed to stop all processes"
    else
        print_success "All services stopped successfully"
    fi
else
    print_success "All services stopped successfully"
fi

echo ""
