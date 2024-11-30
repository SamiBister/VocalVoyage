# Use Ruff for Python Linting

## Status

Accepted

## Context

Code linting is an essential practice for maintaining a clean, consistent, and high-quality codebase. We required a linting tool that is fast, integrates well with our development workflow, and supports multiple Python linting rules without introducing significant overhead.

After evaluating several linting tools, we decided to adopt **Ruff**, a modern Python linter, for the following reasons:

- **Performance:** Ruff is written in Rust, making it significantly faster than other Python-based linters.
- **Feature Set:** It supports a wide range of linting rules and functionalities, including common ones provided by tools like Flake8, PyLint, and isort.
- **Ease of Integration:** Ruff integrates seamlessly into CI/CD pipelines and local development environments.
- **Configurable:** It provides flexible configuration options to adapt to our project’s specific needs.
- **Community Adoption:** Ruff is gaining traction in the Python community, ensuring long-term support and updates.

## Decision

We have decided to use **Ruff** as the primary linting tool for our Python projects. This decision was made based on the following factors:

1. **Speed:** Ruff’s performance ensures fast feedback during development and CI runs, improving developer productivity.
2. **Consolidation of Tools:** Ruff combines the functionality of multiple tools (e.g., Flake8, isort), reducing the need for multiple configurations and dependencies.
3. **Ease of Use:** It is straightforward to install and configure, minimizing the setup effort for developers.
4. **Active Development:** Ruff is actively maintained with regular updates, ensuring compatibility with modern Python versions and practices.

## Consequences

### Positive

- **Improved Efficiency:** Faster linting speeds reduce waiting times for developers.
- **Streamlined Tooling:** Using Ruff minimizes the need for multiple tools, reducing complexity and potential conflicts.
- **Standardized Codebase:** Ensures consistent coding standards across the project.
- **Scalability:** Suitable for large codebases due to its high performance.

### Negative

- **Feature Maturity:** Ruff is relatively new, and certain advanced features or plugins available in older tools like PyLint may not yet be supported.
- **Learning Curve:** Developers familiar with older linting tools may need to adjust to Ruff’s configuration and rules.
- **Dependency on a Newer Tool:** Being a newer project, its long-term viability depends on continued community and maintainer support.

## Follow-Up Actions

1. **Initial Setup:** Add Ruff to the project and configure it according to the team’s coding standards.
2. **Documentation:** Document Ruff’s usage, configuration, and integration within the codebase.
3. **Training:** Provide guidance to developers on Ruff’s rules and how to address linting issues.
4. **CI/CD Integration:** Incorporate Ruff into the CI pipeline to enforce linting on all pull requests.
5. **Monitor Updates:** Regularly review Ruff’s updates and feature roadmap to ensure it continues to meet our needs.

## Alternatives Considered

- **Flake8:** A widely-used Python linter, but slower and requires additional plugins for certain functionalities.
- **PyLint:** Comprehensive but significantly slower for large codebases, which affects developer productivity.
- **Black and isort Combination:** While Black and isort focus on formatting and imports, they lack the broader linting capabilities consolidated in Ruff.

## Summary

Adopting Ruff as the linting tool aligns with our goals of maintaining a high-quality, consistent codebase while ensuring fast feedback and streamlined tooling. Despite being relatively new, Ruff’s speed, features, and growing adoption in the Python community make it the optimal choice for our project’s linting needs.
