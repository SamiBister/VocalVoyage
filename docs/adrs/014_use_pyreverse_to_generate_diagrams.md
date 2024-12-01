### **ADR: Use Pyreverse for Generating Diagrams**

---

#### **Status**

Accepted

---

#### **Context**

To improve the clarity of the project's architecture and facilitate understanding among team members, diagrams such as class and package diagrams need to be generated. These diagrams should represent the relationships between classes and packages in the Python backend.

The requirements for diagram generation are:

1. **Automation**: The process should be easily reproducible and integrated into the CI/CD pipeline.
2. **Versatility**: Diagrams should be available in various formats, including:
   - **`.dot`**: GraphViz source files for further processing or customization.
   - **`.puml`**: PlantUML format for detailed diagram rendering.
   - **`.html`**: Web-accessible static visualizations.
   - **`.mmd`**: Mermaid.js format for Markdown-based diagramming.

After evaluating several tools, **Pyreverse** was selected for this task.

---

#### **Decision**

We will use **Pyreverse**, a utility within **Pylint**, to generate diagrams for the Python backend and store the output in `.dot`, `.puml`, `.html`, and `.mmd` formats.

---

#### **Implementation**

1. **Install Pyreverse**:

   - Pyreverse is included as part of **Pylint**, so ensure it's installed:
     ```bash
     pip install pylint
     ```

2. **Command for Generating Diagrams**:

   - Generate diagrams in the required formats:

     ```bash
     # Generate GraphViz `.dot` files
     pyreverse -o dot -p project_name backend/

     # Generate PlantUML `.puml` files
     pyreverse -o plantuml -p project_name backend/

     # Generate `.html` and `.mmd` (requires post-processing)
     pyreverse -o dot -p project_name backend/
     dot -Tsvg classes_project_name.dot -o diagrams/classes_project_name.html
     dot -Tmmd classes_project_name.dot -o diagrams/classes_project_name.mmd
     ```

3. **Store Generated Files**:

   - Store all generated diagrams in a centralized directory: `doc/backend/diagrams`.
   - The structure:
     ```
     docs/backend/diagrams/
     ├── dot/
     │   ├── classes_project_name.dot
     │   ├── packages_project_name.dot
     ├── puml/
     │   ├── classes_project_name.puml
     │   ├── packages_project_name.puml
     ├── html/
     │   ├── classes_project_name.html
     ├── mmd/
     │   ├── classes_project_name.mmd
     ```

4. **Automate Diagram Generation**:

   - Add a script (`generate_diagrams.sh`) to automate the diagram generation process:

     ```bash
     #!/bin/bash

     OUTPUT_DIR="doc/backend/diagrams"

     echo "Generating diagrams with Pyreverse..."

     # Create output directories
     mkdir -p $OUTPUT_DIR/dot $OUTPUT_DIR/puml $OUTPUT_DIR/html $OUTPUT_DIR/mmd

     # Generate `.dot` and `.puml` files
     pyreverse -o dot -p project_name backend/
     cp classes_project_name.dot packages_project_name.dot $OUTPUT_DIR/dot/
     pyreverse -o plantuml -p project_name backend/
     cp classes_project_name.puml packages_project_name.puml $OUTPUT_DIR/puml/

     # Convert `.dot` to `.html` and `.mmd`
     dot -Tsvg $OUTPUT_DIR/dot/classes_project_name.dot -o $OUTPUT_DIR/html/classes_project_name.html
     dot -Tmmd $OUTPUT_DIR/dot/classes_project_name.dot -o $OUTPUT_DIR/mmd/classes_project_name.mmd

     echo "Diagrams generated and saved in $OUTPUT_DIR"
     ```

5. **Integrate into CI/CD**:

   - Run the `generate_diagrams.sh` script in the CI/CD pipeline to ensure diagrams are always updated and stored in the repository or a documentation site.

6. **Optional Enhancements**:
   - Use PlantUML or Mermaid.js renderers for real-time updates or embedding diagrams in Markdown documentation.

---

#### **Consequences**

**Benefits**:

- **Versatility**: Diagrams are available in multiple formats for different use cases:
  - `.dot` for GraphViz processing.
  - `.puml` for PlantUML rendering.
  - `.html` for easy web hosting.
  - `.mmd` for integration with Markdown-based documentation tools.
- **Automation**: Easily reproducible and maintainable through scripts.
- **Standardization**: Centralized storage ensures consistency across the project.

**Drawbacks**:

- **Complexity**: Managing multiple formats adds some overhead.
- **Graph Layouts**: Pyreverse may produce less aesthetically pleasing layouts compared to more advanced visualization tools.

---

#### **Alternatives Considered**

1. **GraphViz Standalone**:

   - Pros: Direct generation of `.dot` and `.svg` files.
   - Cons: Lacks support for Python-specific diagram generation.

2. **PlantUML Only**:

   - Pros: Detailed and visually appealing diagrams.
   - Cons: Requires additional tooling to generate `.puml` files from Python source.

3. **Mermaid.js Only**:
   - Pros: Markdown-friendly, suitable for documentation sites.
   - Cons: Requires manual generation of diagrams or third-party scripts.

---

#### **Decision Outcome**

By using Pyreverse, we can automatically generate architecture diagrams in multiple formats with minimal effort. This aligns with the project's goals of clarity, automation, and flexibility.
