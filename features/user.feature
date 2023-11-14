@flask
Feature: Test Simple Flask App
As a user,
I want to use the flask app
So I can add, get and manipulate users

Background: User Records
Given a background to implement before every scenario

Scenario: Add User
    Given a user is to be added
    When I send a request with their id and name
    Then they are added as a user

@users
Scenario: Get All User
    Given users exist in the app
    When the details of all users is requested in the application
    Then it should have the details with their id and names

Scenario: Get A User Detail
    Given users exist in the app
    When the details of a user is requested
    Then it should respond with the detail of the user


