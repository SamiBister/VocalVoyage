# app/domain/models.py

from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel


class QuizMode(str, Enum):
    NORMAL = "normal"
    INFINITE = "infinite"


class Word(BaseModel):
    """
    Represents a word with its foreign term and native translation.
    """

    foreign_term: str
    native_translation: str


class QuizResult(BaseModel):
    """
    Represents the result of a quiz attempt.
    """

    correct: int
    incorrect: int
    correct_words: List[str]
    incorrect_words: List[str]
    start_time: datetime
    end_time: datetime
