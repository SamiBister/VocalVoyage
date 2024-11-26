# app/use_cases/word_service.py

import random
from datetime import datetime
from typing import List, Optional

from app.domain.models import QuizMode, QuizResult, Word
from app.interfaces.logger import QuizLogger


class WordService:
    """
    Contains the business logic for the VocabVoyage quiz application.
    """

    def __init__(self, words: List[Word], logger: QuizLogger):
        self.all_words = words
        self.logger = logger
        self.reset_quiz()

    def reset_quiz(self):
        """
        Resets the quiz state.
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
        self.repeat_incorrect_count = (
            {}
        )  # Track how many times the user wrote incorrect terms

    def set_mode(self, mode: str):
        """
        Sets the quiz mode.
        """
        self.mode = QuizMode(mode)
        self.reset_quiz()

    def end_quiz(self):
        """
        Ends the quiz session and logs the results.
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
        """
        Returns the next word based on the quiz mode.
        """
        if self.mode == QuizMode.NORMAL:
            return self._get_next_word_normal()
        elif self.mode == QuizMode.INFINITE:
            return self._get_next_word_infinite()
        else:
            return None

    def _get_next_word_normal(self) -> Optional[Word]:
        """
        Logic for normal mode.
        """
        self.current_word_index += 1
        if self.current_word_index < len(self.word_queue):
            return self.word_queue[self.current_word_index]
        else:
            return None  # No more words left

    def _get_next_word_infinite(self) -> Optional[Word]:
        """
        Logic for infinite mode.
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
        """
        Checks if the user's input matches the foreign term.
        Updates quiz statistics accordingly.
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
        """
        Increments the counter for how many times the user has written the incorrect term.
        """
        if word.foreign_term in self.repeat_incorrect_count:
            self.repeat_incorrect_count[word.foreign_term] += 1
            return self.repeat_incorrect_count[word.foreign_term]
        else:
            return 0  # Should not happen

    def update_words(self, new_words: List[Word]):
        """
        Updates the word list with new words.
        """
        self.all_words = new_words
        self.reset_quiz()
