# app/main.py

from typing import Optional

from app.domain.models import Word
from app.interfaces.logger import QuizLogger
from app.interfaces.repositories import WordRepository
from app.use_cases.word_service import WordService
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(title="VocabVoyage")

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
    word: Word
    user_input: str


class ModeRequest(BaseModel):
    mode: str  # 'normal' or 'infinite'


@app.post("/set_mode/")
async def set_mode(request: ModeRequest):
    """
    Sets the quiz mode.
    """
    if request.mode not in ["normal", "infinite"]:
        raise HTTPException(status_code=400, detail="Invalid mode")
    word_service.set_mode(request.mode)
    return {"message": f"Quiz mode set to {request.mode}"}


@app.post("/start_quiz/")
async def start_quiz():
    """
    Endpoint to start a new quiz session.
    """
    word_service.reset_quiz()
    return {"message": "Quiz started"}


@app.post("/end_quiz/")
async def end_quiz():
    """
    Endpoint to end the current quiz session and log the results.
    """
    word_service.end_quiz()
    return {"message": "Quiz ended and results logged"}


@app.get("/words/next", response_model=Optional[Word])
async def get_next_word():
    """
    Endpoint to retrieve the next word in the quiz.
    """
    word = word_service.get_next_word()
    if word is None:
        return JSONResponse(content=None, status_code=200)
    return word


@app.post("/check/", response_model=dict)
async def check_answer(answer: AnswerRequest):
    """
    Endpoint to check if the user's answer is correct.
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
