Feature: Test Add Two Numbers
As a user,
I want to use the employee System
So I can add and retrieve employee information

Scenario: Adding Positive Numbers
 Given I want to add two numbers with the add function
 When I pass in "5" and "4" to the function
 Then I should get "9"

Scenario: Adding Negative Numbers
 Given I want to add two numbers with the add function
 When I pass in "-6" and "1" to the function
 Then I should get "-5"
