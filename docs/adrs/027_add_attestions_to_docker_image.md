# ADR: **Add Attestations to Docker Images**

## Status

Accepted

## Context

We currently build and push Docker images to Docker Hub without providing attestations. As a result, Docker Hub and other security-focused services label our images with a lower security score or “not fully secure.” We also lack formal proof of supply chain integrity, which is increasingly important for:

- **Compliance**: Organizations require verifiable metadata for auditing and vulnerability management.
- **Best practices**: Tools like `cosign` (Sigstore) and `Attestations` are becoming industry standard for SBOMs, signatures, and provenance data.
- **Traceability**: Developers and security teams need a chain of evidence for how and where the image was built.
- **Public trust**: Users want proof that the image they pull matches the source code and is safe to run.

## Decision

We will **add attestations** (e.g., SBOM, provenance, and/or signatures) to Docker images as part of our CI/CD pipeline. We will:

1. **Build** our Docker images using a standard workflow (e.g., GitHub Actions or another CI).
2. **Attach** attestations—such as SBOMs and supply chain metadata—using an OCI-compliant tool (e.g., `cosign sign-attestation`).
3. **Push** these artifacts to Docker Hub (or other OCI registries) so that each image digest has a corresponding `.att` reference and can be verified.
4. **Integrate** with a transparency log (like [Rekor](https://github.com/sigstore/rekor)) for cryptographic proof, ensuring that artifact integrity is publicly verifiable.

## Consequences

### Positive

- **Improved security reputation**: Docker Hub’s rating will increase, providing higher visibility and trust.
- **Regulatory compliance**: Aligns with security frameworks (e.g., SLSA, NIST) requiring traceable builds and verifiable artifacts.
- **Enhanced developer and user confidence**: Clear, verifiable provenance fosters trust in our releases.

### Negative/Trade-offs

- **Increased build complexity**: Extra steps for signing and attestation in CI/CD.
- **Maintenance overhead**: Keys, tokens, and verification processes must be managed and updated.
- **Possible learning curve**: Development teams must gain familiarity with cryptographic signing tools and transparency logs.

## Alternatives Considered

1. **No attestation**: Remain with the current setup, but continue to be flagged for lower security and possibly fail future supply chain requirements.
2. **Manual SBOM generation only**: Generating SBOMs without cryptographic signing, which partially addresses transparency but does not provide tamper-proof assurance.

## References

- [Docker Documentation: Add labels and metadata](https://docs.docker.com/engine/reference/builder/#label)
- [Sigstore Cosign](https://docs.sigstore.dev/cosign/overview/)
- [OCI Image Spec Annotations](https://github.com/opencontainers/image-spec/blob/main/annotations.md)
