Feature: Amazon terms and Condition page

 Scenario: User can open and close Amazon Privacy Notice
  When Open and Verify amazon help page opens
  When Store original windows
  And Click on Amazon Privacy Notice link
  And Switch to the newly opened window
  Then Verify Amazon Privacy Notice page is opened
  And User can close new window
  And switch back to original window







