# VocabVoyage

VocabVoyage is a language learning application designed to help kids learn vocabulary through interactive quizzes. The app supports translation between languages and provides a fun and engaging way to expand language skills.

## Purpose

This was developed to provide learning app for my daughter, The Girl.

As secondary purpose this is showcase for tech that I find useful and improve development experience.

- UV for managing python dependencies and virtualenv.
  - UV tooling for the pipelines
  - Ruff for linting and formatting
  - Github actions for CI/CD with UV and Ruff
- FastAPI for backend
- NextJS for frontend
- Clean code structure for the python backend
- ChatGPT generated boilerplate.
- Test fully automated document generation
- Playwright for end-to-end testing
- Devlopment container for consistent development environment
  - Add tmux and neovim for development container, to enable nvim development inside tmux

## Features

- **Two Quiz Modes**:
  - **Normal Mode**: Asks all terms once in random order, then provides statistics at the end.
  - **Infinite Mode**: Repeats incorrectly answered terms until all are answered correctly.
- **Write Incorrect Terms**: Users must write incorrect terms three times before proceeding.
- **Statistics**: Tracks correct and incorrect answers, providing feedback at the end of quizzes.
- **Logging**: Logs quiz results in Markdown files for review.
- **Internationalization**: Frontend UI is translatable, supporting multiple languages.
- **Clean Architecture**: Structured following clean architecture principles for maintainability.
- Architectural decions recorded in the `docs/adr` folder.

## Documentation

Documents can be found in `docs` folder.

## Project Structure

```plaintext
VocabVoyage/
├── app/                  # Backend FastAPI application
├── frontend/             # Frontend Next.js application
├── setup.py              # Packaging script for the backend
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
```

## Getting Started

### Prerequisites

- **Git**
- **Docker**
- **Visual Studio Code** with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) or **JetBrains IDE** with DevContainer support

### Preferred Development Setup

We recommend using DevContainers for development to ensure a consistent and isolated environment across all contributors.

1. **Clone the Repository**

   ```bash
   git clone https://github.com/SamiBister/VocabVoyage.git
   cd VocabVoyage
   ```

2. **Open with DevContainer**

- VS Code:
  - Install the Dev Containers extension.
  - Open the project folder in VS Code.
  - When prompted, reopen the folder in the container.
- JetBrains IDE:
  - Install JetBrains Gateway:
    - Install JetBrains Gateway (if you don’t have a full IDE installed) from JetBrains Gateway.
    - Enable Remote Development:
  - Open your JetBrains IDE or Gateway.
    - Connect to the Docker-based DevContainer by following the JetBrains Docker Setup Guide.
  - Start Developing

#### Developement with nvim and tmux

##### Plan

1, Build the dev container image 2. Run container with workspace mount 3. Connect to container 4. Start tmux session
5, Use neovim inside tmux

##### Steps

1. Build image:

```bash
```bash
docker build --platform linux/amd64 -t devenv -f .devcontainer/Dockerfile .
```

```


2. Run container:

```bash
docker run -it --rm \
  --name dev_session \
  -v $(pwd):/workspace \
  -w /workspace \
  -p 3000:3000 \
  -p 8000:8000 \
  devenv \
  fish
```

3. Initialize the workspace:

```bash
uv sync && uv run playwright install --with-deps chromium
```

4. Start tmux session:

```bash
tmux new-session -s dev
```

5. Use neovim inside tmux:

```bash
cd workspace
nvim .
```

6. Common tmux/nvim commands:

```bash
# Inside tmux:
Ctrl+b c     # new window
Ctrl+b "     # split horizontal
Ctrl+b %     # split vertical
Ctrl+b [0-9] # switch window
nvim .       # open neovim in current directory
```

Remember:

Ctrl+b is tmux prefix
Ctrl+b d detaches from tmux session
tmux attach -t dev reattaches to session

### Alternative Setup

If you choose not to use DevContainers, ensure you have UV for Python, Node.js, and npm installed. Follow the manual setup instructions for the

#### Prerequisites

- **UV** for python
- **Node.js** and **npm**

#### Clone the Repository

1. **Clone the Repository**

```bash
git clone https://github.com/SamiBister/VocabVoyage.git
cd VocabVoyage
```

### Backend Setup

1. **Set Up Virtual Environment**

   ```bash
   uv venv & uv sync
   source venv/bin/activate,sh   # On Windows use `venv\Scripts\activate`
   ```

2. **Run Unit Tests**

   ```bash
   uv python -m pytest tests --cov
   ```

3. **Start the Backend Server**

   ```bash
   uv run uvicorn app.main:app --reload
   ```

   The backend server will start at `http://localhost:8000/api`.

   The backend server swaggers documentation is at `http://localhost:8000/api/docs`.

### Frontend Setup

1. **Navigate to Frontend Directory**

   ```bash
   cd frontend
   ```

2. **Install Dependencies**

   ```bash
   npm install
   ```

3. **Create Environment File**

   Create a `.env.local` file in the `frontend` directory:

   ```env
   NEXT_PUBLIC_API_URL=http://localhost:8000/api
   ```

4. **Start the Frontend Server**

   ```bash
   npm run dev
   ```

   The frontend app will start at `http://localhost:3000`.

## Usage

1. **Access the App**

   Open your browser and navigate to `http://localhost:3000`.

2. **Select Quiz Mode**

   - Choose between **Normal Mode** and **Infinite Mode** from the dropdown menu.

3. **Start a Quiz**

   - Click on **"Start Quiz"** to begin.
   - A word in your native language will be displayed.
   - Enter the translation in the foreign language.

4. **Submit Answers**

   - Click **"Submit Answer"** after typing your answer.
   - Immediate feedback is provided.
   - Incorrect answers require you to write the correct term three times before proceeding.

5. **End the Quiz**

   - Click **"End Quiz"** to finish the session.
   - Statistics and incorrectly answered terms are displayed.
   - Quiz results are logged in the `app/out/` folder as Markdown files.

## Customization

### Adding Words

- Add your own CSV files to `app/data/` with the format:

  ```csv
  ForeignTerm,NativeTranslation
  ```

### Translations

- Update or add translation files in `frontend/locales/` for additional languages.

## Project Structure Details

- **app/**: Contains the FastAPI backend application.

  - **domain/**: Business models.
  - **use_cases/**: Business logic and services.
  - **interfaces/**: Repositories and loggers.
  - **data/**: CSV files with words.
  - **out/**: Output folder for quiz result logs.
  - **tests/**: Unit tests for backend components.
  - **translations/**: Translation files for the backend (if needed).

- **frontend/**: Contains the Next.js frontend application.
  - **pages/**: Next.js pages.
  - **locales/**: Translation files for the frontend.

## Update documentation

Run the following command to update the documentation:

```bash
sh ./document.sh
```

or in fish shell

```fish
fish ./document.fish
```

It is mandatory to run this before each push to remote.

## Linting

### Backend

Run the following command to lint the backend code:

```bash
uvx ruff check --select I --fix
uvx ruff format --check .
```

### Frontend

Run the following command to lint the frontend code:

```bash
npm run lint
```

## Testing

### Backend

Run the following command to run the backend unit tests:

```bash
uv run pytest -m unit -vvvv --durations=0 --cov --cov-report=xml
```

### Frontend

Run the following for the frontend unit tests:

```bash
npm run test
```

### End-to-end tests

Run the following command to run the backend unit tests:

```bash
uv run pytest -m e2e -vvvv --durations=0 --cov --cov-report=xml
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Author**: Sami Bister

---

I hope this provides everything you need to get started with **VocabVoyage**. If you have any further questions or need assistance with specific parts of the code, feel free to ask!

It sounds like your README file needs to be updated to include instructions on:

1. **Starting the application with the new scripts.**
2. **Uploading a new questionnaire file.**

Here’s how you can revise and expand the README to include these sections:

---

## **How to Start the Application**

The application uses new scripts for starting the backend and frontend services.

1. Ensure you have UV installed
2. Ensure you have Node.js and npm/yarn installed.
3. Start frontend and backend services using the following steps:

   ```bash
   ./start-dev.sh
   ```

   - The backend will be accessible at: [http://localhost:8000/api](http://localhost:8000/api).
   - The frontend will be accessible at: [http://localhost:3000/](http://localhost:3000/).

## **Uploading a New Questionnaire File**

The application supports uploading questionnaire files to update or add new question sets.

### **Steps to Upload a Questionnaire File**

1. Prepare your questionnaire file in the required format:

   - File type: CSV file.
   - Ensure it follows the structure:

```csv
Foreing,Native
Omena,Apple
Koulu,Sc
```

1. Access the Upload Feature:
   - Open app
     - Go to the URL [http://localhost:3000/](http://localhost:3000/)
   - Press the **Choose file** button.
   - Press the **Upload files** button.

```
