# app/tests/test_word_service.py

import unittest
from unittest.mock import MagicMock

from app.domain.models import Word
from app.interfaces.logger import QuizLogger
from app.use_cases.word_service import WordService


class TestWordService(unittest.TestCase):
    def setUp(self):
        self.words = [
            Word(foreign_term="Hello", native_translation="Hei"),
            Word(foreign_term="World", native_translation="Maailma"),
        ]
        self.mock_logger = MagicMock(spec=QuizLogger)
        self.service = WordService(self.words, self.mock_logger)

    def test_get_next_word_normal(self):
        self.service.set_mode("normal")
        words_asked = []
        while True:
            word = self.service.get_next_word()
            if word is None:
                break
            words_asked.append(word)
            self.service.check_answer(
                word, word.foreign_term
            )  # Simulate correct answers

        self.assertEqual(len(words_asked), len(self.words))
        self.assertEqual(self.service.correct, len(self.words))
        self.assertEqual(self.service.incorrect, 0)

    def test_get_next_word_infinite(self):
        self.service.set_mode("infinite")
        words_asked = []
        for _ in range(3):  # Simulate answering incorrectly three times
            word = self.service.get_next_word()
            if word is None:
                break
            words_asked.append(word)
            self.service.check_answer(word, "Wrong")  # Always incorrect

        self.assertGreaterEqual(len(words_asked), len(self.words))
        self.assertEqual(self.service.correct, 0)
        self.assertEqual(self.service.incorrect, len(words_asked))

    def test_check_answer_correct(self):
        word = self.words[0]
        result = self.service.check_answer(word, "Hello")
        self.assertTrue(result)
        self.assertEqual(self.service.correct, 1)
        self.assertEqual(self.service.incorrect, 0)

    def test_check_answer_incorrect(self):
        word = self.words[0]
        result = self.service.check_answer(word, "Hi")
        self.assertFalse(result)
        self.assertEqual(self.service.correct, 0)
        self.assertEqual(self.service.incorrect, 1)
        self.assertIn("Hello", self.service.incorrect_words)

    def test_increment_incorrect_repeat(self):
        word = self.words[0]
        self.service.check_answer(word, "Hi")  # Incorrect
        count = self.service.increment_incorrect_repeat(word)
        self.assertEqual(count, 1)
        count = self.service.increment_incorrect_repeat(word)
        self.assertEqual(count, 2)


if __name__ == "__main__":
    unittest.main()
