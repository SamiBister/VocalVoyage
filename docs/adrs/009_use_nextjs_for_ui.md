### **ADR: Use Docstrings for Code Documentation**

---

#### **Status**

Accepted

---

#### **Context**

Documentation is essential for understanding and maintaining code. Developers often rely on internal documentation embedded within the code itself to:

1. **Improve Developer Experience**:

   - IDEs can provide contextual tooltips based on inline docstrings.
   - Tooltips reduce the need for developers to leave the codebase to consult external documentation.

2. **Enhance Code Readability**:

   - Inline documentation makes the code easier to understand for new contributors or team members.
   - It reduces the learning curve by clarifying the purpose of methods, functions, and classes.

3. **Automate Persisted Documentation**:
   - Docstrings can be used as a single source of truth to generate external documentation (e.g., Markdown, HTML) through tools like **pdoc3**, **Sphinx**, or **Widdershins**.

To achieve these goals, docstrings will be adopted across the project following a standard format.

---

#### **Decision**

We will use **docstrings** in the codebase to:

1. Document functions, methods, classes, and modules.
2. Provide tooltips in IDEs like PyCharm, VS Code, and others.
3. Serve as the primary source for automated documentation generation.

---

#### **Implementation**

1. **Adopt a Standard Docstring Format**:

   - Use the **NumPy Style** for its clarity and support in most tools.

   **Example in NumPy Style**:

   ```python
   def calculate_sum(a: int, b: int) -> int:
       """
       Calculate the sum of two integers.

       Parameters
       ----------
       a : int
           The first integer.
       b : int
           The second integer.

       Returns
       -------
       int
           The sum of the two integers.

       Examples
       --------
       >>> calculate_sum(2, 3)
       5
       >>> calculate_sum(-1, 5)
       4
       """
       return a + b
   ```

2. **Integrate Docstring Enforcement**:

   - Use tools like `pylint` or `flake8-docstrings` to enforce the presence and format of docstrings in all functions, methods, and classes.

   **Install Flake8 with Docstring Plugin**:

   ```bash
   pip install flake8 flake8-docstrings
   ```

   **Add Configuration to `.flake8`**:

   ```ini
   [flake8]
   max-line-length = 88
   select = D
   ```

3. **Enable Tooltips in IDEs**:

   - IDEs like PyCharm, VS Code, and Jupyter will automatically parse and display docstrings as tooltips during code navigation.

4. **Automate Persisted Documentation**:

   - Use tools like **pdoc3** or **Sphinx** to generate HTML or Markdown documentation from the docstrings.

   **Example with pdoc3**:

   ```bash
   pip install pdoc3
   pdoc --html backend --output-dir docs/backend
   ```

   - Store generated documentation in the `docs/backend` directory for persistence and sharing.

5. **Document the Docstring Policy**:
   - Add guidelines for writing docstrings in the project’s `CONTRIBUTING.md`:
     - Every function, method, and class must have a docstring.
     - Follow the NumPy Style for consistency.

---

#### **Consequences**

**Benefits**:

- **Improves Developer Productivity**:
  - IDE tooltips provide immediate context without requiring external lookup.
- **Enhances Collaboration**:
  - New team members can quickly understand the codebase.
- **Automated Documentation**:
  - Docstrings enable tools like pdoc3 to generate external documentation automatically, ensuring consistency and persistence.
- **Standardization**:
  - A common style across the project ensures readability and ease of maintenance.

**Drawbacks**:

- **Initial Overhead**:
  - Adding docstrings to existing code may require a one-time effort.
- **Enforcement**:
  - Requires integration of linters or reviews to ensure compliance.

---

#### **Alternatives Considered**

1. **Inline Comments**:

   - Pros: Quick and easy to add.
   - Cons: Less structured and not parsed by IDEs or documentation tools.

2. **External Documentation**:

   - Pros: Centralized and polished documentation.
   - Cons: Requires manual updates and risks becoming outdated.

3. **Skip Documentation**:
   - Pros: No additional effort required.
   - Cons: Reduces code clarity and maintainability.

---

#### **Decision Outcome**

By adopting docstrings in the NumPy style, the project will improve code readability, enable IDE tooltips, and provide a foundation for automated documentation. This approach balances clarity, automation, and developer productivity.
