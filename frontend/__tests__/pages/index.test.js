// frontend/pages/index.test.js
import React from "react";
import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import axios from "axios";
import Home from "./index";

// Mock axios
jest.mock("axios");

// Mock the translations
jest.mock("next-translate/useTranslation", () => () => ({
  t: (key) =>
    ({
      welcome: "Welcome to VocabVoyage",
      choose_files: "Choose files",
      start_quiz: "Start Quiz",
      end_quiz: "End Quiz",
      quiz_statistics: "Quiz Statistics",
      translate: "Translate",
      submit_answer: "Submit Answer",
    })[key] || key,
  lang: "en",
}));

describe("Home", () => {
  beforeEach(() => {
    // Mock Axios GET requests
    axios.get.mockImplementation((url) => {
      if (url.includes("/words/next")) {
        return Promise.resolve({
          data: {
            foreign_term: "test",
            native_translation: "testi",
          },
        });
      }
      if (url.includes("/results")) {
        return Promise.resolve({
          data: {
            correct: 1,
            incorrect: 1,
            incorrect_words: ["word1"],
          },
        });
      }
      return Promise.resolve({ data: {} });
    });

    // Mock Axios POST requests
    axios.post.mockResolvedValue({ data: {} });
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  it("shows quiz statistics after ending quiz", async () => {
    render(<Home />);

    // Start the quiz
    const startButton = screen.getByText("Start Quiz");
    fireEvent.click(startButton);

    // Wait for the "End Quiz" button to appear
    const endButton = await screen.findByText("End Quiz");
    expect(endButton).toBeInTheDocument();

    // End the quiz
    fireEvent.click(endButton);

    // Verify that the quiz statistics are displayed
    const statsHeading = await screen.findByText("Quiz Statistics");
    expect(statsHeading).toBeInTheDocument();
  });
});
