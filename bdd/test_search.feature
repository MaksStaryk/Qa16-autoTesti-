Feature: Add to Basket

  As a customer
  I want to add a phone to my basket
  So that I can purchase it later

Scenario: Add phone to basket

  Given I am on the phone page
  When I click on the 'Add to Basket' button for a phone
  Then I should see the basket icon update to '1'
  And the basket icon should be displayed