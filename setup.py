# setup.py

from setuptools import find_packages, setup

setup(
    name="VocabVoyage",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "python-multipart",
    ],
    entry_points={
        "console_scripts": [
            "vocabvoyage=app.main:app",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A language learning app for kids to learn vocabulary through quizzes.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/VocabVoyage",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Framework :: FastAPI",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
