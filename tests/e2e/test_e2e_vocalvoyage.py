import pytest
from playwright.sync_api import Playwright, expect


@pytest.mark.e2e
def test_page_launch(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:3000/")
    expect(page.get_by_text("Welcome to VocabVoyage")).not_to_be_empty()
    # Cleanup
    context.close()
    browser.close()


@pytest.mark.e2e
def test_page_launch_fi(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:3000/fi")
    expect(page.get_by_text("Tervetuloa VocabVoyage")).not_to_be_empty()
    # Cleanup
    context.close()
    browser.close()


@pytest.mark.e2e
def test_query_fi(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Navigate and start quiz
    page.goto("http://localhost:3000/fi")

    # Wait for page to load and verify Finnish text is visible
    welcome_message = page.get_by_test_id("welcome-message")
    expect(welcome_message).to_be_visible(timeout=10000)

    # Click start quiz and wait for button to be ready
    start_button = page.get_by_test_id("start-quiz-button")
    expect(start_button).to_be_visible(timeout=10000)
    start_button.click()

    translate_message = page.get_by_test_id("translate-message")
    expect(translate_message).to_be_visible(timeout=10000)

    answer_input = page.get_by_test_id("answer-input")
    expect(answer_input).to_be_visible(timeout=10000)

    answer_input.click()
    answer_input.fill("apple")

    submit_button = page.get_by_test_id("submit")
    expect(submit_button).to_be_visible(timeout=10000)
    submit_button.click()

    result_message = page.get_by_test_id("correct-message")
    expect(result_message).to_be_visible(timeout=10000)

    context.close()
    browser.close()


@pytest.mark.e2e
def test_query_wrong_fi(playwright: Playwright) -> None:
    # Navigate and start quiz
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Navigate and start quiz
    page.goto("http://localhost:3000")

    # Wait for page to load and verify Finnish text is visible
    welcome_message = page.get_by_test_id("welcome-message")
    expect(welcome_message).to_be_visible(timeout=10000)

    # Click start quiz and wait for button to be ready
    start_button = page.get_by_test_id("start-quiz-button")
    expect(start_button).to_be_visible(timeout=10000)
    start_button.click()

    translate_message = page.get_by_test_id("translate-message")
    expect(translate_message).to_be_visible(timeout=10000)

    answer_input = page.get_by_test_id("answer-input")
    expect(answer_input).to_be_visible(timeout=10000)

    answer_input.click()
    answer_input.fill("orange")

    submit_button = page.get_by_test_id("submit")
    expect(submit_button).to_be_visible(timeout=10000)
    submit_button.click()

    answer_input = page.get_by_test_id("answer-input")
    expect(answer_input).to_be_visible(timeout=10000)

    answer_input.click()
    answer_input.fill("apple")

    submit_button = page.get_by_test_id("submit")
    expect(submit_button).to_be_visible(timeout=10000)
    submit_button.click()

    answer_input = page.get_by_test_id("answer-input")
    expect(answer_input).to_be_visible(timeout=10000)

    answer_input.click()
    answer_input.fill("apple")

    submit_button = page.get_by_test_id("submit")
    expect(submit_button).to_be_visible(timeout=10000)
    submit_button.click()

    result_message = page.get_by_test_id("correct-message")
    expect(result_message).to_be_visible(timeout=10000)

    context.close()
    browser.close()


@pytest.mark.e2e
def test_query_perfect_en(playwright: Playwright) -> None:
    # Navigate and start quiz
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Navigate and start quiz
    page.goto("http://localhost:3000")

    # Wait for page to load and verify Finnish text is visible
    welcome_message = page.get_by_test_id("welcome-message")
    expect(welcome_message).to_be_visible(timeout=10000)

    # Click start quiz and wait for button to be ready
    start_button = page.get_by_test_id("start-quiz-button")
    expect(start_button).to_be_visible(timeout=10000)
    start_button.click()

    translate_message = page.get_by_test_id("translate-message")
    expect(translate_message).to_be_visible(timeout=10000)

    answer_input = page.get_by_test_id("answer-input")
    expect(answer_input).to_be_visible(timeout=10000)

    answer_input.click()
    answer_input.fill("apple")

    submit_button = page.get_by_test_id("submit")
    expect(submit_button).to_be_visible(timeout=10000)
    submit_button.click()

    result_message = page.get_by_test_id("correct-message")
    expect(result_message).to_be_visible(timeout=10000)

    context.close()
    browser.close()


@pytest.mark.e2e
def test_query_wrong_answer_en(playwright: Playwright) -> None:
    # Navigate and start quiz
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Navigate and start quiz
    page.goto("http://localhost:3000")

    # Wait for page to load and verify Finnish text is visible
    welcome_message = page.get_by_test_id("welcome-message")
    expect(welcome_message).to_be_visible(timeout=10000)

    # Click start quiz and wait for button to be ready
    start_button = page.get_by_test_id("start-quiz-button")
    expect(start_button).to_be_visible(timeout=10000)
    start_button.click()

    translate_message = page.get_by_test_id("translate-message")
    expect(translate_message).to_be_visible(timeout=10000)

    answer_input = page.get_by_test_id("answer-input")
    expect(answer_input).to_be_visible(timeout=10000)

    answer_input.click()
    answer_input.fill("orange")

    submit_button = page.get_by_test_id("submit")
    expect(submit_button).to_be_visible(timeout=10000)
    submit_button.click()

    answer_input = page.get_by_test_id("answer-input")
    expect(answer_input).to_be_visible(timeout=10000)

    answer_input.click()
    answer_input.fill("apple")

    submit_button = page.get_by_test_id("submit")
    expect(submit_button).to_be_visible(timeout=10000)
    submit_button.click()

    answer_input = page.get_by_test_id("answer-input")
    expect(answer_input).to_be_visible(timeout=10000)

    answer_input.click()
    answer_input.fill("apple")

    submit_button = page.get_by_test_id("submit")
    expect(submit_button).to_be_visible(timeout=10000)
    submit_button.click()

    result_message = page.get_by_test_id("correct-message")
    expect(result_message).to_be_visible(timeout=10000)

    context.close()
    browser.close()
