#!/usr/bin/env fish

# Navigate to the project root directory
#cd (dirname (status --current-filename))

# Activate Python virtual environment
# source .venv/bin/activate.fish

# Start the backend server
echo "Starting backend server..."
uv run uvicorn app.main:app --reload &

# Save the PID of the backend server
set BACKEND_PID $last_pid

# Navigate to the frontend directory
cd frontend

# Start the frontend server
echo "Starting frontend server..."
npm run dev

# Wait for the frontend server to exit
wait

# When done, kill the backend server
kill $BACKEND_PID
