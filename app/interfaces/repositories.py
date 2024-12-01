"""
Handle loading words from CSV files.

app/interfaces/repositories.py

Attributes:
    data_folder (str): The folder where CSV files are stored. Defaults to "app/data".

Methods:
    load_words() -> List[Word]:
        Reads CSV files from the data folder and returns a list of Word objects.

Dependencies:
    - csv: Used for reading CSV files.
    - os: Used for file and directory operations.
    - typing.List: Used for type hinting the return type of load_words method.
    - app.domain.models.Word: The Word class used to create word objects from CSV data.
"""

import csv
import os
from typing import List

from app.domain.models import Word


class WordRepository:
    """
    Handles loading words from CSV files.

    Attributes:
        data_folder (str): The folder where CSV files containing words are stored.

    Methods:
        load_words() -> List[Word]:
            Reads CSV files from the data folder and returns a list of Word objects.

        Initializes the WordRepository with the specified data folder.

        Args:
            data_folder (str): The folder where CSV files containing words are stored. Defaults to "app/data".

        Reads CSV files from the data folder and returns a list of Word objects.

        Returns:
            List[Word]: A list of Word objects created from the CSV files.

    """

    def __init__(self, data_folder: str = "app/data"):
        self.data_folder = data_folder

    def load_words(self) -> List[Word]:
        """
        Reads CSV files from the specified data folder and returns a list of Word objects.

        Each CSV file should contain rows with at least two columns: the first column for the foreign term
        and the second column for the native translation. The method iterates through all CSV files in the
        data folder, reads their contents, and creates Word objects for each valid row.

        Returns:
            List[Word]: A list of Word objects created from the CSV file contents.
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
