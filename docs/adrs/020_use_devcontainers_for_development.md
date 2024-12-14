# **ADR: Use Development Containers (DevContainers)**

## **Context**

The development process for our projects, which include a **Python backend** and a **Next.js frontend**, requires a consistent and reliable environment for developers. Historically, issues such as environment conflicts, onboarding delays, and dependency mismatches have impacted productivity and collaboration.

To address these issues, we aim to standardize the development environment using **DevContainers**. DevContainers provide a containerized development environment that can be version-controlled, shared across teams, and used in a variety of editors, including VS Code, JetBrains, and Neovim.

1. **Standardize Development Environments**:

   - Ensure all developers work in the same environment regardless of their host machine.
   - Reduce dependency conflicts between projects by isolating the environment.

2. **Version-Controlled Configuration**:

   - Development environment configurations are stored as code in the repository.
   - Changes to the environment can be proposed, reviewed, and versioned through pull requests.

3. **Ease of Onboarding**:

   - New developers can start working with minimal setup by simply cloning the repository and opening it in VS Code, JetBrains, or using Neovim with the container.

4. **Cross-Editor Compatibility**:

   - Works seamlessly with Visual Studio Code, JetBrains IDEs, and Neovim (with support for tmux and plugins inside the container).

5. **Support for Playwright and End-to-End Testing**:

   - The DevContainer includes all necessary dependencies to run Playwright tests alongside unit tests and integration tests.

6. **Browser-Based Development**:

   - Can be used with **GitHub Codespaces** or other cloud-based development tools, enabling browser-based development.

7. **Python Backend and Next.js Frontend**:

   - Supports running both the Python backend and the Next.js frontend concurrently within the container.

8. **Host Isolation**:
   - Isolates development dependencies from the host machine, reducing the risk of conflicts and ensuring consistent builds.ß

---

## **Decision**

We will adopt **DevContainers** for our development environment. This setup will:

---

## **Implementation**

### **1. DevContainer Setup**

1. **Directory Structure**:

   - Add a `.devcontainer/` directory to the repository with the following files:
     - `devcontainer.json`: Configuration file for the DevContainer.
     - `Dockerfile`: Defines the container's base image and tools.

2. **Key Features**:
   - Python and Node.js environments for backend and frontend development.
   - Tools for running tests, including Playwright for end-to-end tests.
   - Neovim, tmux, and shell utilities for advanced workflows.

**`devcontainer.json`**:

```json
{
  "name": "Fullstack DevContainer",
  "dockerFile": "Dockerfile",
  "context": "..",
  "mounts": ["source=${localWorkspaceFolder},target=/workspace,type=bind"],
  "workspaceFolder": "/workspace",
  "settings": {
    "terminal.integrated.defaultProfile.linux": "fish",
    "editor.formatOnSave": true
  },
  "extensions": [
    "ms-vscode.vscode-typescript-next",
    "esbenp.prettier-vscode",
    "ms-python.python",
    "ms-playwright.playwright",
    "neovim.neovim"
  ],
  "postCreateCommand": "uv sync",
  "remoteUser": "vscode"
}
```

**`Dockerfile`**:

```dockerfile
FROM mcr.microsoft.com/devcontainers/base:ubuntu

RUN apt-get update && apt-get install -y \
    fish \
    neovim \
    curl \
    git \
    tmux \
    build-essential \
    python3-pip \
    nodejs \
    npm \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install uv for Python environment management
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Set fish as the default shell
RUN chsh -s /usr/bin/fish vscode

WORKDIR /workspace
```

---

### **2. Key Features**

1. **Environment Isolation**:

   - All development dependencies are installed in the container.
   - Host system is unaffected by the development environment.

2. **Testing Support**:

   - All tests, including Playwright E2E tests, can run inside the container:
     - Python tests are executed with `pytest`.
     - Frontend tests and Playwright E2E tests are run using `npm test` and `npx playwright test`.

3. **Frontend and Backend Support**:

   - The Python backend runs on port `8000`.
   - The Next.js frontend runs on port `3000`.
   - Both services can be started concurrently within the container.

4. **Neovim and Tmux**:
   - Neovim is pre-installed with support for plugins.
   - Tmux is available for advanced terminal workflows.

---

## **Consequences**

### **Positive Consequences**

1. **Consistent Development Environment**:
   - All developers work in an identical environment, reducing "it works on my machine" issues.
2. **Ease of Collaboration**:
   - Changes to the environment are version-controlled and reviewed through pull requests.
3. **Reduced Onboarding Time**:
   - New team members can start contributing with minimal setup.
4. **Dependency Management**:
   - Dependencies are isolated, avoiding conflicts with other projects on the host machine.
5. **Cross-Editor Compatibility**:
   - Developers can use their preferred editor or IDE (VS Code, JetBrains, Neovim).
6. **Browser-Based Development**:
   - Fully compatible with GitHub Codespaces for cloud-based development.

### **Negative Consequences**

1. **Initial Setup Effort**:
   - Requires some effort to define and configure the container for the first time.
2. **Performance Overhead**:
   - Running a containerized environment may have slight performance overhead compared to native development.
3. **Learning Curve**:
   - Developers unfamiliar with containerized environments may require time to adapt.

---

## **Alternatives Considered**

1. **Local Development Without Containers**:

   - Pros:
     - No performance overhead.
   - Cons:
     - Leads to dependency conflicts and inconsistent environments across developers.

2. **Vagrant or Other Virtual Machines**:

   - Pros:
     - Provides similar isolation.
   - Cons:
     - Heavier and slower than containers; less integration with modern tools like GitHub Codespaces.

3. **GitHub Codespaces Only**:
   - Pros:
     - Fully cloud-based, no local setup required.
   - Cons:
     - Not ideal for developers who prefer local workflows.

---

## **Decision Outcome**

By adopting DevContainers, we ensure a streamlined and standardized development process. The environment supports both local and cloud-based workflows, reduces onboarding time, and eliminates dependency conflicts, enhancing team productivity and collaboration.
