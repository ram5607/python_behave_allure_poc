@critical
Feature: Sales force dashboard

    Scenario Outline: Validate the dashboard section header

        Given I login into Sales force
        Then I see Home page
        Then Dashboard shows correct headers for row "<tittle>"
        Examples:
             | tittle          |
             | Administration   |