ARG IMAGE=python:3.13-slim
ARG VERSION=latest
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

LABEL org.opencontainers.image.version="${VERSION}"
LABEL org.opencontainers.image.title="VocabVoyage Backend"
LABEL org.opencontainers.image.description="VocabVoyage Backend Service"
LABEL org.opencontainers.image.source="https://github.com/SamiBister/VocabVoyage"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.authors="Sami Bister"

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