Feature: Original product filter

  As a user
  In order to see only original products
  I want to be able to select the "Original product" filter on the phone page

Scenario: Select the "Original product" filter
  Given I am on the phone page
  When I scroll to the "Brand" section
  And I select the "Original product" filter
  Then I should see the "Original product" text displayed on the page