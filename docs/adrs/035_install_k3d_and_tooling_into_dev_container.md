**ADR: Provide Developer Container with K3D Environment Tools**

**Status:** Accepted

---

## Context

Local development and testing often require multiple tools (such as **k3d**, **kubectl**, **Helm**, **Helmfile**, etc.). Installing, configuring, and keeping them up to date on each developer’s machine can be error-prone and time-consuming. We want to:

1. **Ensure consistency** across development environments.
2. **Reduce onboarding friction** by making tools readily available.
3. **Enable quick adoption of new features** by updating a single container image, rather than multiple local machines.

Providing a preconfigured **developer container** with all necessary tools addresses these needs.

---

## Decision

We will **build and maintain a developer container** that includes all tools required to run our **k3d** environment, deploy Helm charts, and manage Kubernetes resources. Specifically:

1. **Container Image**: A Debian- or Ubuntu-based image containing k3d, kubectl, Helm, Helmfile, and any other CLI tools.
2. **Version Pinning**: We will pin versions of critical tools to ensure reproducible builds.
3. **Distribution**: The container image will be published to an internal or external registry so developers can pull and run it easily (or use it as a VSCode DevContainer).
4. **Updates and Maintenance**: The team will update this image as new versions of k3d or other tools are released, ensuring a uniform approach to upgrades.

---

## Consequences

### Positive

1. **Consistency**
   - All developers use the exact same versions of k3d, kubectl, Helm, etc., minimizing “it works on my machine” issues.
2. **Faster Onboarding**
   - New team members can pull the container image and have a ready-made environment.
3. **Easy Upgrades**
   - When tools need to be updated, we only update the container image, and everyone benefits immediately.

### Negative

1. **Image Size**
   - The developer container may become large if it includes many tools, which can increase download times.
2. **Maintenance**
   - We must regularly maintain the container, updating dependencies and fixing security issues.

Overall, the benefits of a streamlined, uniform environment outweigh the overhead of maintaining the container.
