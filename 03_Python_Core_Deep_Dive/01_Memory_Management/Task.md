# Tasks: Core Python

Complete the following tasks in a new notebook or Python script.

## Task 1: Efficient List Processing
Given a list of numbers `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`:
1.  Create a new list containing the squares of all even numbers using a **list comprehension**.
2.  Do the same using a standard `for` loop and compare the readability.

## Task 2: Data Cleaning Helper
Write a function `clean_data(data, strategy='drop')` that takes a list of values (some might be `None`) and a strategy string.
*   If `strategy` is 'drop', remove all `None` values.
*   If `strategy` is 'fill_zero', replace `None` with `0`.
*   Use `**kwargs` to accept an optional `fill_value` if the strategy is 'fill_custom'.

## Task 3: The `zip` and `enumerate` Challenge
You have two lists:
```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
```
1.  Use `zip` to combine them into a list of tuples: `[('Alice', 85), ...]`.
2.  Iterate over this combined list and print "Rank {i}: {name} got {score}" starting from Rank 1. Use `enumerate`.
