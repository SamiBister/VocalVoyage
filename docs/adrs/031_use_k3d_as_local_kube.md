# Use k3d as Local Development Environment

**Date:** 2024-12-15

## Status

**Proposed**

## Context

Local development environments often rely on standalone tools like `kind` or Minikube to create and manage Kubernetes clusters on a developer’s workstation. These solutions work, but they may incur substantial resource overhead, slow startup times, and additional complexity when integrating into CI/CD pipelines. We need a lightweight, easily reproducible local Kubernetes cluster solution that accelerates developer feedback loops, supports container-based workflows, and aligns closely with production-like configurations.

`k3d` is a wrapper around [k3s](https://k3s.io/) that leverages Docker containers to create and run Kubernetes clusters. It provides a minimal resource footprint, rapid spin-up times, and seamless integration with Docker-based local workflows. By choosing `k3d`, developers can quickly provision clusters, experiment with services, run integrations tests, and iterate more rapidly on their code.

## Decision

**Use `k3d` to provision and manage local development Kubernetes clusters.**

## Consequences

- **Positive:**
  - **Lightweight and Fast:** Developers gain quick startup and teardown of Kubernetes clusters, reducing iteration time and improving the development experience.
  - **Lower Resource Usage:** Running clusters in Docker containers consumes fewer resources compared to fully fledged virtual machine–based solutions, allowing developers to run multiple clusters or other resource-intensive workloads simultaneously.
  - **Integration with Existing Tooling:** `k3d` integrates smoothly with Docker-based workflows, making it straightforward to build, test, and run containerized services in a local Kubernetes environment.
  - **Consistent Environment:** Teams ensure that local testing and development environments are more closely aligned with production-ready Kubernetes configurations.

- **Negative:**
  - **Feature Limitations:** `k3d` provides a lightweight Kubernetes distribution (`k3s`), which may not support every Kubernetes feature or configuration available in more comprehensive distributions.
  - **Learning Curve:** Team members accustomed to Minikube or kind will need to learn `k3d` commands and management patterns.
  - **Docker Dependency:** Relying on Docker as the container runtime may limit flexibility if the team moves away from Docker in the future.

Overall, adopting `k3d` will streamline local Kubernetes development, shorten feedback loops, and improve the resource efficiency of running local clusters.

## Implementation

Collecting workspace information

To set up `k3d` as your local Kubernetes development environment with Helm charts, a local Docker registry, Traefik as the ingress controller, and expose your backend similarly to your Docker Compose setup, follow these steps:

---

### **1. Install `k3d`**

First, install `k3d` on your local machine:

```sh
# For macOS using Homebrew
brew install k3d

# For other systems, use the install script
wget -q -O - https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash
```

### **2. Create a `k3d` Cluster with a Local Registry**

Create a `k3d` cluster configuration file named `k3d-cluster.yml`:

```yaml
apiVersion: k3d.io/v1alpha4
kind: Simple
metadata:
  name: vocabvoyage
servers: 1
agents: 0
image: rancher/k3s:v1.25.4-k3s1
ports:
  - port: 80:80      # Expose HTTP port
    nodeFilters:
      - loadbalancer
options:
  k3s:
    extraArgs:
      - "--disable=traefik"  # Disable default Traefik
registries:
  create:
    name: 'local-registry.localhost'
    host: '0.0.0.0'
    hostPort: '5000'
```

Create the cluster using the configuration:

```sh
k3d cluster create --config k3d-cluster.yml
```

### **3. Update

hosts

 for Local Registry Access**

Add the following entry to your

hosts

 file:

```plaintext
127.0.0.1 local-registry.localhost
```

### **4. Build and Push Docker Images to the Local Registry**

Update your

docker-compose.yml

 to build and tag images for the local registry:

```yaml
services:
  api:
    build:
      context: .
      dockerfile: devops/docker/backend/Dockerfile
    image: local-registry.localhost:5000/vocabvoyage/api:latest
    # ... other configurations
  
  frontend:
    build:
      context: .
      dockerfile: devops/docker/frontend/Dockerfile
    image: local-registry.localhost:5000/vocabvoyage/frontend:latest
    # ... other configurations
```

Build and push the images:

```sh
docker compose build
docker push local-registry.localhost:5000/vocabvoyage/api:latest
docker push local-registry.localhost:5000/vocabvoyage/frontend:latest
```

### **5. Create Helm Charts for Your Application**

Create a Helm chart directory at `helm/vocabvoyage`:

#### **`helm/vocabvoyage/Chart.yaml`**

```yaml
apiVersion: v2
name: vocabvoyage
description: A Helm chart for the VocabVoyage application
version: 0.1.0
appVersion: "1.0"
```

#### **`helm/vocabvoyage/values.yaml`**

```yaml
image:
  repository: local-registry.localhost:5000/vocabvoyage
  tag: latest

ingress:
  enabled: true
  className: traefik
  hosts:
    - host: vocabvoyage.local
      paths:
        - path: /
          pathType: Prefix
```

#### **`helm/vocabvoyage/templates/deployment.yaml`**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 1
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
        - name: api
          image: "{{ .Values.image.repository }}/api:{{ .Values.image.tag }}"
          ports:
            - containerPort: 8000
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
spec:
  replicas: 1
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
        - name: frontend
          image: "{{ .Values.image.repository }}/frontend:{{ .Values.image.tag }}"
          ports:
            - containerPort: 3000
```

#### **`helm/vocabvoyage/templates/service.yaml`**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: api
spec:
  selector:
    app: api
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
---
apiVersion: v1
kind: Service
metadata:
  name: frontend
spec:
  selector:
    app: frontend
  ports:
    - protocol: TCP
      port: 80
      targetPort: 3000
```

#### **`helm/vocabvoyage/templates/ingress.yaml`**

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: vocabvoyage-ingress
  annotations:
    kubernetes.io/ingress.class: traefik
spec:
  rules:
    - host: vocabvoyage.local
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: frontend
                port:
                  number: 80
          - path: /api
            pathType: Prefix
            backend:
              service:
                name: api
                port:
                  number: 80
```

### **6. Install Traefik as the Ingress Controller**

Since we disabled the default Traefik in the cluster, install Traefik via Helm:

```sh
helm repo add traefik https://helm.traefik.io/traefik
helm repo update
kubectl create namespace traefik
helm install traefik traefik/traefik --namespace traefik
```

### **7. Deploy Your Application Using Helm**

Install your application Helm chart:

```sh
kubectl create namespace vocabvoyage
helm install vocabvoyage ./helm/vocabvoyage --namespace vocabvoyage
```

### **8. Update

hosts

 for Access**

Add the following entry to your

hosts

 file:

```plaintext
127.0.0.1 vocabvoyage.local
```

### **9. Verify the Deployment**

Check that all resources are running:

```sh
kubectl get all -n vocabvoyage
kubectl get ingress -n vocabvoyage
```

### **10. Access the Application**

Open your browser and navigate to `http://vocabvoyage.local` to access your frontend, and `http://vocabvoyage.local/api/docs` for your API documentation.

---

**Notes:**

- **Environment Variables**: Ensure your application is configured to use the correct API URL. In your frontend, set `NEXT_PUBLIC_API_URL` to `/api`.

- **Traefik Configuration**: The ingress configuration uses Traefik annotations to route traffic to your services.

- **Local Registry**: Images are pulled from the local registry `local-registry.localhost:5000`. Make sure your images are tagged and pushed to this registry.

- **Helm Charts**: The Helm charts mirror your Docker Compose setup, creating deployments and services for your `api` and frontend
