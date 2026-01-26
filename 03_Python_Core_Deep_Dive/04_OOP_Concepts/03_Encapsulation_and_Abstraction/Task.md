# Task: Access Control

## Objective
Validation.

## Setup
*   You are building a `User` class.

## Task
1.  Create `User` with private attributes `__username` and `__password`.
2.  Use properties to allow reading the username, but NOT the password.
3.  Add a method `verify_password(input_password)` that returns True/False.
4.  Add a setter for password that enforces: "Password must be at least 8 characters".

## Question
What is 'Name Mangling'?
*   Answer: When you use `__var`, Python changes the name to `_ClassName__var` at runtime. This prevents child classes from accidentally overriding private variables of the parent class.
