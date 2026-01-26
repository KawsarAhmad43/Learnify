# Task: Color Shift

## Objective
Simulate a simple domain shift and fix it manually.

## Data
*   Source: Mean 10.
*   Target: Mean 15.

## Task
1.  Assume `y = model(x)` works well when x is around 10.
2.  Now x comes in around 15. The model output is wrong.
3.  Implement a simple \"Normalization\" fix:
    *   `x_adapted = x - (Mean_Target - Mean_Source)`.

## Question
Why is `Batch Normalization` so good for Domain Adaptation? (Hint: It forces everything to Mean 0, Variance 1, effectively removing the shift).

Write a script to shift a list of numbers `[14, 15, 16]` back to the source distribution (centered at 10).
