
import pytest
from playwright.sync_api import Playwright, expect


@pytest.mark.e2e
def test_page_launch(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:3000/")
    expect(page.get_by_text("Welcome to VocabVoyage")).not_to_be_empty()


@pytest.mark.e2e
def test_query_fi(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:3000/fi")
    page.get_by_role("button", name="Aloita tietovisa").click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill("apple")
    page.get_by_role("button", name="Lähetä vastaus").click()
    page.get_by_text("Oikein:").click()
    page.get_by_text("Väärin:").click()
    page.get_by_text("Pisteet: 100.00%").click()
    page.get_by_text("Läpäisit kokeen huippupistein").click()
    expect(page.get_by_text("Läpäisit kokeen huippupistein")).not_to_be_empty()


@pytest.mark.e2e
def test_query_wrong_fi(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:3000/fi")
    page.get_by_role("button", name="Aloita tietovisa").click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill("orange")
    page.get_by_role("textbox").press("Enter")
    page.get_by_role("textbox").fill("apple")
    page.get_by_role("textbox").press("Enter")
    page.get_by_placeholder("Apple").fill("apple")
    page.get_by_placeholder("Apple").press("Enter")
    expect(page.get_by_text("Jatka yrittämistä, kunnes")).not_to_be_empty()
    expect(page.get_by_text("Apple")).not_to_be_empty()


@pytest.mark.e2e
def test_query_perfect_en(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:3000/")
    page.get_by_role("button", name="Start Quiz").click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill("apple")
    page.get_by_role("textbox").press("Enter")
    expect(page.get_by_text("You aced this exam! You can")).not_to_be_empty()


@pytest.mark.e2e
def test_query_wrong_answer_en(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:3000/")
    page.get_by_role("button", name="Start Quiz").click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill("orange")
    page.get_by_role("textbox").press("Enter")
    page.get_by_role("textbox").fill("apple")
    page.get_by_role("textbox").press("Enter")
    page.get_by_placeholder("Apple").fill("apple")
    page.get_by_placeholder("Apple").press("Enter")
    page.get_by_text("Keep trying until you get the").click()
    expect(page.get_by_text("Keep trying until you get the")).not_to_be_empty()
    expect(page.get_by_text("Apple")).not_to_be_empty()
