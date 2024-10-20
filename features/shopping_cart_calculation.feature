Feature: Shopping Cart Calculation

Scenario: Correct price information displayed in shopping Cart (Test Scenario 3)
    Given the user navigates to the homepage
    And   the user clicks on the shop button
    When  the user buys the following items
        | item_name      | amount | 
        | Stuffed Frog   | 2      |
        | Fluffy Bunny   | 5      |
        | Valentine Bear | 3      |
    And the user clicks on the Cart button 
    Then the itemized cart prices match the following
        | item_name      | price    |
        | Stuffed Frog   | 10.99    |
        | Fluffy Bunny   | 9.99     |
        | Valentine Bear | 14.99    |
    Then the itemized cart subtotals match the following
        | item_name      | subtotal |
        | Stuffed Frog   | 21.98    |
        | Fluffy Bunny   | 49.95    |
        | Valentine Bear | 44.97    |
    And the total cost displayed is "116.9"

