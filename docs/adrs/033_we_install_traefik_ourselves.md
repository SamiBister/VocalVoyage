**ADR: Install and Manage Traefik as Ingress in k3d**

**Status:** Accepted

---

## Context

We want to use **k3d** for local Kubernetes clusters. By default, k3s (which k3d wraps) ships with a built-in version of Traefik. However, we need:

1. **Version control and configuration**: We want to lock in specific Traefik versions and manage configurations consistently.
2. **Flexibility**: We plan to customize Traefik’s resources and middlewares, which can be cumbersome with the built-in distribution.
3. **Consistency across environments**: Managing Traefik ourselves ensures our local k3d setup is closer to production or other non-default environments.

Disabling the built-in Traefik in k3s and installing our own instance is a straightforward way to achieve these requirements.

---

## Decision

We will **disable the built-in Traefik** in k3s when creating a k3d cluster, then **install Traefik ourselves**—for example, via Helm. This approach allows us to manage Traefik independently of the k3s lifecycle.

1. **k3d Configuration**

   - Add `--disable=traefik` to our k3s arguments in the `k3d` config to ensure the default Traefik does not run.

2. **Custom Traefik Installation**

   - Use a dedicated chart or repository (e.g., the official Traefik Helm chart) to install and manage Traefik.
   - Apply specific configuration for ports, logs, middlewares, TLS, etc.

3. **Ingress Configuration**
   - Configure `Ingress` resources to route traffic through our new Traefik instance.
   - Optionally set up advanced routing, middlewares, or custom certificates.

---

## Status

**Accepted** — We will adopt this approach for local development, testing, and possibly replicate the model in other non-production environments as needed.

---

## Consequences

### Positive

1. **Version Control**: We decide which version of Traefik to run, making upgrades explicit and easier to manage.
2. **Consistency**: The local environment closely mirrors any environment where we also install Traefik manually.
3. **Flexibility**: We can fully customize Traefik’s configuration (ports, middlewares, TLS, logs, metrics, etc.).

### Negative

1. **Maintenance**: We assume responsibility for maintaining and upgrading Traefik, including applying security patches.
2. **Slight Complexity**: We have one more Helm release (or other deployment method) to manage, rather than using a built-in component.

---

## Links & References

- [k3d Documentation](https://k3d.io/)
- [Traefik Helm Chart](https://github.com/traefik/traefik-helm-chart)
- [k3s — Disabling Components](https://rancher.com/docs/k3s/latest/en/installation/install-options/#disable)
