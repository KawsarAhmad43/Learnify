# Task: Custom List

## Objective
Container Emulation.

## Setup
*   You want a list that starts indexing at 1 (like Lua/Matlab) instead of 0.

## Task
1.  Create `OneIndexedList` class.
2.  Implement `__init__(self, initial_data)`. Saving data in a private internal list.
3.  Implement `__getitem__(self, index)`. Adjust the index (`index - 1`) and return the element. Raise IndexError if out of bounds.
4.  Implement `__setitem__(self, index, value)`.
5.  Implement `__len__(self)`.
6.  Implement `__str__(self)`.
7.  **Test**: `my_list[1]` should return the first item. `my_list[0]` should fail.

## Question
What is `__call__`?
*   Answer: It allows an object to be called like a function: `obj()`. Very common in PyTorch (e.g., `model(input)` actually calls `model.__call__`, which calls `model.forward`).
