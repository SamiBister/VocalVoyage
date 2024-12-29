# Build stage
ARG IMAGE=sha256:f2f8fc3620ff636de73129f9a3a20c5366ce96bbe08f41d54ed158196efa7a9c
FROM $IMAGE AS builder

WORKDIR /app

# Copy package files
COPY ./frontend/package*.json ./
COPY ./frontend/.env.docker ./.env.local

# Install dependencies
RUN npm ci

# Copy source files
COPY frontend/ .

# Build application
RUN npm run build

#Production stage
FROM $IMAGE AS runner



WORKDIR /app

# Copy necessary files from builder
COPY  --chown=node:node --from=builder /app/.next ./.next
COPY  --chown=node:node --from=builder /app/public ./public
COPY  --chown=node:node --from=builder /app/package.json ./package.json
COPY  --chown=node:node --from=builder /app/.env.local ./.env.local
COPY  --chown=node:node --from=builder /app/node_modules ./node_modules



EXPOSE 3000
# Set production environment
ENV NODE_ENV=production
ENV NEXT_PUBLIC_API_URL=/api

USER node

# Start the application
CMD ["npm", "start"]


