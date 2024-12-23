# ADR: Adopt Syft for SBOM Generation

- **Date:** 2024-12-23
- **Status:** Accepted

## Context

We need a robust and standardized way to **generate a Software Bill of Materials (SBOM)** for our code and container images. Currently, our security scanning relies on [Grype](https://github.com/anchore/grype) for vulnerability detection; however, Grype can achieve more accurate results by scanning from an SBOM instead of re-inspecting the entire container or directory every time.

Moreover, we foresee future expansions where the SBOM file can be used for:

- **License compliance checks**
- **Audit trails**
- **Detailed artifact inventory** for supply chain security

**Key points**:

1. **Source and Container**: Both the source code directory (for package dependencies) and the final Docker image (for OS-level packages) must be scanned to capture the full dependency landscape.
2. **Long-term Vision**: Storing SBOM artifacts in a registry or an artifact repository will allow other tools to consume the SBOM for extended use cases (e.g., license checks, DevSecOps dashboards).

## Decision

We will **adopt [Syft](https://github.com/anchore/syft)** as our primary SBOM generation tool. Specifically:

1. **Generate an SBOM for the Source Code**:

   - When code is checked in or built, Syft will scan the local directory (e.g., `syft dir:./source -o json > sbom-source.json`).
   - This captures all application-level dependencies (e.g., Python, Node.js, Go modules).

2. **Generate an SBOM for the Container Image**:

   - After building the Docker image, Syft will scan the image (e.g., `syft docker:myrepo/myimage:latest -o json > sbom-image.json`).
   - This captures OS packages and other runtime dependencies included in the final container.

3. **Use SBOM as Input to Grype**:

   - Grype will consume the SBOM files (`grype sbom:sbom-*.json`) instead of scanning the image or directory from scratch.
   - This yields more accurate and faster security scans.

4. **Store SBOM Outputs**:
   - The SBOM files (`sbom-source.json` and `sbom-image.json`) will be uploaded as CI artifacts or stored in our artifact repository for future analysis.

## Alternatives Considered

1. **No SBOM (Direct Scanning with Grype)**

   - We currently rely on Grype scanning the container or source code directly.
   - While effective, it duplicates scanning efforts and lacks an intermediary artifact that can be reused by other tools.

2. **Other SBOM Generators** (e.g., `tern`, `Trivy`’s built-in SBOM capability)

   - We evaluated multiple tools. Syft’s **speed**, **community support**, and **integration** with Grype make it an optimal choice.

3. **Manual Tracking of Dependencies**
   - Maintaining a manually updated list of dependencies in a spreadsheet or a file.
   - Prone to human error and lacks automation.

## Consequences

### Positive Outcomes

- **Accurate Scans**  
  Grype scans from a standardized SBOM rather than re-inspecting containers or directories, improving both performance and consistency.
- **Reusable SBOM Artifact**  
  We can reuse `sbom-source.json` and `sbom-image.json` for license checks, compliance, or future DevSecOps workflows without re-scanning the same content.

- **Complete Coverage**  
  Separate scans for **source code** and **container image** ensure we capture both application-level and OS-level dependencies.

### Potential Downsides

- **Additional Step**  
  Generating the SBOM requires a Syft installation and a step in the CI/CD pipeline, adding complexity.

- **Maintenance**  
  We must ensure Syft remains updated (especially to handle new package types) and our team is trained to interpret SBOM output.

## Related Work & References

- [Syft Documentation](https://github.com/anchore/syft)
- [Grype Documentation](https://github.com/anchore/grype)
- [CycloneDX and SPDX SBOM Standards](https://cyclonedx.org/) and [https://spdx.dev/](https://spdx.dev/)
