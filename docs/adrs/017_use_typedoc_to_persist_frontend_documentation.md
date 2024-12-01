### **ADR: Use TypeDoc for Persisting JSDoc Documentation**

---

#### **Status**

Accepted

---

#### **Context**

The project requires a standardized approach to generate and persist documentation for the frontend codebase, which is written in TypeScript. The documentation should:

1. **Be Generated from JSDoc Comments**:

   - JSDoc comments provide inline documentation within the codebase.
   - Automated tools are needed to convert these comments into a shareable and easily navigable format (e.g., HTML or Markdown).

2. **Provide Persistent Documentation**:

   - Documentation should be stored and accessible in a centralized location (`docs/frontend`).
   - It should be version-controlled to ensure historical reference and easy sharing.

3. **Support Automation**:
   - The process should be automated to reduce manual effort and ensure consistency with code changes.

TypeDoc is a well-supported tool for generating documentation from JSDoc comments in TypeScript codebases. It meets the project’s needs for automation, readability, and flexibility in output formats.

---

#### **Decision**

The project will use **TypeDoc** to generate and persist documentation from JSDoc comments. The generated documentation will be stored in the `docs/frontend` directory for persistence and distribution.

---

#### **Implementation**

1. **Install TypeDoc**:

   - Add TypeDoc and necessary plugins as a development dependency:
     ```bash
     npm install typedoc typedoc-plugin-markdown --save-dev
     ```

2. **Configure TypeDoc**:

   - Create a `typedoc.json` configuration file in the project root:
     ```json
     {
       "entryPoints": ["src/"],
       "out": "docs/frontend",
       "plugin": ["typedoc-plugin-markdown"],
       "theme": "default",
       "exclude": ["**/*.test.tsx", "**/*.spec.ts"],
       "excludeExternals": true,
       "hideGenerator": true,
       "categorizeByGroup": false
     }
     ```
     - **Key Options**:
       - `entryPoints`: Specifies the source directory for TypeScript files.
       - `out`: Defines the output directory for the generated documentation.
       - `plugin`: Enables the Markdown output plugin.
       - `exclude`: Excludes test files from documentation.
       - `categorizeByGroup`: Simplifies grouping in the output.

3. **Generate Documentation**:

   - Add an npm script to generate documentation:
     ```json
     "scripts": {
       "docs:generate": "typedoc"
     }
     ```
   - Run the script to generate the documentation:
     ```bash
     npm run docs:generate
     ```

4. **Store Documentation**:

   - Generated documentation will be saved in `docs/frontend`.

5. **Automate in CI/CD**:

   - Add a step to the CI/CD pipeline to generate and commit updated documentation:
     ```bash
     npm install
     npm run docs:generate
     git add docs/frontend
     git commit -m "Update frontend documentation"
     git push
     ```

6. **Host Documentation**:
   - Use a static site hosting solution to make the documentation publicly accessible:
     - **GitHub Pages**: Commit the generated `docs/frontend` directory to the repository and enable GitHub Pages.
     - **Netlify or Vercel**: Deploy the directory as a static site.

---

#### **Consequences**

**Benefits**:

- **Automation**: Automatically generates documentation from JSDoc, reducing manual effort.
- **Persistence**: Stores documentation in version control, providing historical reference and ensuring availability.
- **Developer Experience**: Improves code clarity by linking inline documentation (JSDoc) with external resources.
- **Markdown Output**: Supports Markdown for integration with documentation systems like MkDocs or GitHub Pages.

**Drawbacks**:

- **Initial Setup**: Requires additional configuration and dependencies.
- **Tool Limitations**: Complex customizations may require extending TypeDoc.

---

#### **Alternatives Considered**

1. **Manual Documentation**:

   - Pros: Full control over structure and content.
   - Cons: Labor-intensive and prone to becoming outdated.

2. **JSDoc CLI**:

   - Pros: Generates documentation directly from JSDoc.
   - Cons: Limited output formats and less modern UI compared to TypeDoc.

3. **No Persisted Documentation**:
   - Pros: No additional tooling or maintenance required.
   - Cons: Missed opportunity for centralized, shareable documentation.

---

#### **Decision Outcome**

Using **TypeDoc** ensures consistent, automated, and persistent documentation generation from JSDoc comments. The documentation will be easy to access, version-controlled, and aligned with code changes, improving maintainability and developer experience.
