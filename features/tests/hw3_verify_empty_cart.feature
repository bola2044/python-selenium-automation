Feature: Amazon Empty Cart tests

 Scenario: User can see empty cart
   Given Open amazon main page
   When Click on cart button
   Then Verify user see empty cart message
