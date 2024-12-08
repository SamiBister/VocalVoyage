import os
from pathlib import Path

import pytest
from playwright.async_api import async_playwright, expect

# from playwright.sync_api import Playwright, expect


ARTIFACTS_DIR = Path(os.environ.get("GITHUB_WORKSPACE", ".")) / "test-artifacts"
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_page_launch() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate and start quiz
        await page.goto("http://localhost:3000")
        await page.wait_for_load_state("networkidle")
        # Locate the welcome-message element
        welcome_message = page.get_by_test_id("welcome-message")
        # Expect it to be visible within 10 seconds
        await expect(welcome_message).to_be_visible(timeout=10000)


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_page_launch_fi() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate and start quiz
        await page.goto("http://localhost:3000/fi")
        await page.wait_for_load_state("networkidle")
        # Locate the welcome-message element
        welcome_message = page.get_by_test_id("welcome-message")
        # Expect it to be visible within 10 seconds
        await expect(welcome_message).to_be_visible(timeout=10000)


# @pytest.mark.e2e
# def test_page_launch(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=True)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("http://localhost:3000/")
#     expect(page.get_by_text("Welcome to VocabVoyage")).not_to_be_empty()
#     # Cleanup
#     context.close()
#     browser.close()


# @pytest.mark.e2e
# def test_page_launch_fi(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=True)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("http://localhost:3000/fi")
#     expect(page.get_by_text("Tervetuloa VocabVoyage")).not_to_be_empty()
#     # Cleanup
#     context.close()
#     browser.close()


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_query_fi() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        # # Register event listeners before navigation
        # async def log_response(response):
        #     print(
        #         f"RESPONSE: URL={response.url}, Status={response.status}, "
        #         f"Headers={await response.all_headers()}"
        #     )

        # async def log_request_failed(request):
        #     print(
        #         f"REQUEST FAILED: URL={request.url}, "
        #         f"Failure={request.failure}, Method={request.method}"
        #     )

        # Navigate and start quiz
        await page.goto("http://localhost:3000/fi")
        await page.wait_for_load_state("networkidle")

        # Click start quiz and wait for button to be ready
        # await page.get_by_test_id("start-quiz-button").click()
        await page.get_by_test_id("start-quiz-button").scroll_into_view_if_needed()
        await page.get_by_test_id("start-quiz-button").click(force=True)
        await page.wait_for_timeout(10000)
        await page.wait_for_selector(
            "[data-testid='answer1']", state="visible", timeout=20000
        )
        await page.get_by_test_id("answer1").fill("apple")
        await page.get_by_test_id("answer1").press("Enter")
        # Locate the translate-message element
        correct_message = page.get_by_test_id("correct-message")

        # Expect it to be visible within 10 seconds
        await expect(correct_message).to_be_visible(timeout=10000)

        await context.close()
        await browser.close()


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_query_en() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate and start quiz
        await page.goto("http://localhost:3000")
        await page.wait_for_load_state("networkidle")

        # Click start quiz and wait for button to be ready
        # await page.get_by_test_id("start-quiz-button").click()
        await page.get_by_test_id("start-quiz-button").scroll_into_view_if_needed()
        await page.get_by_test_id("start-quiz-button").click(force=True)
        await page.wait_for_timeout(10000)
        await page.wait_for_selector(
            "[data-testid='answer1']", state="visible", timeout=20000
        )
        await page.get_by_test_id("answer1").fill("apple")
        await page.get_by_test_id("answer1").press("Enter")
        # Locate the translate-message element
        correct_message = page.get_by_test_id("correct-message")

        # Expect it to be visible within 10 seconds
        await expect(correct_message).to_be_visible(timeout=10000)

        await context.close()
        await browser.close()


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_query_fail_en() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate and start quiz
        await page.goto("http://localhost:3000")
        await page.wait_for_load_state("networkidle")

        # Click start quiz and wait for button to be ready
        # await page.get_by_test_id("start-quiz-button").click()
        await page.get_by_test_id("start-quiz-button").scroll_into_view_if_needed()
        await page.get_by_test_id("start-quiz-button").click(force=True)
        await page.wait_for_timeout(10000)
        await page.wait_for_selector(
            "[data-testid='answer1']", state="visible", timeout=20000
        )
        await page.get_by_test_id("answer1").fill("orange")
        await page.get_by_test_id("answer1").press("Enter")

        await page.wait_for_selector(
            "[data-testid='answer2']", state="visible", timeout=20000
        )
        await page.get_by_test_id("answer2").fill("apple")
        await page.get_by_test_id("answer2").press("Enter")

        await page.wait_for_selector(
            "[data-testid='answer2']", state="visible", timeout=20000
        )
        await page.get_by_test_id("answer2").fill("apple")
        await page.get_by_test_id("answer2").press("Enter")
        # Locate the translate-message element
        correct_message = page.get_by_test_id("correct-message")

        # Expect it to be visible within 10 seconds
        await expect(correct_message).to_be_visible(timeout=10000)

        await context.close()
        await browser.close()


@pytest.mark.asyncio
@pytest.mark.e2e
async def test_query_fail_fi() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate and start quiz
        await page.goto("http://localhost:3000/fi")
        await page.wait_for_load_state("networkidle")

        # Click start quiz and wait for button to be ready
        # await page.get_by_test_id("start-quiz-button").click()
        await page.get_by_test_id("start-quiz-button").scroll_into_view_if_needed()
        await page.get_by_test_id("start-quiz-button").click(force=True)
        await page.wait_for_timeout(10000)
        await page.wait_for_selector(
            "[data-testid='answer1']", state="visible", timeout=20000
        )
        await page.get_by_test_id("answer1").fill("orange")
        await page.get_by_test_id("answer1").press("Enter")

        await page.wait_for_selector(
            "[data-testid='answer2']", state="visible", timeout=20000
        )
        await page.get_by_test_id("answer2").fill("apple")
        await page.get_by_test_id("answer2").press("Enter")

        await page.wait_for_selector(
            "[data-testid='answer2']", state="visible", timeout=20000
        )
        await page.get_by_test_id("answer2").fill("apple")
        await page.get_by_test_id("answer2").press("Enter")
        # Locate the translate-message element
        correct_message = page.get_by_test_id("correct-message")

        # Expect it to be visible within 10 seconds
        await expect(correct_message).to_be_visible(timeout=10000)

        await context.close()
        await browser.close()
