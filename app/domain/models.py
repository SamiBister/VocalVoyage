"""
This module defines the data models used in the VocabVoyage application.

# app/domain/models.py

Classes:
    QuizMode (Enum): An enumeration representing the different modes of a quiz.
        - NORMAL: Standard quiz mode.
        - INFINITE: Endless quiz mode.

    Word (BaseModel): A Pydantic model representing a word with its foreign term and native translation.
        Attributes:
            foreign_term (str): The word in the foreign language.
            native_translation (str): The translation of the word in the native language.

    QuizResult (BaseModel): A Pydantic model representing the result of a quiz attempt.
        Attributes:
            correct (int): The number of correct answers.
            incorrect (int): The number of incorrect answers.
            correct_words (List[str]): A list of words that were answered correctly.
            incorrect_words (List[str]): A list of words that were answered incorrectly.
            start_time (datetime): The start time of the quiz.
            end_time (datetime): The end time of the quiz.
"""
from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel


class QuizMode(str, Enum):
    """
    QuizMode: A class that defines an mode of the quiz.

    Enum representing different quiz modes.
    Attributes:
        NORMAL (str): Represents the normal quiz mode.
        INFINITE (str): Represents the infinite quiz mode.
    """

    NORMAL = "normal"
    INFINITE = "infinite"


class Word(BaseModel):
    """
    Represents a word with its foreign term and native translation.
    
    Attributes:
        foreign_term (str): The word in the foreign language.
        native_translation (str): The translation of the foreign term in the native language.

    """

    foreign_term: str
    native_translation: str


class QuizResult(BaseModel):
    """
    Represents the result of a quiz attempt.

    Attributes:
        correct (int): The number of correct answers.
        incorrect (int): The number of incorrect answers.
        correct_words (List[str]): A list of words that were answered correctly.
        incorrect_words (List[str]): A list of words that were answered incorrectly.
        start_time (datetime): The timestamp when the quiz attempt started.
        end_time (datetime): The timestamp when the quiz attempt ended.

    """

    correct: int
    incorrect: int
    correct_words: List[str]
    incorrect_words: List[str]
    start_time: datetime
    end_time: datetime
