# ADR: Adopt Semantic Versioning

- **Date:** 2024-12-21
- **Status:** Accpeted

- **Context:**  
  Our team needs a clear and consistent way to communicate the impact of software changes to other developers. Currently, version numbers are updated in an ad-hoc manner, leading to confusion about whether a release has breaking changes, new features, or just bug fixes. We want to ensure that **developer-facing** version increments provide immediate insight into the **scope** of changes in each commit or release.

- **Decision:**  
  We will adopt **Semantic Versioning (SemVer)** for all our software projects. The version format is `MAJOR.MINOR.PATCH` and follows these rules:

  1. **MAJOR** version increments when incompatible (breaking) changes are introduced.
  2. **MINOR** version increments when backward-compatible features or functionality are added.
  3. **PATCH** version increments when backward-compatible bug fixes or internal improvements are made.

  The **primary audience** for the version numbers is **developers**—both within our team and any external teams or consumers—so that the version itself **communicates the scope** of the change:

  - A **MAJOR** bump signals that existing code integrations may break and require changes.
  - A **MINOR** bump signals new features that developers can opt into without breaking their current usage.
  - A **PATCH** bump signals safe-to-upgrade bug fixes or small improvements.

- **Alternatives Considered:**

  1. **Date-based versioning**: We considered versions like `YYYY.MM.DD`, but this format fails to clearly communicate the magnitude or compatibility impact of changes.
  2. **Commit count or build number**: This would provide a strictly increasing number but does not inform developers if changes are breaking, minor, or patches.

- **Consequences:**

  1. **Positive Outcomes**
     - **Clarity**: Developers see at a glance how significant a change is (breaking vs. additive vs. fix).
     - **Predictability**: A consistent versioning practice helps teams plan upgrades without unexpected breakage.
     - **Developer Communication**: The version number itself becomes a shorthand to describe the scope of changes—reinforcing that versioning is not just for release management but also for developer-to-developer communication.
  2. **Potential Downsides**
     - **Strictness**: Developers must carefully decide if a commit constitutes a patch, minor, or major release, adding overhead to the release process.
     - **Education**: Teams need to understand and consistently follow SemVer guidelines.

- **Related Work & References**
  - [Semantic Versioning 2.0.0](https://semver.org/)
