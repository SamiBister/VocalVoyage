# Build stage
FROM node:18-alpine AS builder

WORKDIR /app

# Copy package files
COPY ./frontend/package*.json ./
COPY ./frontend/.env.template ./

# Install dependencies
RUN npm ci

# Copy source files
COPY frontend/ .

# Set backend URL for production
ENV NEXT_PUBLIC_API_URL=http://backend:8000

# Build application
RUN npm run build

# Production stage
FROM node:18-alpine AS runner

WORKDIR /app

# Copy necessary files from builder
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/public ./public
COPY --from=builder /app/.env.local ./.env.local

# Set production environment
ENV NODE_ENV=production
ENV NEXT_PUBLIC_API_URL=http://backend:8000

# Expose the port
EXPOSE 3000

# Start the application
CMD ["npm", "start"]