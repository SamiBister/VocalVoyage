#!/bin/zsh

# Check if widdershins is installed
if ! command -v widdershins &> /dev/null; then
    echo "Installing widdershins..."
    npm install -g widdershins
fi

# Create necessary directories
mkdir -p docs/backend/html docs/backend/diagrams docs/backend/api

# Generate API documentation with pdoc
echo "Generating API documentation..."
uv run pdoc --html --output-dir docs/backend/html app --force

# Generate diagrams with pyreverse
echo "Generating class diagrams..."
uv run pyreverse -o mmd -p vocabvoyage app.domain app.interfaces app.use_cases app.main --output-directory docs/backend/diagrams
uv run pyreverse -o html -p vocabvoyage app.domain app.interfaces app.use_cases app.main --output-directory docs/backend/diagrams
uv run pyreverse -o png -p vocabvoyage app.domain app.interfaces app.use_cases app.main --output-directory docs/backend/diagrams

# Start uvicorn server
echo "Starting uvicorn server..."
uv run uvicorn app.main:app --reload &

# Wait for server to start
sleep 10

# Generate OpenAPI documentation
echo "Generating OpenAPI documentation..."
curl http://localhost:8000/openapi.json -o docs/backend/api/openapi.json
widdershins docs/backend/api/openapi.json -o docs/backend/api/api-docs.md

# Kill uvicorn server
lsof -ti :8000 | xargs kill

# Generate frontend documentation
echo "Generating frontend documentation..."
cd frontend
npm run docs

echo "Documentation generation complete!"