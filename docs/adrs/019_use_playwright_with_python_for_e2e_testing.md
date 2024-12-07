# **ADR: Use Playwright with Python for End-to-End Testing**

## **Context**

End-to-end (E2E) testing ensures that the application behaves as expected by simulating real user interactions. The project includes:

- A **Python backend** running from the root directory.
- A **Next.js frontend** located in the `frontend/` directory.

We need a solution for E2E testing that integrates seamlessly with the Python ecosystem and allows:

1. **Simulating Real User Interactions**:

   - Verify the integration of frontend and backend services.
   - Test user workflows, including navigation, API calls, and data updates.

2. **Automation**:

   - Start the backend and frontend servers as part of the test setup.
   - Automatically clean up the environment after tests.

3. **Integration with Pytest**:
   - Use pytest as the test framework to leverage existing configurations and reporting tools.
   - Categorize E2E tests with `pytest.mark.e2e` for selective execution.

Playwright is a robust tool for end-to-end testing that supports multiple browsers and integrates well with Python.

---

## **Decision**

We will use **Playwright with Python** for end-to-end testing and integrate it with **pytest**. The testing workflow will:

1. Start the **backend** (Python) and **frontend** (Next.js) servers as part of the test environment.
2. Use Playwright to interact with the application through a browser.
3. Categorize E2E tests with `pytest.mark.e2e` for flexibility in running tests.
4. Allow seamless execution of tests locally and in CI/CD pipelines.

---

## **Implementation**

### **1. Install Required Dependencies**

Install Playwright for Python and pytest integration:

```bash
pip install pytest pytest-playwright
playwright install
```

---

### **2. Directory Structure**

Organize the tests and supporting files:

```
root/
├── main.py                # Backend entry point
├── frontend/              # Frontend application
│   ├── package.json
│   ├── ...
├── tests/                 # Test files
│   ├── e2e/               # E2E tests
│   │   ├── test_homepage.py
│   │   ├── test_navigation.py
│   ├── conftest.py        # Setup backend and frontend
├── pytest.ini             # Pytest configuration
└── ...
```

---

### **3. `conftest.py` for Test Environment Setup**

**`tests/conftest.py`:**

```python
import subprocess
import time
import pytest

@pytest.fixture(scope="session", autouse=True)
def start_test_environment():
    """
    Starts the Python backend and Next.js frontend servers before running tests,
    and shuts them down afterward.
    """
    # Start the backend server
    backend_process = subprocess.Popen(
        ["python3", "main.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=".",  # Backend runs from the root
    )

    # Start the frontend server
    frontend_process = subprocess.Popen(
        ["npm", "run", "dev"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd="frontend",  # Frontend runs from the "frontend" directory
    )

    # Wait for servers to start
    time.sleep(5)  # Adjust based on your application startup time

    yield  # Tests execute here

    # Shut down the servers after tests
    backend_process.terminate()
    backend_process.wait()
    frontend_process.terminate()
    frontend_process.wait()
```

---

### **4. Configure Pytest Markers**

Add custom markers for E2E tests in `pytest.ini`:

**`pytest.ini`:**

```ini
[pytest]
markers =
    e2e: End-to-end tests that verify backend and frontend integration.
```

---

### **5. Write E2E Tests**

Create Playwright-based tests in the `tests/e2e/` directory.

#### Example: Test Homepage

**`tests/e2e/test_homepage.py`:**

```python
import pytest
from playwright.sync_api import Page

@pytest.mark.e2e
def test_homepage_title(page: Page):
    # Navigate to the homepage
    page.goto("http://localhost:3000")

    # Assert the page title
    assert page.title() == "Welcome to Next.js"

@pytest.mark.e2e
def test_navigation(page: Page):
    # Navigate to the homepage
    page.goto("http://localhost:3000")

    # Click on the About link
    page.click("text=About")

    # Assert the URL
    assert page.url == "http://localhost:3000/about"
```

---

### **6. Run Tests**

- Run **all tests**:

  ```bash
  pytest
  ```

- Run **E2E tests only**:
  ```bash
  pytest -m e2e
  ```

---

### **7. CI/CD Integration**

Integrate the tests into your CI/CD pipeline. Example for **GitHub Actions**:

**`ci.yml`:**

```yaml
name: End-to-End Tests

on:
  push:
    branches:
      - main

jobs:
  e2e-tests:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Install Python dependencies
        run: pip install -r requirements.txt

      - name: Install frontend dependencies
        run: npm install --prefix frontend

      - name: Run Playwright tests
        run: pytest -m e2e
```

## **Consequences**

### **Positive Consequences**

1. **Comprehensive Testing**:

   - Simulates real user workflows, verifying the integration between frontend and backend.

2. **Pytest Integration**:

   - Easy categorization and execution using `pytest.mark.e2e`.
   - Unified reporting for unit and E2E tests.

3. **Automated Environment Setup**:

   - Servers start and stop automatically, reducing manual intervention.

4. **CI/CD Friendly**:
   - Easily integrated into pipelines for automated testing.

### **Negative Consequences**

1. **Resource Intensive**:

   - E2E tests require more time and resources compared to unit tests.

2. **Setup Complexity**:

   - Requires maintaining test-specific server configurations.

3. **Longer Feedback Cycles**:
   - Slower compared to unit tests, which may impact rapid iterations.

## **Alternatives Considered**

1. **Cypress for E2E Tests**:

   - Pros:
     - Rich GUI for debugging.
   - Cons:
     - Requires a separate toolchain, increasing complexity for Python projects.

2. **Selenium**:

   - Pros:
     - Well-established tool for browser automation.
   - Cons:
     - Slower and less modern compared to Playwright.

3. **No E2E Tests**:
   - Pros:
     - Faster development cycles.
   - Cons:
     - Higher risk of undetected integration issues.

## **Decision Outcome**

By using Playwright for E2E testing with Python, we ensure robust integration testing with minimal disruption to the existing development workflow. The integration with pytest provides flexibility and aligns with existing testing practices.
