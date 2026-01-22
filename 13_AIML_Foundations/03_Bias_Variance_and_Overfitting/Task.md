# Task: Taming Overfitting

## Objective
Fix an overfitted model using Regularization.

## Data
We have a very small, noisy dataset of 10 points generated from a cubic function ($y=x^3$).

## Tasks
1.  **Overfit**: Fit a **Degree 10** Polynomial Regression. Plot it. Observe the wild oscillations.
2.  **Regularize**: Fit a **Ridge Regression** (L2 Regularization) with the same Degree 10 features.
    *   Use `sklearn.linear_model.Ridge(alpha=1.0)`.
    *   Plot the new curve. Notice how it is much smoother, effectively "ignoring" the high-degree freedom to prevent overfitting.
