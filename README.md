Gherkin and Playwright Test Code

Overview
This repository contains automated tests for the login functionality of a web application using Gherkin syntax for behavior-driven development (BDD) and Playwright for browser automation. The tests are written in Python and use the pytest-bdd framework.

Test Scenarios
Scenario 1: Successful Login
Given The user is on the login page
When The user enters valid credentials
And Clicks the login button
Then They should be logged in successfully

Scenario 2: Invalid Login
Given The user is on the login page
When The user enters invalid credentials
And Clicks the login button
Then They should see an error message

Scenario 3: Screenshot Working
Given The user is on the login page
When The user enters valid or invalid credentials
Then Take a screenshot of the screen
Test Code Explanation
The test code is organized into steps using Gherkin syntax, making it easy to understand the behavior of each scenario. The Playwright library is used for browser automation, and pytest-bdd is employed for BDD-style test execution.

Code Structure
test_login.py: Contains the test scenarios and step definitions.
requirements.txt: Lists the required dependencies for the project.
Test Fixtures
browser: Launches and closes the browser instance.
page: Creates and closes a new page within the browser.

Test Steps
Given The user is on the login page

Navigates to the specified URL.
When The user enters valid credentials

Fills in the username and password fields with valid data.
When The user enters invalid credentials

Fills in the username and password fields with invalid data.
When The user clicks the login button

Simulates a button click action.
Then They should be logged in successfully

Verifies the title of the page after successful login.
Then They should see an error message

Verifies the title of the page after unsuccessful login.
Then A screenshot should be taken

Captures a screenshot of the current page.
