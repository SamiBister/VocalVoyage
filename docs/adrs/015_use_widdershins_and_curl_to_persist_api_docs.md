### **ADR: Use cURL and Widdershins for API Documentation Generation**

---

#### **Status**

Accepted

---

#### **Context**

The project requires up-to-date and readable API documentation for the backend services. The documentation must:

1. Stay in sync with the Swagger (OpenAPI) specification exposed by the backend.
2. Be automatically generated during the development lifecycle.
3. Output Markdown files for integration with the broader project documentation.

While Swagger UI and Redoc provide live API documentation interfaces, they do not meet the project's requirements for Markdown output. **Widdershins**, combined with **cURL** for fetching the latest OpenAPI spec, provides a lightweight and flexible solution.

---

#### **Decision**

The project will use **cURL** to fetch the `openapi.json` from the backend’s Swagger endpoint and **Widdershins** to convert it into Markdown documentation. The resulting files will be stored in `docs/backend/api`.

---

#### **Implementation**

1. **Fetch OpenAPI Spec with cURL**:

   - Use `cURL` to retrieve the `openapi.json` file from the backend:
     ```bash
     curl http://localhost:8000/openapi.json -o docs/backend/api/openapi.json
     ```

2. **Generate API Documentation with Widdershins**:

   - Use Widdershins to convert the OpenAPI spec to Markdown:
     ```bash
     widdershins --summary --language_tabs 'python:Python' 'javascript:JavaScript' \
     -o docs/backend/api/api-docs.md docs/backend/api/openapi.json
     ```

3. **Directory Structure**:

   - The documentation will reside in the `docs/backend/api` directory:
     ```
     docs/
     └── backend/
         └── api/
             ├── openapi.json
             ├── api-docs.md
     ```

4. **Automate the Process**:

   - Create a script (`generate_api_docs.sh`) to automate fetching the OpenAPI spec and generating Markdown documentation:

     ```bash
     #!/bin/bash

     SWAGGER_URL="http://localhost:8000/openapi.json"
     API_DOC_DIR="docs/backend/api"
     OUTPUT_FILE="$API_DOC_DIR/api-docs.md"
     SPEC_FILE="$API_DOC_DIR/openapi.json"

     echo "Fetching OpenAPI specification from $SWAGGER_URL..."
     curl $SWAGGER_URL -o $SPEC_FILE

     echo "Generating Markdown API documentation with Widdershins..."
     widdershins --summary --language_tabs 'python:Python' 'javascript:JavaScript' \
     -o $OUTPUT_FILE $SPEC_FILE

     echo "API documentation updated in $OUTPUT_FILE"
     ```

5. **Run Backend Locally for Documentation**:

   - Ensure the backend is running locally on `http://localhost:8000` before executing the script.

6. **Integrate into CI/CD**:

   - Add the script to the CI/CD pipeline to ensure the documentation is automatically updated with each backend change.

7. **Commit Documentation**:
   - Add a step to commit the updated documentation:
     ```bash
     git add docs/backend/api
     git commit -m "Update API documentation"
     git push
     ```

---

#### **Consequences**

**Benefits**:

- **Always Up-to-Date**: cURL fetches the latest OpenAPI spec directly from the running backend.
- **Markdown Output**: Widdershins produces readable and structured Markdown documentation.
- **Automation**: Ensures minimal manual effort to maintain documentation.
- **Integration-Ready**: Markdown format integrates seamlessly with static site generators or version control.

**Drawbacks**:

- **Backend Dependency**: Requires the backend to be running to fetch the OpenAPI spec.
- **Additional Steps**: Requires automation to ensure consistent updates.

---

#### **Alternatives Considered**

1. **Swagger UI or Redoc**:

   - Pros: Provides live API documentation.
   - Cons: Does not support Markdown output for integration.

2. **Manual Maintenance**:
   - Pros: Full control over content.
   - Cons: Labor-intensive and prone to inconsistencies.

---

#### **Decision Outcome**

Using **cURL** and **Widdershins** ensures the API documentation is always up-to-date, easily integrated, and automated. This approach aligns with the project's goals of minimal manual intervention and Markdown-based documentation.
