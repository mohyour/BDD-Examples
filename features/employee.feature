Feature: Test Employee System Functionality
As a user,
I want to use the employee System
So I can add and retrieve employee information 


Scenario Outline: Creating employee
  Given new employees are hired by the company
  When I register their details with "<ID>", "<name>" and "<department>"
  Then the employee should be created with details "<ID>", "<name>", "<department>"

  Examples:
    | ID | name | department |
    | 1 | Sharon | Product |
    | 2 | Boyle | HR |
    | 3 | Musa | Data |

  But if employee already exist with the same ID
  Then it should fail to register the new employee


Scenario: Getting all employees
  Given employees already exist in the system
  When I query all employees
  Then I have the total number of registered employees


Scenario Outline: Getting employee details
  Given employees already exist in the system
  When I input an id of "<ID>"
  Then employee should be returned with id "<ID>" and name "<name>"

  Examples:
    | ID | name |
    | 3 | Musa |
    | 1 | Sharon |
    | 2 | Boyle |

Scenario Outline: Updating employee details
  Given employees already exist in the system
  And I want to update employee's details
  When I input their ID "<ID>" and new department "<department>"
  Then employee details should be updated with new "<department>"

  Examples:
    | ID | department |
    | 3 | Operations |
    | 1 | Technology |

Scenario Outline: Deleting employee details
  Given employee no longer works with the company
  And I want to delete employee's details
  When I input their ID to delete
  Then employee details should be removed from the system
  But should fail if employee does not exist