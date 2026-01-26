# Task: Calculate Parameters

## Objective
Train your intuition on model size.

## The Layer
*   **Input**: 5x5 image, 3 Channels.
*   **Layer**: Conv2D(Filters=10, Kernel=3x3, Stride=1, Padding=1).

## Task
1.  How many weights are in the Kernel?
    *   Hint: Each kernel is 3x3x(Input Channels).
    *   There are 10 Filters.
2.  How many biases? (1 per filter).
3.  Total Parameters?

## Answer Key
*   Kernel: $3 \times 3 \times 3 = 27$ weights per filter.
*   Total Weights: $27 \times 10 = 270$.
*   Total Biases: $10$.
*   Grand Total: 280 parameters.

Write a python script to verify this calculation logic.
