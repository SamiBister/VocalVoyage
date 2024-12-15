# app/main.py
"""
VocabVoyage API

This module sets up the FastAPI application for the VocabVoyage project. It includes
endpoints for setting quiz modes and handling user answers. The application uses
various internal modules and services to manage words and log quiz activities.

Internal Imports:
- app.domain.models: Contains the Word and QuizMode models.
- app.interfaces.logger: Provides the QuizLogger for logging quiz activities.
- app.interfaces.repositories: Contains the WordRepository for managing word data.
- app.use_cases.word_service: Provides the WordService for word-related operations.
"""

import os
import shutil
import uuid
from typing import List, Optional

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.domain.models import Word
from app.interfaces.logger import QuizLogger
from app.interfaces.repositories import WordRepository
from app.use_cases.word_service import WordService

app = FastAPI(title="VocabVoyage", root_path="/api")

# CORS middleware to allow frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the exact origin(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load words at startup
word_repo = WordRepository()
words = word_repo.load_words()
quiz_logger = QuizLogger()
word_service = WordService(words, quiz_logger)


class AnswerRequest(BaseModel):
    """
    Request model for submitting an answer.

    Attributes
    ----------
    word : Word
        The word object of the questioner.
    user_input : str
        The user's input for the word.
    """

    word: Word
    user_input: str


class ModeRequest(BaseModel):
    """
    Request model for setting the quiz mode.

    Attributes
    ----------
        mode (str): The quiz mode, either 'normal' or 'infinite'.
    """

    mode: str  # 'normal' or 'infinite'


@app.post("/set_mode/")
async def set_mode(request: ModeRequest):
    """
    Sets the quiz mode.

    Parameters
    ----------
    request : ModeRequest
        The request containing the desired mode.

    Raises
    ------
    HTTPException
        If the mode is not 'normal' or 'infinite'.

    Returns
    -------
    JSONResponse
        A response indicating the mode has been set.
    """
    if request.mode not in ["normal", "infinite"]:
        raise HTTPException(status_code=400, detail="Invalid mode")
    word_service.set_mode(request.mode)
    return {"message": f"Quiz mode set to {request.mode}"}


@app.post("/start_quiz/")
async def start_quiz():
    """
    Endpoint to start a new quiz session.

    This endpoint resets the current quiz session and starts a new one. It clears any
    previous quiz data and prepares the system for a new quiz session. This can be
    useful when a user wants to restart the quiz from the beginning.

    Returns
    -------
        JSONResponse: A response indicating that the quiz has started.
    """
    word_service.reset_quiz()
    return {"message": "Quiz started"}


@app.post("/end_quiz/")
async def end_quiz():
    """
    Endpoint to end the current quiz session and log the results.

    This endpoint marks the end of the current quiz session. It triggers the logging
    of the quiz results, including the number of correct and incorrect answers, and
    any other relevant statistics. This can be useful for tracking user performance
    and providing feedback.

    Returns
    -------
        JSONResponse: A response indicating that the quiz has ended and results have been logged.
    """
    word_service.end_quiz()
    return {"message": "Quiz ended and results logged"}


@app.get("/words/next", response_model=Optional[Word])
async def get_next_word():
    """
    Endpoint to retrieve the next word in the quiz.

    Returns
    -------
        Optional[Word]: The next word in the quiz, or None if there are no more words.
    """
    word = word_service.get_next_word()
    if word is None:
        return JSONResponse(content=None, status_code=200)
    return word


@app.post("/check/", response_model=dict)
async def check_answer(answer: AnswerRequest):
    """
    Check if the user's answer is correct.

    Parameters
    ----------
    answer : AnswerRequest
        The user's answer request containing the word and user input.

    Returns
    -------
    dict
        A dictionary with a key 'is_correct' indicating whether the user's answer is correct.
    """
    is_correct = word_service.check_answer(answer.word, answer.user_input)
    return {"is_correct": is_correct}


@app.get("/results/", response_model=dict)
async def get_results():
    """
    Endpoint to get current quiz statistics.
    """
    return {
        "correct": word_service.correct,
        "incorrect": word_service.incorrect,
        "incorrect_words": word_service.incorrect_words,
    }


@app.post("/upload_words/")
async def upload_words(files: List[UploadFile] = File(...)):
    """
    Endpoint to upload new word files.

    This endpoint allows users to upload new word files in CSV format. It clears any
    existing word files in the data directory and replaces them with the newly uploaded
    files. The words from the new files are then loaded into the system.

    Parameters
    ----------
    files : List[UploadFile]
        A list of uploaded files. Each file must be in CSV format.

    Raises
    ------
    HTTPException
        If any of the uploaded files is not a CSV file.

    Returns
    -------
    dict
        A message indicating that the word files have been uploaded and the word list has been updated.
    """
    data_directory = "app/data"
    # Clear existing files in the data directory
    for filename in os.listdir(data_directory):
        file_path = os.path.join(data_directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # Save the uploaded files
    for file in files:
        # Check if filename is not None
        if not file.filename:
            # Assign a default unique filename
            filename = f"{uuid.uuid4()}.csv"
        else:
            filename = os.path.basename(file.filename)

        # Ensure the uploaded file is a .csv file
        if not filename.endswith(".csv"):
            raise HTTPException(status_code=400, detail="Only .csv files are allowed")

        file_location = os.path.join(data_directory, filename)
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)

    # Reload the words from the new files
    word_repo = WordRepository()
    words = word_repo.load_words()
    word_service.update_words(words)

    return {"message": "Word files uploaded and word list updated"}
