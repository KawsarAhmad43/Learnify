# Task: Bias and Variance

## Task 1: The Validation Curve
In the implementation notebook, we looked at Training MSE.
1.  Copy the code.
2.  Generate a **separate** Test Set (`X_test_new`, `y_test_new`) of 20 points.
3.  Loop through degrees from 1 to 15.
4.  For each degree:
    *   Train on the Training Set.
    *   Calculate MSE on Train Set.
    *   Calculate MSE on Test Set.
5.  Plot `Train MSE` and `Test MSE` vs `Degree` on the same graph.
6.  Identify the degree where Test MSE is lowest. This is the sweet spot.

## Task 2: Regularization
1.  Use `sklearn.linear_model.Ridge` instead of `LinearRegression`.
2.  Train a Degree 15 polynomial (which was overfitting) but with `Ridge(alpha=1.0)`.
3.  Plot the result. Does the line wiggle less?
