# python:3.13-slim
ARG IMAGE=sha256:73b10ec18665ab5fb450c3118f76406ba3384f36af9bea43a55a482a8bf287a8 
FROM $IMAGE AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Change the working directory to the `app` directory
WORKDIR /app

COPY pyproject.toml uv.lock README.md ./
COPY ./app ./app

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-editable --no-dev


FROM $IMAGE as runner

# Create app user
RUN groupadd -r app && \
    useradd -r -g app app && \
    mkdir -p /app && \
    chown app:app /app

WORKDIR /app

# Copy the application and Python packages
COPY  --chown=app:app  --from=builder /app /app

# Expose port 8000
EXPOSE 8000

# # Copy from builder
# COPY --from=builder /app /app

USER app

# Run the application
CMD ["/app/.venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]