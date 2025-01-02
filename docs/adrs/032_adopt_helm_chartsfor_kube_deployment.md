**ADR: Adopt Helm Charts for Kubernetes Deployment**

**Status:** Accepted

---

## Context

Our organization needs a consistent, reliable, and maintainable way to package and deploy our containerized services to Kubernetes. We have multiple services (frontend, backend, etc.) running in local and cloud environments. Manual configurations or ad-hoc YAML manifests often lead to:

- Duplication of configuration and deployment files
- Divergent best practices and version mismatches
- Complexity in rolling out updates across multiple environments

The team has evaluated various deployment tools and package managers, including raw Kubernetes manifests, Kustomize, and Helm. After considering the requirements for templating, versioning, discoverability, and community support, we found Helm to be the most mature and flexible solution.

---

## Decision

We will **adopt Helm charts** for deploying our services and infrastructure components into Kubernetes clusters.

1. **Helm Chart Structure**

   - Each service (or stack) will have its own dedicated Helm chart.
   - Shared or cross-cutting infrastructure (like Traefik) may also have a separate chart or be managed through a recognized external chart.

2. **Versioning & Repository**

   - Each Helm chart is versioned independently (using semantic versioning).
   - Charts are stored alongside the service repositories or in a centralized Helm repository.

3. **Templating & Values**

   - We will rely on Helm’s templating capabilities for environment-specific configuration.
   - Default configuration values will be stored in `values.yaml`, with environment-specific overrides in separate values files.

4. **Release Process**

   - We will use either Helm CLI or automation (e.g., GitHub Actions, Argo CD, Flux) to install/upgrade Helm releases.
   - The charts will be tested locally using `helm lint` and `helm template` to ensure they render valid Kubernetes manifests.

5. **Helmfile or Umbrella Charts**
   - Where multiple services need to be deployed together, we will use Helmfile or an umbrella chart to orchestrate them in a single command.

---

## Status

**Accepted** — We have consensus on using Helm. Next steps include creating the initial charts for each service, setting up a CI/CD pipeline, and training team members on Helm usage.

---

## Consequences

### Positive

1. **Consistency**: All services follow a standard packaging and deployment methodology.
2. **Scalability**: New services can quickly adopt existing patterns for environment-specific overrides.
3. **Community & Ecosystem**: Helm is widely used, giving us access to existing charts (e.g., Traefik, Prometheus) and tooling.

### Negative

1. **Learning Curve**: Team members need to learn Helm’s templating syntax, best practices, and chart structure.
2. **Complexity**: Helm adds an additional layer on top of raw Kubernetes manifests.

Overall, the benefits of standardized deployments, version control, and strong community support outweigh the downsides.
