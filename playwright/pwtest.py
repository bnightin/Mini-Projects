from pytest_bdd import scenario, given, when, then
import pytest
from playwright.sync_api import Page, Browser, Playwright

def browser(playwright: Playwright):
    browser = playwright.chromium.launch()
    yield browser
    browser.close()

def page(browser: Browser):
    page = browser.new_page()
    yield page
    page.close()

@given("The user is on the login Page")
def login_page(page: Page):
    page.goto("https://demo.opencart.com/admin/")

@when("The user enters valid credentials")
def valid_credentials(page: Page):
    page.fill('input#input-username','demo')
    page.fill('input#input-password','demo')

@when("The user enters invalid credentials")
def invalid_credentials(page: Page):
    page.fill('input#input-username','invaliddemo')
    page.fill('input#input-password','invaliddemo')

@when("Then user clicks the login button")
def clicks_login(page: Page):
    page.click('button[type=submit]')

@then("They should be logged in successfully")
def valid_login(playwright):
    title = page.title()
    assert title == 'Dashboard'

@then("They should see an error message")
def invalid_login():
    title = page.title()
    assert title == 'Administration'

@then("A screenshot should be taken")
def take_screenshot(page: Page):
    page.screenshot(path='screenshot.png')
    
