# Task: Be the Neural Network

## Objective
Manually calculate the forward pass of a tiny network to understand the matrix math.

## The Network
*   **Input ($x$)**: `[1, 2]`
*   **Weights 1 ($W_1$)**: `[[1, 1], [-2, 1]]` (Rows are inputs, Cols are nodes)
    *   *Correction*: Standard convention usually is (Inputs x Nodes).
    *   Node 1 weights: `[1, -2]`
    *   Node 2 weights: `[1, 1]`
*   **Bias 1**: `[0, 0]`
*   **Activation 1**: ReLU
*   **Weights 2 ($W_2$)**: `[[1], [-1]]` (2 hidden nodes -> 1 output)
*   **Bias 2**: `[0]`
*   **Activation 2**: None (Identity)

## Tasks
1.  **Calculate $z_1$**: $x \cdot W_1 + b_1$
2.  **Calculate $a_1$**: ReLU($z_1$)
3.  **Calculate $output$**: $a_1 \cdot W_2 + b_2$
4.  **Verify**: Write a script to check your math.
