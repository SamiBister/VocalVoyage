# **Architectural Decision Record: Use Traefik as Reverse Proxy with Docker Compose**

## **Status**

Approved

## **Context**

In the current architecture, we need a reverse proxy to route requests to services deployed with Docker Compose. The chosen solution must meet the following requirements:

- **Dynamic Configuration**: The reverse proxy must support automatic discovery and reconfiguration of services as they scale up, down, or are updated.
- **Integration with Kubernetes**: Our future roadmap includes deploying services on Kubernetes (k3d), which uses Traefik as its default ingress controller. Aligning with this ensures consistency and smoother transitions.

Alternative options like NGINX and HAProxy are widely used but require manual reconfiguration or additional scripting for dynamic updates. Traefik, by contrast, integrates natively with Docker Compose and Kubernetes for service discovery and dynamic routing.

## **Decision**

We will use **Traefik** as the reverse proxy for the services managed by Docker Compose.

## **Rationale**

The primary reasons for choosing Traefik are:

1. **Dynamic Configuration**:
   - Traefik supports automatic service discovery through Docker Compose labels.
   - It can dynamically update its configuration when services are added, removed, or updated without requiring a restart.

2. **Kubernetes Alignment**:
   - Traefik is the default ingress controller in **k3d** Kubernetes. Using it in the current setup aligns with future Kubernetes deployments, simplifying transitions.
   - It supports Kubernetes CRDs (Custom Resource Definitions), enabling advanced routing rules and scalability.

3. **Ease of Use**:
   - Traefik’s use of declarative configuration via labels in `docker-compose.yml` simplifies its integration.
   - Built-in support for Let's Encrypt provides automated SSL/TLS certificate generation and renewal.

4. **Features**:
   - Support for multiple protocols (HTTP, HTTPS, TCP, UDP).
   - Built-in metrics and monitoring with Prometheus and Grafana.
   - Middleware for advanced traffic management, such as rate limiting and request redirection.

5. **Community and Ecosystem**:
   - Strong community support and documentation.
   - A widely adopted solution for microservices architectures.

## **Consequences**

- **Positive**:
  - Simplifies service discovery and routing for Docker Compose deployments.
  - Aligns with future Kubernetes deployments, reducing learning curve and migration complexity.
  - Provides modern features like automatic SSL, monitoring, and middleware support out of the box.

- **Negative**:
  - Slight learning curve for teams unfamiliar with Traefik's configuration style.
  - Potential overhead for very simple setups where dynamic configuration isn't required.

---

## **Decision Outcome**

We will configure Traefik with Docker Compose by:

1. Including the Traefik service in the `docker-compose.yml` file.
2. Using Docker labels for dynamic configuration of service routes.
3. Enabling SSL/TLS through Let's Encrypt.
4. Setting up monitoring integrations as needed.

The decision will be revisited if:

- There are major architectural changes (e.g., abandoning Kubernetes).
- Performance or feature limitations arise with Traefik.

## **References**

- [Traefik Documentation](https://doc.traefik.io/traefik/)
- [k3d Documentation](https://k3d.io/)
- [Docker Compose Configuration](https://docs.docker.com/compose/)
