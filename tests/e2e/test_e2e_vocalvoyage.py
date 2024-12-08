import os
from datetime import datetime
from pathlib import Path

import pytest
from playwright.sync_api import Playwright, expect

ARTIFACTS_DIR = Path(os.environ.get("GITHUB_WORKSPACE", ".")) / "test-artifacts"
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)


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
    page.get_by_test_id("start-quiz-button").click()
    page.get_by_test_id("answer-input").fill("apple")
    page.get_by_test_id("answer-input").press("Enter")

    context.close()
    browser.close()


@pytest.mark.e2e
def test_degug_fi(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    try:
        # Navigate and start quiz
        page.goto("http://localhost:3000/fi")

        # Debug: Print button state
        start_button = page.get_by_test_id("start-quiz-button")
        print("=== Debug Info Before Click ===")
        print(f"Button text: {start_button.text_content()}")
        print(f"Button HTML: {start_button.evaluate('el => el.outerHTML')}")
        print(f"Button enabled: {start_button.is_enabled()}")
        print(f"Button visible: {start_button.is_visible()}")

        # Force wait for any animations
        page.wait_for_timeout(2000)

        # Ensure button is ready
        expect(start_button).to_be_visible()
        expect(start_button).to_be_enabled()

        # Force wait to ensure UI is stable
        page.wait_for_timeout(3000)

        # Click with retry logic
        try:
            start_button.click(timeout=5000)
        except Exception as e:
            # Take debug screenshot
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            page.screenshot(path=str(ARTIFACTS_DIR / f"error_en_{timestamp}.png"))
            page.screenshot(path="button-click-failed.png")
            print(f"Click failed: {str(e)}")
            print(f"Page content: {page.content()}")
            raise
            # Debug after click
        print("=== Debug Info After Click ===")
        print(f"Page URL: {page.url}")
        page.wait_for_timeout(1000)
        print(f"Page content after click: {page.content()}")
        # Verify click worked by checking for next element
        translate_message = page.get_by_test_id("translate-message")
        expect(translate_message).to_be_visible(timeout=10000)

    except Exception:
        # Take failure screenshot
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(
            path=str(ARTIFACTS_DIR / f"test-failure-error_en_{timestamp}.png")
        )
        raise
    finally:
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

    # translate_message = page.get_by_test_id("translate-message")
    # expect(translate_message).to_be_visible(timeout=10000)

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
