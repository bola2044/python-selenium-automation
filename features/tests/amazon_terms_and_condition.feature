Feature: Amazon terms and Condition page

 Scenario: User can open and close Amazon Privacy Notice
 Given Open amazon main page
  When Click Orders
   Then Verify Sign In page opens
  And Click condition of use
  When Store original windows
  And Click on Amazon Privacy Notice link
  Then Verify Amazon Privacy Notice page is opened
  And User can close new window
 And Switch to original window







