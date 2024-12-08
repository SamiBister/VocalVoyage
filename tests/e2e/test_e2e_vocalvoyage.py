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
def test_query_fi(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Navigate and start quiz
    page.goto("http://localhost:3000/fi")

    # Wait for page to load and verify Finnish text is visible
    expect(page.get_by_text("Tervetuloa VocabVoyage")).to_be_visible(timeout=10000)

    # Ensure language switch is complete
    page.wait_for_timeout(2000)  # Wait for translations to load

    # Click start quiz and wait for button to be ready
    start_button = page.get_by_role("button", name="Aloita tietovisa")
    expect(start_button).to_be_visible(timeout=10000)
    start_button.click()

    # Wait for quiz interface to load and try multiple possible text variations
    try:
        # Try different possible translations
        translations = ["Käännä:", "Käännä", "Translate:"]
        found = False
        for translation in translations:
            if page.get_by_text(translation).is_visible(timeout=2000):
                found = True
                break

        if not found:
            raise AssertionError("Translation text not found")

        # Find input field and verify it exists
        answer_input = page.get_by_role("textbox").first
        expect(answer_input).to_be_visible(timeout=10000)

        # Input answer
        answer_input.click()
        answer_input.fill("apple")

        # Find and click submit button
        submit_button = page.get_by_role("button", name="Lähetä vastaus")
        expect(submit_button).to_be_visible(timeout=10000)
        submit_button.click()

        # Verify result with longer timeout
        expect(page.get_by_text("Läpäisit kokeen huippupistein")).to_be_visible(
            timeout=15000
        )
    finally:
        # Cleanup
        context.close()
        browser.close()


@pytest.mark.e2e
def test_query_perfect_en(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
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
    browser = playwright.chromium.launch(headless=True)
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
