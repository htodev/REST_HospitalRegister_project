Feature: Manage UserProfile

  Background:
	Given I have the back-end service up
	And I login as a regular user

  Scenario: Get user profile
	When I sent a get request to "/accounts/profile/"
	Then I should receive response with code "200"
	And I should receive user data

  Scenario: Try change user email
	When I change my email
    Then The email should not be changed


  Scenario: Change username
	When I try to change my username
	Then I should receive user data with different username

  Scenario: Add allowed specialty
    When I send patch request with existing specialty
	Then I should be able to get this specialty

  Scenario: Try to add not allowed specialty
    When I send patch request with not existing specialty
	Then I should receive response with code "404"
    And I should receive error message
