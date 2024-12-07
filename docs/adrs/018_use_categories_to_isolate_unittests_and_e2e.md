# **ADR: Use Categories to Isolate End-to-End Tests from Unit Tests**

## **Context**

The project involves a backend written in Python and a frontend application. To ensure the quality of the application, we need a structured testing strategy that:

1. **Differentiates Unit Tests and End-to-End (E2E) Tests**:

   - Unit tests verify isolated components or logic, such as utility functions or API handlers, without external dependencies.
   - End-to-End tests verify the interaction between the backend and frontend, simulating user workflows and external API calls.

2. **Enables Flexible Test Execution**:

   - Developers should be able to run unit tests, E2E tests, or both, depending on the context (e.g., during local development or CI/CD pipelines).

3. **Supports Clear Organization and Maintainability**:
   - Tests should be logically separated in the codebase to prevent confusion and improve maintainability.

To address these needs, we decided to use **categories** for tests and leverage `pytest.mark` to tag and isolate unit tests from E2E tests.

## **Decision**

We will categorize tests into **unit tests** and **end-to-end tests**:

1. **Unit Tests**:

   - Reside in the `tests/unit/` directory.
   - Marked with `@pytest.mark.unit`.
   - Focus on isolated logic without requiring external services.

2. **End-to-End Tests**:
   - Reside in the `tests/e2e/` directory.
   - Marked with `@pytest.mark.e2e`.
   - Require both the Python backend and frontend to be running.

### **Implementation**

1. **Directory Structure**:

   - Tests are organized into separate directories:
     ```
     tests/
     ├── unit/
     │   ├── test_backend_logic.py
     │   ├── test_utilities.py
     ├── e2e/
     │   ├── test_homepage.py
     │   ├── test_navigation.py
     ```

2. **Markers**:

   - Add custom markers for `unit` and `e2e` in `pytest.ini`:
     ```ini
     [pytest]
     markers =
         unit: Unit tests for isolated logic.
         e2e: End-to-end tests for backend and frontend integration.
     ```

3. **Test Example**:

   - **Unit Test**:

     ```python
     import pytest

     @pytest.mark.unit
     def test_addition():
         assert 1 + 1 == 2
     ```

   - **End-to-End Test**:

     ```python
     import pytest
     from playwright.sync_api import Page

     @pytest.mark.e2e
     def test_homepage_loads(page: Page):
         page.goto("/")
         assert page.title() == "Welcome to Next.js"
     ```

4. **Running Tests**:

   - Run unit tests only:
     ```bash
     pytest -m unit
     ```
   - Run E2E tests only:
     ```bash
     pytest -m e2e
     ```
   - Run all tests:
     ```bash
     pytest
     ```

5. **CI/CD Integration**:

   - Separate unit and E2E tests in pipelines:

     ```yaml
     jobs:
       unit-tests:
         runs-on: ubuntu-latest
         steps:
           - run: pytest -m unit

       e2e-tests:
         runs-on: ubuntu-latest
         steps:
           - run: pytest -m e2e
     ```

## **Consequences**

### **Positive Consequences**

1. **Clear Test Categorization**:

   - Unit tests and E2E tests are logically separated, making it easier for developers to understand their purpose.

2. **Flexible Execution**:

   - Developers can run specific categories of tests based on their current needs, improving efficiency during local development and CI/CD.

3. **Improved Maintainability**:
   - Test organization improves as the project scales, ensuring tests remain manageable.

### **Negative Consequences**

1. **Setup Complexity**:

   - Additional setup is required for defining markers and maintaining directory structures.

2. **Marker Enforcement**:

   - Developers need to remember to tag tests with the appropriate `@pytest.mark`.

3. **Longer CI/CD Pipeline**:
   - Running unit and E2E tests in separate jobs can slightly increase overall pipeline runtime.

## **Alternatives Considered**

1. **Run All Tests Together Without Categorization**:

   - Pros:
     - Simplifies test setup and execution.
   - Cons:
     - Test execution becomes slower, and unit test feedback is delayed due to longer-running E2E tests.

2. **Use Directories Without Markers**:

   - Pros:
     - No need for `pytest.mark`.
   - Cons:
     - Lacks flexibility to selectively run tests without specifying directories explicitly.

3. **Use a Separate Test Framework for E2E Tests**:
   - Pros:
     - Fully isolated test frameworks for unit and E2E tests.
   - Cons:
     - Adds complexity by introducing another tool for E2E tests, such as Cypress or Playwright outside pytest.

## **Decision Outcome**

By using categories and `pytest.mark` to isolate unit and E2E tests:

- The testing process is more modular, efficient, and developer-friendly.
- Test execution is flexible, enabling targeted testing during development and CI/CD.

This approach ensures scalable, maintainable, and effective testing practices for the project.
