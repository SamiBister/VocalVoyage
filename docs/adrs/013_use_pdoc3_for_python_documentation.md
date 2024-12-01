### **ADR: Use pdoc3 for Automated Python Documentation Generation**

---

#### **Status**

Accepted

---

#### **Context**

To ensure that the Python backend of the project is well-documented and the documentation remains up-to-date with minimal manual effort, an automated solution is required. The generated documentation should be:

1. Easy to produce.
2. Understandable by developers.
3. Flexible enough to support both local and CI/CD workflows.
4. Well-integrated with existing Python docstring conventions.

Several tools were considered for this purpose, including **Sphinx**, **PyDoc**, and **pdoc3**.

---

#### **Decision**

We will use **pdoc3** as the primary tool to generate automated documentation from Python docstrings.

**pdoc3** was chosen due to the following reasons:

- It provides **Markdown/HTML output**, which is lightweight and readable.
- Requires minimal configuration compared to Sphinx.
- Supports live previews of the documentation, improving the developer experience.
- Works seamlessly with Google-style and NumPy-style docstrings, which are already in use in the project.
- Simple to integrate into CI/CD pipelines for automated updates to documentation.

---

#### **Implementation**

1. **Install pdoc3**:
   Add pdoc3 to the project dependencies:

   ```bash
   pip install pdoc3
   ```

2. **Directory for Documentation**:
   Generated documentation will be placed in `doc/backend`.

3. **Generate Documentation**:
   Use the following command to generate the documentation in Markdown or HTML:

   ```bash
   pdoc --output-dir doc/backend backend
   ```

4. **Automate Documentation Updates**:

   - Add a script (`generate_docs.sh`) to automate the documentation generation process:

     ```bash
     #!/bin/bash
     echo "Generating documentation..."
     pdoc --output-dir doc/backend backend
     echo "Documentation updated in doc/backend"
     ```

   - Integrate this script into the CI/CD pipeline to ensure that documentation is automatically updated and published when code changes are merged.

5. **Host the Documentation**:
   - Markdown files can be committed to the repository for local use or hosted on platforms like GitHub Pages.
   - Alternatively, the HTML output can be served via a static site hosting service (e.g., Netlify, AWS S3).

---

#### **Consequences**

**Benefits**:

- Simple setup and maintenance.
- Lightweight documentation with clear Markdown/HTML output.
- Reduces developer workload by automating the process.
- Encourages adherence to docstring conventions for code clarity.

**Drawbacks**:

- pdoc3 does not support advanced customization features (e.g., cross-referencing) that tools like Sphinx provide.
- Markdown output may require additional formatting for some use cases.

---

#### **Alternatives Considered**

1. **Sphinx**:

   - Pros: Highly customizable, supports various formats (Markdown, HTML, PDF).
   - Cons: Complex setup, requires additional dependencies and configuration.

2. **PyDoc**:
   - Pros: Built into Python, no extra installation required.
   - Cons: Limited output options (plain text or basic HTML), not as developer-friendly for large projects.

---

#### **Decision Outcome**

Using **pdoc3** ensures that documentation generation is simple, consistent, and integrates seamlessly with existing workflows. This decision aligns with the project's goals to maintain clarity and minimize complexity.
