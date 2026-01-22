# Task: Broadcasting

## Objective
Use broadcasting to perform row/column-wise operations.

## Tasks

### Task 1: Normalization
Create a random matrix of shape `(10, 5)` (10 samples, 5 features).
1.  Calculate the mean of each feature (column).
2.  Subtract the mean from the matrix (center the data) using broadcasting.
3.  Verify that the new means are effectively 0.

### Task 2: Multiplication Table
Create a multiplication table (from 1 to 10) in a single line of code using broadcasting.
*   Hint: Reshape `arange(1, 11)` into column `(10, 1)` and row `(1, 10)` and multiply.
