import pytest
from playwright.sync_api import Playwright, expect


@pytest.mark.e2e
def test_page_launch(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:3000/")
    expect(page.get_by_text("Welcome to VocabVoyage")).not_to_be_empty()
    # Cleanup
    context.close()
    browser.close()


@pytest.mark.e2e
def test_page_launch_fi(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:3000/fi")
    expect(page.get_by_text("Tervetuloa VocabVoyage")).not_to_be_empty()
    # Cleanup
    context.close()
    browser.close()


@pytest.mark.e2e
def test_query_fi(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Navigate and start quiz
    page.goto("http://localhost:3000/fi")
    page.get_by_role("button", name="Aloita tietovisa").click()

    # Wait for translation to appear and input to be ready
    page.wait_for_selector("text=Käännä:")

    # Find input field - try multiple possible selectors
    answer_input = page.get_by_role("textbox").first

    # Input wrong answer
    answer_input.click()
    answer_input.fill("apple")
    page.get_by_role("button", name="Lähetä vastaus").click()

    # Verify result message appears
    expect(page.get_by_text("Läpäisit kokeen huippupistein")).not_to_be_empty()

    # Cleanup
    context.close()
    browser.close()


@pytest.mark.e2e
def test_query_wrong_fi(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Navigate and start quiz
    page.goto("http://localhost:3000/fi")
    page.get_by_role("button", name="Aloita tietovisa").click()

    # Wait for translation to appear and input to be ready
    page.wait_for_selector("text=Käännä:")

    # Find input field - try multiple possible selectors
    answer_input = page.get_by_role("textbox").first

    # Input wrong answer
    answer_input.click()
    answer_input.fill("orange")
    page.get_by_role("button", name="Lähetä vastaus").click()

    # Wait for error message and retry with correct answer
    answer_input = page.get_by_role("textbox").first

    # Input corrected answer
    answer_input.click()
    answer_input.fill("apple")
    page.get_by_role("button", name="Lähetä vastaus").click()

    # Input corrected answer
    answer_input = page.get_by_role("textbox").first
    answer_input.click()
    answer_input.fill("apple")
    page.get_by_role("button", name="Lähetä vastaus").click()

    # Verify result message appears
    expect(page.get_by_text("Jatka yrittämistä")).not_to_be_empty()

    # Cleanup
    context.close()
    browser.close()


@pytest.mark.e2e
def test_query_perfect_en(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Navigate and start quiz
    page.goto("http://localhost:3000/")
    page.get_by_role("button", name="Start Quiz").click()

    # Wait for translation to appear and input to be ready
    page.wait_for_selector("text=Translate:")

    # Find input field - try multiple possible selectors
    answer_input = page.get_by_role("textbox").first

    # Input wrong answer
    answer_input.click()
    answer_input.fill("Apple")
    page.get_by_role("button", name="Submit Answer").click()

    # Verify result message appears
    expect(page.get_by_text("You aced this exam")).not_to_be_empty()

    # Cleanup
    context.close()
    browser.close()


@pytest.mark.e2e
def test_query_wrong_answer_en(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Navigate and start quiz
    page.goto("http://localhost:3000/")
    page.get_by_role("button", name="Start Quiz").click()

    # Wait for translation to appear and input to be ready
    page.wait_for_selector("text=Translate:")

    # Find input field - try multiple possible selectors
    answer_input = page.get_by_role("textbox").first

    # Input wrong answer
    answer_input.click()
    answer_input.fill("orange")
    page.get_by_role("button", name="Submit Answer").click()

    # Wait for error message and retry with correct answer
    answer_input = page.get_by_role("textbox").first

    # Input corrected answer
    answer_input.click()
    answer_input.fill("apple")
    page.get_by_role("button", name="Submit Answer").click()

    # Input corrected answer
    answer_input = page.get_by_role("textbox").first
    answer_input.click()
    answer_input.fill("apple")
    page.get_by_role("button", name="Submit Answer").click()

    # Verify result message appears
    expect(page.get_by_text("Keep trying until")).not_to_be_empty()

    # Cleanup
    context.close()
    browser.close()
