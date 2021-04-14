Feature: Enrollment feature

  Background:
	Given I have the back-end service up
	And I login as a regular user

  Scenario: Create enrollment
	When I send post request to create new enrollment
	Then I should receive response with code "201"
	And I should receive enrollment data

  Scenario: Update my own enrollment
    Given I send post request to create new enrollment
    When I sent a patch request to update the existing enrollment
    Then I should receive response with code "200"
    And I should receive enrollment object with different "patient_name,room_number"

  Scenario: Delete my own specific enrollment
    Given I send post request to create new enrollment
    And I sent a delete request to delete the existing enrollment
    And I should receive response with code "204"
    And I should NOT be able to get this enrollment

  Scenario: Get my existing enrollment
    When I send post request to create new enrollment
    Then I sent a get request to get my own specific enrollment
    Then I should receive response with code "200"
    And I should be able to get this enrollment


  Scenario: Get my all existing enrollment records
    Given I send post request to create new enrollment
	Then I sent a get request to get my all existing enrolment records
	And I should receive response with code "200"
	And I should be able to get my all enrolments