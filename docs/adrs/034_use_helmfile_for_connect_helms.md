**ADR: Use Helmfile to Tie the Deployment Together**

**Status:** Accepted

---

## Context

We manage multiple microservices in Kubernetes, each with its own Helm chart (frontend, backend, Traefik, etc.). While deploying them individually with Helm works, coordinating multiple releases and environments can become cumbersome. We need a single tool that:

1. **Orchestrates multiple Helm releases** in one command.
2. **Allows consistent environment-based configuration** without duplicating effort.
3. **Simplifies** updates and rollbacks across multiple services.

**Helmfile** addresses these requirements by letting us define all Helm releases in one YAML, supporting advanced features such as ordering, environment overrides, and easy rollbacks.

---

## Decision

We will **adopt Helmfile** to tie the deployment together. Specifically:

1. **Centralize** Helm releases in a single `helmfile.yaml` (or multiple YAMLs for advanced use cases).
2. **Leverage environment-specific overrides** and secrets management if needed.
3. **Automate** deployments in CI/CD by running a single `helmfile apply` command.

By doing so, we streamline multi-service deployments and reduce the operational overhead of manually coordinating each Helm release.

---

## Consequences

### Positive

1. **Single Command Deployments**  
   We can install or upgrade all services in one shot, making deployments more efficient.
2. **Consistency**  
   Shared configurations (e.g., environment variables, tags) can be easily inherited across releases.
3. **Easier Management**  
   Helmfile’s environment layering and advanced orchestration reduce the complexity of multi-service rollouts.

### Negative

1. **Learning Curve**  
   Team members must learn Helmfile’s syntax and how it interacts with Helm.
2. **Extra Tooling**  
   Helmfile adds another layer to the toolchain, which means more tooling to maintain.
