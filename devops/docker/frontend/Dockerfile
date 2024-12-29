# Build stage
ARG NODE_VERSION=23-slim
FROM node:$NODE_VERSION AS builder

WORKDIR /app

# Copy package files
COPY ./frontend/package*.json ./
COPY ./frontend/.env.docker ./.env.local

# Install dependencies
RUN npm ci

# Copy source files
COPY frontend/ .

# Build application with specific environment
ENV NODE_ENV=production
RUN npm run build

#Production stage
FROM node:$NODE_VERSION AS runner

LABEL org.opencontainers.image.version="${VERSION}"
LABEL org.opencontainers.image.title="VocabVoyage YU"
LABEL org.opencontainers.image.description="VocabVoyage UI"
LABEL org.opencontainers.image.source="https://github.com/SamiBister/VocabVoyage"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.authors="Sami Bister"

WORKDIR /app

# Copy necessary files from builder
COPY  --chown=node:node --from=builder /app/.next ./.next
COPY  --chown=node:node --from=builder /app/public ./public
COPY  --chown=node:node --from=builder /app/package.json ./package.json
COPY  --chown=node:node --from=builder /app/.env.local ./.env.local
COPY  --chown=node:node --from=builder /app/node_modules ./node_modules

EXPOSE 3000
# Set production environment
ENV NODE_ENV=production \
    NEXT_PUBLIC_API_URL=/api \
    PORT=3000 \
    NEXT_TELEMETRY_DISABLED=1

USER node

# Start the application
CMD ["npm", "start"]


