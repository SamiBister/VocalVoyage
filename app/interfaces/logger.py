# app/interfaces/logger.py

import os

from app.domain.models import QuizResult


class QuizLogger:
    """
    Logs quiz results into Markdown files in the out folder.
    """

    def __init__(self, output_folder: str = "app/out"):
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)

    def log_result(self, result: QuizResult) -> None:
        """
        Logs the quiz result into a Markdown file.
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
