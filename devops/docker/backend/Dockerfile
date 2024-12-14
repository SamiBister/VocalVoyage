# Install uv
FROM python:3.13-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Change the working directory to the `app` directory
WORKDIR /app

COPY pyproject.toml uv.lock README.md ./
COPY ./app ./app

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-editable --no-dev


FROM python:3.13-slim

# Create app user
RUN groupadd -r app && \
    useradd -r -g app app && \
    mkdir -p /app && \
    chown app:app /app

WORKDIR /app

# Expose port 8000
EXPOSE 8000

# Copy from builder
COPY --from=builder /app /app

# Run the application
CMD ["/app/.venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]