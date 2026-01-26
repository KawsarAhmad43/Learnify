# Task: Loop Optimization

## Objective
Cleaner logic.

## Setup
*   You have a function `get_data()` that returns a value or None.
*   You want to process the value repeatedly until it returns None.

## Task
1.  **Without Walrus**: Write a loop that calls `get_data()`, stores it in a variable, checks if it's None, breaks if so, or processes it. This usually takes 4-5 lines and repeating the call.
2.  **With Walrus**: Write the same logic in 2 lines: `while (val := get_data()) is not None: process(val)`.

## Question
What is `f-string`?
*   Answer: Formatted String Literals (Python 3.6). `f"Name: {name}"`. It is faster and more readable than `%` formatting or `.format()`. You can even put expressions inside: `f"{x + 1}"` or `f"{x=}"` (Python 3.8 debugging).
