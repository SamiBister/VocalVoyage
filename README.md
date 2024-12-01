# VocabVoyage

VocabVoyage is a language learning application designed to help kids learn vocabulary through interactive quizzes. The app supports translation between languages and provides a fun and engaging way to expand language skills.

## Purpose

This was developed to provide learning app for my daughter, The Girl.

As secondary purpose this is POC for following things:

- UV for managing python dependencies and virtualenv.
  - UV tooling for the pipelines
- FastAPI for backend
- NextJS for frontend
- Clean code structure for the python backend
- ChatGPT generated boilerplate.
- Test fully automated document generation

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

- **UV** for python
- **Node.js** and **npm**

### Backend Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/SamiBister/VocabVoyage.git
   cd VocabVoyage
   ```

2. **Set Up Virtual Environment**

   ```bash
   uv venv & uv sync
   source venv/bin/activate,sh   # On Windows use `venv\Scripts\activate`
   ```

3. **Run Unit Tests**

   ```bash
   uv python -m pytest tests --cov
   ```

4. **Start the Backend Server**

   ```bash
   uv run uvicorn app.main:app --reload
   ```

   The backend server will start at `http://localhost:8000`.

   The backend server swaggers documentation is at `http://localhost:8000/docs`.

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
   NEXT_PUBLIC_API_URL=http://localhost:8000
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

Run the following command to run the backend tests:

```bash
uv run pytest -v --durations=0 --cov --cov-report=xml
```

### Frontend

TBA

```bash
npm run test
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

   - The backend will be accessible at: [http://localhost:3000/](http://localhost:3000/).
   - The frontend will be accessible at: [http://localhost:3000/](http://localhost:3000/).

## **Uploading a New Questionnaire File**

The application supports uploading questionnaire files to update or add new question sets.

### **Steps to Upload a Questionnaire File**

1. Prepare your questionnaire file in the required format:

   - File type: CSV file.
   - Ensure it follows the structure:

     ```csv

     ```

Foreing,Native
Omena,Apple
Koulu,Sc
```

2. Access the Upload Feature:
   - Open app
     - Go to the URL [http://localhost:3000/](http://localhost:3000/)
   - Press the **Choose file** button.
   - Press the **Upload files** button.
