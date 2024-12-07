import subprocess
import time
import pytest
import os


@pytest.fixture(scope="session", autouse=True)
def start_test_environment():
    """
    Starts the Python backend and Next.js frontend servers before running tests
    and shuts them down afterward.
    """
    # Resolve paths relative to the root of the project
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    frontend_dir = os.path.join(root_dir, "frontend")
    # Start the backend server
    backend_process = subprocess.Popen(
        [
            "uvicorn",
            "app.main:app",
            "--reload",
        ],  # Adjust if your backend entry point differs
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=root_dir,
    )

    # Start the frontend server
    frontend_process = subprocess.Popen(
        ["npm", "run", "dev"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=frontend_dir,
    )

    # Wait for both servers to start
    time.sleep(10)  # Adjust based on startup times of your servers

    yield  # Tests run here

    # Stop the servers after tests
    backend_process.terminate()
    backend_process.wait()
    frontend_process.terminate()
    frontend_process.wait()
