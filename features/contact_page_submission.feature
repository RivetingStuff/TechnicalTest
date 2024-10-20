Feature: Contact page submission 

Background: 
    Given the user navigates to the homepage
    And   the user clicks on the contact button

Scenario: Missing mandatory contact fields produce warning banner (Test case 1-1)
    When the user submits an incomplete form 
    Then the warning banner displays "- but we won't get it unless you complete the form correctly."

Scenario: Missing mandatory contact fields doesn't block submission (Test case 1-2)
    Given the user has submitted an incomplete form
    When  the user enters the forename "Example"
    And   the user enters the email "email@example.com"
    And   the user enters the message "Example message"
    And   the user submits the form 
    Then  the success banner displays the message "Thanks Example, we appreciate your feedback"

Scenario: User can submit the contact form (Test case 2) 
    When the user enters the forename "Example"
    And  the user enters the email "email@example.com"
    And  the user enters the message "Example message"
    And  the user submits the form 
    Then the success banner displays the message "Thanks Example, we appreciate your feedback"