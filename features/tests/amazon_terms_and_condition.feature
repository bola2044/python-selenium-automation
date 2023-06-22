Feature: Amazon terms and Condition page

 Scenario: User can get to Amazon sign in page
  Given Open amazon main page
  When User clicks on orders button
   Then User can see sign-in page

 Scenario: User can get to condition of use
  Given Open amazon main page
  Then User can see sign-in page
  When Click on condition of use button
  And Opens amazon help page
  Then User can see help content

 Scenario: User can open and close Amazon Privacy Notice
  Given User is on amazon help page
  When Store original windows
  And Click on Amazon Privacy Notice link
  And Switch to the newly opened window
  Then Verify Amazon Privacy Notice page is opened
  And User can close new window
  And switch back to original window







