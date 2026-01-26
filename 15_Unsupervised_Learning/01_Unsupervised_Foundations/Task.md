# Task: Dimensionality Reduction

## Objective
Visualize the MNIST Digits dataset (64 features) in just 2D.

## Data
`sklearn.datasets.load_digits()`

## Tasks
1.  **Load Data**: Get `X` (data) and `y` (target labels).
2.  **PCA**: Use `sklearn.decomposition.PCA` to reduce `X` to **2 components**.
3.  **Scatter Plot**: Plot the 2 components. Use `c=y` to color the points by their digit.
    *   *Question*: Can you see distinct blobs for the numbers 0, 1, 2, etc?
