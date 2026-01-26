# Task: Calculate Output Shape

## Objective
Calculate the output dimension manually.

## Parameters
*   **Input Image**: 28x28 (MNIST)
*   **Kernel**: 5x5
*   **Padding**: 2 (Two pixels on left, two on right, etc)
*   **Stride**: 1

## Formula Replacer
$$ Out = \frac{W - K + 2P}{S} + 1 $$

## Task
1.  Plug in the numbers.
2.  What is the output size? 
3.  Is this "Same" padding (Is Output == Input)?
4.  Write a check using the python function from the Implementation notebook.
