Feature: Login Page Testing

Scenario: Successful Login
    Given The User is on the login Page
    When the user enters valid credentials
    And Clicks the login button
    Then They should be logged in successfully

Scenario: Invalid Login
    Given the user is on the login page
    When the user enters invalid credentials
    And clicks the login button
    Then they should see an error message

Scenario: Screenshot Working
    Given The user is on the login page
    When the user enters valid or invalid credentials
    Then Take a screenshot of the screen
