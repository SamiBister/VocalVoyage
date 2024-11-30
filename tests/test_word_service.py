"""
Unit tests for the WordService class.

app/tests/test_word_service.py

Classes:
    TestWordService: Contains unit tests for the WordService class.

TestWordService Methods:
    setUp: Initializes the test case with sample data and mocks.
    test_get_next_word_normal: Tests the get_next_word method in normal mode.
    test_get_next_word_infinite: Tests the get_next_word method in infinite mode.
    test_check_answer_correct: Tests the check_answer method with a correct answer.
    test_check_answer_incorrect: Tests the check_answer method with an incorrect answer.
    test_increment_incorrect_repeat: Tests the increment_incorrect_repeat method.
"""

import unittest
from unittest.mock import MagicMock

from app.domain.models import Word
from app.interfaces.logger import QuizLogger
from app.use_cases.word_service import WordService


class TestWordService(unittest.TestCase):
    """
    Unit tests for the WordService class.
    Test Cases:
    - test_get_next_word_normal: Tests the normal mode where each word is asked once and all answers are correct.
    - test_get_next_word_infinite: Tests the infinite mode where words are asked repeatedly and all answers are incorrect.
    - test_check_answer_correct: Tests the check_answer method with a correct answer.
    - test_check_answer_incorrect: Tests the check_answer method with an incorrect answer.
    - test_increment_incorrect_repeat: Tests the increment_incorrect_repeat method to ensure it correctly counts repeated incorrect answers.
    Attributes:
    - words: A list of Word objects used for testing.
    - mock_logger: A mock object for the QuizLogger.
    - service: An instance of WordService initialized with the test words and mock logger.
    """

    def setUp(self):
        """
        Set up the test environment for WordService tests.
        This method initializes a list of Word objects and a mock QuizLogger.
        It then creates an instance of WordService with the initialized words and mock logger.
        """

        self.words = [
            Word(foreign_term="Hello", native_translation="Hei"),
            Word(foreign_term="World", native_translation="Maailma"),
        ]
        self.mock_logger = MagicMock(spec=QuizLogger)
        self.service = WordService(self.words, self.mock_logger)

    def test_get_next_word_normal(self):
        """
        Test the `get_next_word` method in "normal" mode.
        This test sets the service mode to "normal" and continuously retrieves the next word
        until no more words are available. It simulates correct answers for each word retrieved
        and checks the following:
        - The number of words asked matches the total number of words available.
        - The number of correct answers recorded by the service matches the total number of words.
        - The number of incorrect answers recorded by the service is zero.
        """

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
        """
        Tests the `get_next_word` method in "infinite" mode.
        This test simulates the scenario where the user answers incorrectly three times.
        It verifies that:
        - The service continues to provide words even after incorrect answers.
        - The number of words asked is at least as many as the total words available.
        - The count of correct answers remains zero.
        - The count of incorrect answers matches the number of words asked.
        Steps:
        1. Set the service mode to "infinite".
        2. Simulate answering incorrectly three times by calling `get_next_word` and `check_answer` with "Wrong".
        3. Verify that the number of words asked is at least the number of available words.
        4. Verify that the count of correct answers is zero.
        5. Verify that the count of incorrect answers matches the number of words asked.
        """

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
        """
        Test case for checking if the answer is correct.
        This test verifies that the `check_answer` method correctly identifies
        a correct answer and updates the `correct` and `incorrect` counters
        accordingly.
        Steps:
        1. Retrieve the first word from the `words` list.
        2. Call the `check_answer` method with the word and the answer "Hello".
        3. Assert that the result is True.
        4. Assert that the `correct` counter is incremented to 1.
        5. Assert that the `incorrect` counter remains 0.
        """

        word = self.words[0]
        result = self.service.check_answer(word, "Hello")
        self.assertTrue(result)
        self.assertEqual(self.service.correct, 1)
        self.assertEqual(self.service.incorrect, 0)

    def test_check_answer_incorrect(self):
        """
        Test the check_answer method for an incorrect answer.
        This test verifies that when an incorrect answer is provided to the 
        check_answer method, the method returns False, increments the incorrect 
        counter, and adds the word to the incorrect_words list.
        Assertions:
            - The result of check_answer should be False.
            - The correct counter should remain 0.
            - The incorrect counter should be incremented to 1.
            - The word should be added to the incorrect_words list.
        """

        word = self.words[0]
        result = self.service.check_answer(word, "Hi")
        self.assertFalse(result)
        self.assertEqual(self.service.correct, 0)
        self.assertEqual(self.service.incorrect, 1)
        self.assertIn("Hello", self.service.incorrect_words)

    def test_increment_incorrect_repeat(self):
        """
        Test the increment_incorrect_repeat method of the word service.
        This test verifies that the incorrect repeat count for a word is correctly
        incremented when the increment_incorrect_repeat method is called.
        Steps:
        1. Retrieve the first word from the words list.
        2. Call the check_answer method with an incorrect answer to ensure the word
           is marked as incorrect.
        3. Call the increment_incorrect_repeat method and verify that the count is 1.
        4. Call the increment_incorrect_repeat method again and verify that the count is 2.
        """

        word = self.words[0]
        self.service.check_answer(word, "Hi")  # Incorrect
        count = self.service.increment_incorrect_repeat(word)
        self.assertEqual(count, 1)
        count = self.service.increment_incorrect_repeat(word)
        self.assertEqual(count, 2)


if __name__ == "__main__":
    unittest.main()
