@critical
Feature: Login

    Scenario Outline: Validate the login form with valid and invalid data

        Given I login with <username> and <password> into Sales force
        Then I see the message <message>
        Examples:
            | username           |    password   | message |
            |ram1006@gmail.com   |techm@123   | (//span[text()='Home'])[1] |
            |ram1006@gmail.com   |techm@      | //div[text()="Please check your username and password. If you still can't log in, contact your Salesforce administrator."] |
