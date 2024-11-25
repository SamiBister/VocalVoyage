# app/interfaces/repositories.py

import csv
import os
from typing import List

from app.domain.models import Word


class WordRepository:
    """
    Handles loading words from CSV files.
    """

    def __init__(self, data_folder: str = "app/data"):
        self.data_folder = data_folder

    def load_words(self) -> List[Word]:
        """
        Reads CSV files and returns a list of Word objects.
        """
        words = []
        for filename in os.listdir(self.data_folder):
            if filename.endswith(".csv"):
                filepath = os.path.join(self.data_folder, filename)
                with open(filepath, newline="", encoding="utf-8") as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        if len(row) >= 2:
                            word = Word(foreign_term=row[0], native_translation=row[1])
                            words.append(word)
        return words
