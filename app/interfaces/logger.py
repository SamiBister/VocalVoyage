"""
app/interfaces/logger.py
This module provides the `QuizLogger` class, which is responsible for logging quiz results into Markdown files.

Classes:
    - QuizLogger: Logs quiz results into Markdown files in the specified output folder.

Dependencies:
    - os: Used for creating directories and handling file paths.
    - app.domain.models.QuizResult: The model representing the quiz result to be logged.
"""

import os

from app.domain.models import QuizResult


class QuizLogger:
    """
    A class to log quiz results into Markdown files in the specified output folder.

    Attributes:
    ----------
    output_folder : str
        The directory where the quiz result files will be saved.

    Methods:
    -------
    __init__(output_folder: str = "app/out"):
        Initializes the QuizLogger with the specified output folder, creating the folder if it doesn't exist.

    log_result(result: QuizResult) -> None:
        Logs the quiz result into a Markdown file with details such as start time, end time, correct and incorrect answers.
    """

    def __init__(self, output_folder: str = "app/out"):
        """
        Initializes the Logger instance.
        Args:
            output_folder (str): The folder where log files will be stored. Defaults to "app/out".
        Creates the output folder if it does not already exist.
        """

        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)

    def log_result(self, result: QuizResult) -> None:
        """
        Logs the quiz result into a Markdown file.
        This method creates a Markdown file named with the timestamp of the quiz start time.
        The file contains details about the quiz, including start and end times, the number of
        correct and incorrect answers, and lists of correctly and incorrectly answered terms.

        Args:
            result (QuizResult): An object containing the quiz result details, including:
            - start_time (datetime): The start time of the quiz.
            - end_time (datetime): The end time of the quiz.
            - correct (int): The number of correct answers.
            - incorrect (int): The number of incorrect answers.
            - correct_words (List[str]): A list of correctly answered terms.
            - incorrect_words (List[str]): A list of incorrectly answered terms.

        Returns:
            None

        """
        timestamp = result.start_time.strftime("%Y%m%d_%H%M%S")
        filename = f"quiz_{timestamp}.md"
        filepath = os.path.join(self.output_folder, filename)

        content = (
            f"# Quiz Result - {result.start_time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            f"**Start Time:** {result.start_time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            f"**End Time:** {result.end_time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            f"**Correct Answers:** {result.correct}\n\n"
            f"**Incorrect Answers:** {result.incorrect}\n\n"
            f"## Correctly Answered Terms:\n\n"
        )

        if result.correct_words:
            for word in result.correct_words:
                content += f"- {word}\n"
        else:
            content += "None\n"

        content += "\n## Incorrectly Answered Terms:\n\n"

        if result.incorrect_words:
            for word in result.incorrect_words:
                content += f"- {word}\n"
        else:
            content += "None\n"

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)
