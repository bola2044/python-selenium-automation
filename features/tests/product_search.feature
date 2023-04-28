Feature: Test Scenarios for Search functionality

  Scenario: Usergit status can search for a product
    Given Open Google page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown