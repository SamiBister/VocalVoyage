### **ADR: Use JSDoc for Code Documentation**

---

#### **Status**

Accepted

---

#### **Context**

Documentation is essential for understanding and maintaining the codebase. Inline documentation improves developer productivity and facilitates collaboration by:

1. **Enhancing Code Readability**:

   - Inline documentation helps developers understand the purpose and usage of classes, methods, and functions directly in the code.

2. **Improving Developer Experience**:

   - IDEs like Visual Studio Code, WebStorm, and others can display tooltips based on JSDoc, providing contextual help without requiring developers to consult external documentation.

3. **Enabling Automated Documentation**:
   - JSDoc comments serve as a single source of truth for automated tools like **TypeDoc**, which can generate external documentation (e.g., Markdown, HTML).

To meet these objectives, we need a standardized inline documentation approach for TypeScript and JavaScript code.

---

#### **Decision**

We will use **JSDoc** for documenting the frontend codebase, including:

- Functions
- Methods
- Classes
- Interfaces

This decision aligns with the project's goals to maintain high code clarity, developer productivity, and easily generated external documentation.

---

#### **Implementation**

1. **Adopt the JSDoc Format**:

   - Use **JSDoc** comments in the codebase to document functions, methods, classes, and interfaces.

   **Example**:

   ```typescript
   /**
    * Calculates the sum of two numbers.
    *
    * @param a - The first number.
    * @param b - The second number.
    * @returns The sum of the two numbers.
    *
    * @example
    * // Returns 5
    * calculateSum(2, 3);
    */
   function calculateSum(a: number, b: number): number {
     return a + b;
   }
   ```

2. **Enable IDE Tooltips**:

   - Ensure IDEs like VS Code are configured to use JSDoc comments. No additional setup is required; JSDoc is natively supported.

3. **Automate Documentation Generation**:

   - Use **TypeDoc** to generate external documentation:
     - Install TypeDoc:
       ```bash
       npm install typedoc --save-dev
       ```
     - Generate documentation:
       ```bash
       npx typedoc --entryPoints src/ --out docs/frontend
       ```

4. **Integrate Linting for JSDoc**:

   - Use **ESLint** with the `eslint-plugin-jsdoc` plugin to enforce JSDoc presence and correctness:
     - Install the plugin:
       ```bash
       npm install eslint eslint-plugin-jsdoc --save-dev
       ```
     - Add the plugin to your ESLint configuration:
       ```json
       {
         "plugins": ["jsdoc"],
         "rules": {
           "jsdoc/check-alignment": "error",
           "jsdoc/check-param-names": "error",
           "jsdoc/require-param": "error",
           "jsdoc/require-returns": "error"
         }
       }
       ```

5. **Store Documentation**:

   - Generated documentation will be stored in `docs/frontend` and committed to the repository for persistence and sharing.

6. **Document JSDoc Standards**:
   - Add documentation guidelines to the project’s `CONTRIBUTING.md` file, including:
     - Every function, method, and class must have a JSDoc comment.
     - Include `@param`, `@returns`, and `@example` in every JSDoc.

---

#### **Consequences**

**Benefits**:

- **Improved Developer Productivity**:
  - IDE tooltips provide immediate context, improving development speed.
- **Enhanced Collaboration**:
  - New team members can quickly understand the purpose and usage of code elements.
- **Automated Documentation**:
  - JSDoc enables tools like TypeDoc to generate external documentation automatically.
- **Consistency**:
  - A standardized documentation format ensures readability and maintainability.

**Drawbacks**:

- **Initial Overhead**:
  - Adding JSDoc comments to the existing codebase requires an initial time investment.
- **Linting Complexity**:
  - Requires additional configuration and enforcement through linters.

---

#### **Alternatives Considered**

1. **Inline Comments**:

   - Pros: Quick and easy to add.
   - Cons: Not parsed by IDEs or documentation tools; lacks standardization.

2. **External Documentation Only**:

   - Pros: Can provide more polished and structured documentation.
   - Cons: Requires manual updates and risks becoming outdated.

3. **Skip Documentation**:
   - Pros: Reduces time investment.
   - Cons: Results in reduced code clarity and maintainability.

---

#### **Decision Outcome**

Using **JSDoc** ensures that the codebase is well-documented, tooltips are available in IDEs, and external documentation is automatically generated. This decision aligns with the goals of improving code clarity, developer experience, and maintainability.
