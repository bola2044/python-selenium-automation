# Created by priscillao at 6/7/23
Feature: Tests for amazon bestseller page

  Scenario: User can open amazon bestseller page
    Given Open amazon main page
    When Search for bestseller
    Then Verify there are 5 links