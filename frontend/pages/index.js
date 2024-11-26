// frontend/pages/index.js

import { useState, useEffect, useRef } from "react";
import useTranslation from "next-translate/useTranslation";
import setLanguage from "next-translate/setLanguage";
import axios from "axios";
import Head from "next/head";
import Image from "next/image";
import styles from "../styles/Home.module.css";

export default function Home() {
  const { t, lang } = useTranslation("common");
  const [currentWord, setCurrentWord] = useState(null);
  const [userInput, setUserInput] = useState("");
  const [stats, setStats] = useState({
    correct: 0,
    incorrect: 0,
    incorrect_words: [],
  });
  const [mode] = useState("infinite"); // Always use infinite mode
  const [writeCount, setWriteCount] = useState(0);
  const [language, setUILanguage] = useState(lang);
  const [message, setMessage] = useState("");
  const inputRef = useRef(null);

  const [selectedFiles, setSelectedFiles] = useState([]);
  const [uploadMessage, setUploadMessage] = useState("");

  useEffect(() => {
    if (inputRef.current) {
      inputRef.current.focus();
    }
  }, [currentWord, writeCount]);

  const startQuiz = async () => {
    await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/set_mode/`, {
      mode,
    });
    await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/start_quiz/`);
    fetchNextWord();
  };

  const endQuiz = async () => {
    await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/end_quiz/`);
    const response = await axios.get(
      `${process.env.NEXT_PUBLIC_API_URL}/results/`,
    );
    setStats(response.data);
    setCurrentWord(null);
  };

  const fetchNextWord = async () => {
    try {
      const response = await axios.get(
        `${process.env.NEXT_PUBLIC_API_URL}/words/next`,
      );
      if (response.data !== null) {
        setCurrentWord(response.data);
        setUserInput("");
        setWriteCount(0);
        setMessage("");
      } else {
        // No more words, end the quiz
        endQuiz();
      }
    } catch (error) {
      console.error("Error fetching next word:", error);
      setMessage("An error occurred while fetching the next word.");
    }
  };

  const submitAnswer = async () => {
    if (!currentWord) return;

    const response = await axios.post(
      `${process.env.NEXT_PUBLIC_API_URL}/check/`,
      {
        word: currentWord,
        user_input: userInput,
      },
    );

    const isCorrect = response.data.is_correct;

    if (isCorrect) {
      setUserInput("");
      setMessage(t("correct_answer"));
      fetchNextWord();
    } else {
      setWriteCount(1);
      setUserInput("");
      setMessage(
        t("incorrect_write_term_three_times", {
          term: currentWord.foreign_term,
        }),
      );
    }
  };

  const handleRepeatIncorrect = () => {
    if (
      userInput.trim().toLowerCase() ===
      currentWord.foreign_term.trim().toLowerCase()
    ) {
      const newWriteCount = writeCount + 1;
      setWriteCount(newWriteCount);
      setUserInput("");
      if (newWriteCount >= 3) {
        // Reset the write count and message, then proceed to the next word
        setWriteCount(0);
        setMessage("");
        fetchNextWord();
      } else {
        setMessage(t("keep_writing", { count: newWriteCount }));
      }
    } else {
      setUserInput("");
      setMessage(t("incorrect_spelling", { term: currentWord.foreign_term }));
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      if (writeCount > 0 && writeCount <= 3) {
        handleRepeatIncorrect();
      } else {
        submitAnswer();
      }
    }
  };

  const changeLanguage = async (e) => {
    const newLang = e.target.value;
    setUILanguage(newLang);
    await setLanguage(newLang);
  };

  const fileInputRef = useRef(null);

  const handleFileChange = (e) => {
    setSelectedFiles(e.target.files);
  };

  const uploadWordFiles = async () => {
    if (!selectedFiles || selectedFiles.length === 0) {
      setUploadMessage(t("no_files_selected"));
      return;
    }

    const formData = new FormData();
    for (let i = 0; i < selectedFiles.length; i++) {
      formData.append("files", selectedFiles[i]);
    }

    try {
      const response = await axios.post(
        `${process.env.NEXT_PUBLIC_API_URL}/upload_words/`,
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        },
      );
      setUploadMessage(response.data.message);
    } catch (error) {
      console.error("Error uploading files:", error);
      setUploadMessage(t("file_upload_error"));
    }
  };

  // Calculate the percentage of correct answers
  const totalAnswers = stats.correct + stats.incorrect;
  const correctPercentage =
    totalAnswers > 0 ? (stats.correct / totalAnswers) * 100 : 0;

  // Determine the result image and message based on the percentage
  let resultImage = "";
  let resultMessage = "";

  if (totalAnswers > 0 && !currentWord) {
    if (correctPercentage === 100) {
      resultImage = "/perfect.webp";
      resultMessage = t("result_perfect");
    } else if (correctPercentage >= 80) {
      resultImage = "/very_high.webp";
      resultMessage = t("result_very_high");
    } else if (correctPercentage >= 60) {
      resultImage = "/high.webp";
      resultMessage = t("result_high");
    } else if (correctPercentage >= 40) {
      resultImage = "/medium.webp";
      resultMessage = t("result_medium");
    } else if (correctPercentage >= 20) {
      resultImage = "/low.webp";
      resultMessage = t("result_low");
    } else {
      resultImage = "/very_low.webp";
      resultMessage = t("result_very_low");
    }
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>VocabVoyage</title>
        <link rel="icon" href="/favicon.ico" />
        {/* Existing links and meta tags */}
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link
          rel="preconnect"
          href="https://fonts.gstatic.com"
          crossOrigin="true"
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Comic+Neue:wght@400;700&display=swap"
          rel="stylesheet"
        />
      </Head>

      <div className={styles.header}>
        <Image
          src="/logo.webp" // The path to your image in the public folder
          alt="Logo"
          width={100} // Adjust the width and height as needed
          height={100}
          className={styles.logo}
        />
        <h1 className={styles.heading}>{t("welcome")}</h1>
      </div>

      {/* Language Selection Dropdown */}
      <label className={styles.label}>
        {t("select_language")}:
        <select
          className={styles.select}
          value={language}
          onChange={changeLanguage}
        >
          <option value="en">English</option>
          <option value="fi">Suomi</option>
          {/* Add more languages as needed */}
        </select>
      </label>

      {/* File Upload Section */}
      <div className={styles.uploadSection}>
        <h2 className={styles.subheading}>{t("upload_word_files")}</h2>
        <div className={styles.fileUpload}>
          <label htmlFor="file-upload" className={styles.fileUploadLabel}>
            {t("choose_files")}
          </label>
          <input
            id="file-upload"
            type="file"
            accept=".csv"
            multiple
            onChange={handleFileChange}
            className={styles.fileInput}
            ref={fileInputRef}
          />
          <span className={styles.fileName}>
            {selectedFiles.length > 0
              ? Array.from(selectedFiles)
                  .map((file) => file.name)
                  .join(", ")
              : t("no_file_chosen")}
          </span>
        </div>
        <button className={styles.button} onClick={uploadWordFiles}>
          {t("upload_files")}
        </button>
        {uploadMessage && <p className={styles.message}>{uploadMessage}</p>}
      </div>

      {!currentWord && totalAnswers === 0 ? (
        <div>
          <button className={styles.button} onClick={startQuiz}>
            {t("start_quiz")}
          </button>
        </div>
      ) : currentWord ? (
        <div>
          {message && <p className={styles.message}>{message}</p>}
          {writeCount > 0 && writeCount <= 3 ? (
            <div>
              <p>
                {t("please_write_term_three_times", {
                  term: currentWord.foreign_term,
                  count: writeCount,
                })}
              </p>
              <input
                type="text"
                className={styles.textInput}
                value={userInput}
                onChange={(e) => setUserInput(e.target.value)}
                onKeyDown={handleKeyDown}
                placeholder={currentWord.foreign_term}
                ref={inputRef}
              />
              <button className={styles.button} onClick={handleRepeatIncorrect}>
                {t("submit_answer")}
              </button>
            </div>
          ) : (
            <div>
              <p>{`${t("translate")}: ${currentWord.native_translation}`}</p>
              <input
                type="text"
                className={styles.textInput}
                value={userInput}
                onChange={(e) => setUserInput(e.target.value)}
                onKeyDown={handleKeyDown}
                ref={inputRef}
              />
              <button className={styles.button} onClick={submitAnswer}>
                {t("submit_answer")}
              </button>
              <button className={styles.button} onClick={endQuiz}>
                {t("end_quiz")}
              </button>
            </div>
          )}
        </div>
      ) : totalAnswers > 0 && !currentWord ? (
        <div className={styles.resultSection}>
          <h2>{t("quiz_statistics")}</h2>
          <p>{`${t("correct")}: ${stats.correct}`}</p>
          <p>{`${t("incorrect")}: ${stats.incorrect}`}</p>
          <p>{`${t("score")}: ${correctPercentage.toFixed(2)}%`}</p>
          {resultImage && (
            <Image
              src={resultImage}
              alt="Result Image"
              width={200}
              height={200}
              className={styles.resultImage}
            />
          )}
          {resultMessage && (
            <p className={styles.resultMessage}>{resultMessage}</p>
          )}
          {stats.incorrect_words.length > 0 && (
            <>
              <h3>{t("incorrect_words")}</h3>
              <ul>
                {stats.incorrect_words.map((word, index) => (
                  <li key={index}>{word}</li>
                ))}
              </ul>
            </>
          )}
          <button className={styles.button} onClick={startQuiz}>
            {t("start_new_quiz")}
          </button>
        </div>
      ) : null}
    </div>
  );
}
