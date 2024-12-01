# app/use_cases/word_service.py
"""This module contains the WordService class, which encapsulates the business logic for the VocabVoyage quiz application.

Classes
-------
WordService

Usage of internal imports
-------------------------
- app.domain.models: QuizMode, QuizResult, Word
- app.interfaces.logger: QuizLogger

Attributes
----------
all_words : List[Word]
    List of all words for the quiz.
logger : QuizLogger
    Logger for recording quiz results.
correct : int
    Number of correct answers.
incorrect : int
    Number of incorrect answers.
incorrect_words : List[str]
    List of incorrectly answered words.
correct_words : List[str]
    List of correctly answered words.
start_time : datetime
    Start time of the quiz.
mode : QuizMode
    Current quiz mode.
word_queue : List[Word]
    Queue of words for the quiz.
current_word_index : int
    Index of the current word in the queue.
repeat_incorrect_count : dict
    Counter for how many times each word was answered incorrectly.

Methods
-------
__init__(words: List[Word], logger: QuizLogger)
    Initializes the WordService with a list of words and a logger.
reset_quiz()
    Resets the quiz state.
set_mode(mode: str)
    Sets the quiz mode.
end_quiz()
    Ends the quiz session and logs the results.
get_next_word() -> Optional[Word]
    Returns the next word based on the quiz mode.
_get_next_word_normal() -> Optional[Word]
    Logic for normal mode.
_get_next_word_infinite() -> Optional[Word]
    Logic for infinite mode.
check_answer(word: Word, user_input: str) -> bool
    Checks if the user's input matches the foreign term and updates quiz statistics accordingly.
increment_incorrect_repeat(word: Word)
    Increments the counter for how many times the user has written the incorrect term.
update_words(new_words: List[Word])
    Updates the word list with new words.
"""

import random
from datetime import datetime
from typing import List, Optional

from app.domain.models import QuizMode, QuizResult, Word
from app.interfaces.logger import QuizLogger


class WordService:
    """Contains the business logic for the VocabVoyage quiz application."""

    def __init__(self, words: List[Word], logger: QuizLogger):
        """Initializes the WordService with a list of words and a logger.

        Parameters
        ----------
        words : List[Word]
            A list of Word objects to be used in the quiz.
        logger : QuizLogger
            A logger instance for logging quiz activities.
        """

        self.all_words = words
        self.logger = logger
        self.reset_quiz()

    def reset_quiz(self):
        """Resets the quiz state to its initial configuration.

        This method performs the following actions:
        - Sets the count of correct answers to zero.
        - Sets the count of incorrect answers to zero.
        - Clears the list of incorrect words.
        - Clears the list of correct words.
        - Records the current time as the start time of the quiz.
        - Sets the quiz mode to NORMAL.
        - Copies all words to the word queue and shuffles them.
        - Resets the current word index to -1, which will be incremented when fetching the next word.
        - Initializes a dictionary to track the number of times each word was answered incorrectly.
        """
        self.correct = 0
        self.incorrect = 0
        self.incorrect_words = []
        self.correct_words = []
        self.start_time = datetime.now()
        self.mode = QuizMode.NORMAL
        self.word_queue = self.all_words.copy()
        random.shuffle(self.word_queue)
        self.current_word_index = -1  # Will be incremented in get_next_word()
        self.repeat_incorrect_count = {}  # Track how many times the user wrote incorrect terms

    def set_mode(self, mode: str):
        """Sets the quiz mode."""
        self.mode = QuizMode(mode)
        self.reset_quiz()

    def end_quiz(self):
        """Ends the quiz session, calculates the results, and logs them.

        This method captures the end time of the quiz, creates a QuizResult object
        containing the number of correct and incorrect answers, the lists of correct
        and incorrect words, and the start and end times of the quiz. It then logs
        the result using the logger.

        Parameters
        ----------
        correct : int
            The number of correct answers.
        incorrect : int
            The number of incorrect answers.
        correct_words : list
            The list of correctly answered words.
        incorrect_words : list
            The list of incorrectly answered words.
        start_time : datetime
            The start time of the quiz session.
        logger : Logger
            The logger instance used to log the quiz results.
        """
        end_time = datetime.now()
        result = QuizResult(
            correct=self.correct,
            incorrect=self.incorrect,
            correct_words=list(set(self.correct_words)),
            incorrect_words=list(set(self.incorrect_words)),
            start_time=self.start_time,
            end_time=end_time,
        )
        self.logger.log_result(result)

    def get_next_word(self) -> Optional[Word]:
        """Retrieves the next word based on the current quiz mode.

        Returns
        -------
        Optional[Word]
            The next word to be used in the quiz. Returns a Word object if a word is available,
            otherwise returns None.

        Raises
        ------
        None
        """
        if self.mode == QuizMode.NORMAL:
            return self._get_next_word_normal()
        elif self.mode == QuizMode.INFINITE:
            return self._get_next_word_infinite()
        else:
            return None

    def _get_next_word_normal(self) -> Optional[Word]:
        """Retrieve the next word in the queue for normal mode.

        In normal mode, the user is presented with words sequentially.
        If the user answers incorrectly, it is simply marked as wrong in the results.

        Returns
        -------
        Optional[Word]
            The next word in the queue if available, otherwise None.
        """
        self.current_word_index += 1
        if self.current_word_index < len(self.word_queue):
            return self.word_queue[self.current_word_index]
        else:
            return None  # No more words left

    def _get_next_word_infinite(self) -> Optional[Word]:
        """Retrieve the next word in the queue for infinite mode.

        In infinite mode, the user is presented with words sequentially.
        If the user answers incorrectly, it is returned to queue for repetition.

        Returns
        -------
        Optional[Word]
            The next word in the queue if available, otherwise None.
        """
        if self.current_word_index + 1 < len(self.word_queue):
            self.current_word_index += 1
            return self.word_queue[self.current_word_index]
        elif self.incorrect_words:
            # Reset the queue with incorrect words
            self.word_queue = [
                Word(foreign_term=word, native_translation="")
                for word in self.incorrect_words
            ]
            self.incorrect_words = []
            self.current_word_index = 0
            return self.word_queue[self.current_word_index]
        else:
            return None  # All words answered correctly

    def check_answer(self, word: Word, user_input: str) -> bool:
        """Check if the user's input matches the foreign term of the given word.

        Parameters
        ----------
        word : Word
            The word object containing the foreign term to be checked.
        user_input : str
            The user's input to be compared with the foreign term.

        Returns
        -------
        bool
            True if the user's input matches the foreign term, False otherwise.

        Side Effects
        ------------
        - Increments the correct answer count and appends the foreign term to
          the correct_words list if the answer is correct.
        - Increments the incorrect answer count and appends the foreign term to
          the incorrect_words list if the answer is incorrect.
        - Removes the foreign term from repeat_incorrect_count if the answer is
          correct and it exists in the dictionary.
        - Initializes the repeat_incorrect_count for the foreign term to 0 if
          the answer is incorrect.
        """
        is_correct = word.foreign_term.strip().lower() == user_input.strip().lower()
        if is_correct:
            self.correct += 1
            self.correct_words.append(word.foreign_term)
            if word.foreign_term in self.repeat_incorrect_count:
                del self.repeat_incorrect_count[word.foreign_term]
        else:
            self.incorrect += 1
            self.incorrect_words.append(word.foreign_term)
            self.repeat_incorrect_count[word.foreign_term] = 0  # Initialize counter
        return is_correct

    def increment_incorrect_repeat(self, word: Word):
        """Increments the counter for the number of times the user has written the incorrect term for a given word.

        Parameters
        ----------
        word : Word
            The word object containing the foreign term to be incremented.

        Returns
        -------
        int
            The updated count of incorrect repetitions for the given foreign term.
            Returns 0 if the foreign term is not found in the repeat_incorrect_count dictionary.
        """
        if word.foreign_term in self.repeat_incorrect_count:
            self.repeat_incorrect_count[word.foreign_term] += 1
            return self.repeat_incorrect_count[word.foreign_term]
        else:
            return 0  # Should not happen

    def update_words(self, new_words: List[Word]):
        """Updates the internal word list with a new set of words and resets the quiz.

        Parameters
        ----------
        new_words : List[Word]
            A list of Word objects to update the internal word list with.

        Returns
        -------
        None
        """
        self.all_words = new_words
        self.reset_quiz()
