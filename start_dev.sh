#!/bin/zsh

# Navigate to the project root directory
# cd "$(dirname "$0")"

# Activate Python virtual environment
# source .venv/bin/activate

# Start the backend server
echo "Starting backend server..."
uv run uvicorn app.main:app --reload &

# Save the PID of the backend server
BACKEND_PID=$!

# Navigate to the frontend directory
cd frontend

# Start the frontend server
echo "Starting frontend server..."
npm run dev

# Wait for the frontend server to exit
wait

# When done, kill the backend server
lsof -ti :8000 | xargs kill
