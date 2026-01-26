# Task: Library Management System

## Objective
Basic Class Design.

## Setup
*   You are building a system for a Library.

## Task
1.  Create a `Book` class with attributes: `title`, `author`, `isbn`, `is_borrowed`.
2.  Create a `Library` class that holds a list of `Book` objects.
3.  Add methods to `Library`:
    *   `add_book(book)`
    *   `borrow_book(isbn)`: Sets `is_borrowed` to True if available.
    *   `return_book(isbn)`: Sets `is_borrowed` to False.
4.  **Task**: Create a library, add 3 books, borrow one, and try to borrow it again (should fail).

## Question
What is the difference between `__str__` and `__repr__`?
*   Answer: `__str__` is for end-users (readable). `__repr__` is for developers (ambiguous, ideally executable code to recreate the object).
