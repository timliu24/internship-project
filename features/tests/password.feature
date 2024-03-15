# Created by liudi at 3/12/2024
Feature: Change Password
  User sign in to site and can open change password page

  Scenario: User can open change password page
    Given Open the main page
    When Log in to the page
    And Click on settings option
    And Click on Change password option
    And Verify the right page opens
    And Add some test password to the input fields
    Then Verify the “Change password” button is available