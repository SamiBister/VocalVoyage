# ADR: **Implement Attestation with the Docker Official GitHub Action**

## Status

Accepted

## Context

We currently produce Docker images that we want to attest so they can be recognized by Docker Hub’s security checks. However, Docker Hub **only** recognizes attestations created via the **Docker Official GitHub Action**. Our existing approach—using third-party tools (e.g., `cosign` or manual SBOM uploads)—is not recognized by Docker Hub for improved security ratings.

Further complicating matters:

- We **must** run a separate security scan step (in the CI/CD pipeline) that can fail the build when vulnerabilities are found.
- The Docker Official GitHub Action requires building and pushing the image in the **same** job that generates the attestation, which conflicts with our desire to build separately and run a security scan first.

## Decision

We will **implement attestation using the Docker Official GitHub Action**, ensuring Docker Hub recognizes our images as properly attested. The plan:

1. **Use Docker Official GitHub Action** for building and pushing images.
2. **Generate a Docker Hub–recognized attestation** in the same workflow step.
3. **Integrate a separate security scan** prior to the final Docker Official GitHub Action step. This means:
   - We will build (and optionally push to a temporary or staging tag) for scanning.
   - If the security scan **passes**, we proceed to the Docker Official GitHub Action to rebuild (or re-tag) and push the final image with the attestation.
   - If the security scan **fails**, the pipeline stops, and we do **not** push an attested image.

## Consequences

### Positive

- **Attestation recognized by Docker Hub**: Our images will show improved security status, boosting trust and compliance.
- **Single Source of Truth**: The official action streamlines attestation management within the Docker ecosystem.
- **Automated CI integration**: We can configure the action to automatically push attested images, reducing manual overhead.

### Negative/Trade-offs

- **Duplicate builds**: We may need to build the image twice—once for scanning, and once with the official Docker Action (if scanning passes).
- **Potential pipeline complexity**: Splitting the build into two parts (security scan, then official build+attest) increases config overhead.
- **Limited flexibility**: We rely on Docker’s official GitHub Action features, which may be less flexible than third-party solutions like cosign.

## Alternatives Considered

1. **Continue using third-party attestation (e.g., cosign)**

   - Docker Hub does not fully recognize these attestations, providing no improvement in their UI or security rating.

2. **Build and attest only once**

   - Skips the separate security scanning step or lumps it inside a single Docker Action job. This loses the ability to fail the pipeline _before_ an image is pushed or attested.

3. **Do no attestation**
   - Our images remain flagged as lacking full security compliance, potentially impacting trust and adoption.

## References

- [Docker Official GitHub Action Documentation](https://github.com/docker/build-push-action)
- [Docker Hub Security Scanning](https://docs.docker.com/docker-hub/vulnerability-scanning/)
- [OCI Image Spec and Attestations](https://github.com/opencontainers/image-spec)
