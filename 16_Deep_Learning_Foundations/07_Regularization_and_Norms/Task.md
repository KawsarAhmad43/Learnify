# Task: Apply L2 penalties

## Objective
Calculate the new loss after adding L2 regularization.

## Data
*   **MSE Loss**: 0.5
*   **Weights ($W$)**: `[0.1, 4.0, -0.5, 0.0]`
*   **Lambda ($\lambda$)**: 0.1

## Task
1.  **Calculate L2 Penalty**: sum of squared weights.
2.  **Scale it**: Multiply by lambda.
3.  **Total Loss**: MSE + penalty.
4.  **Reflection**: Which weight contributes most to the penalty? The `4.0`, right? The optimizer will try to shrink this weight aggressively in the next step.

Write a Python script to calculate this.
