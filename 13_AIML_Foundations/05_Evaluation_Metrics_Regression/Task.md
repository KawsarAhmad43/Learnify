# Task: Regression Metrics

## Task 1: Calculate RMSE
Using the `y_true`, `y_pred_A`, and `y_pred_B` from the notebook:
1.  Calculate RMSE for Model A.
2.  Calculate RMSE for Model B.

## Task 2: Create a Baseline
1.  Load the "California Housing" dataset from `sklearn.datasets`.
2.  Split into Train/Test.
3.  Create a "Dummy Regressor" that always predicts the **median** of the training labels.
4.  Calculate its MAE and RMSE on the Test set. This is your baseline to beat.

## Task 3: The Outlier Effect
1.  Create a small dataset `X = [1, 2, 3, 4, 5]`, `y = [1, 2, 3, 4, 100]`.
2.  Fit a Linear Regression.
3.  Calculate MAE.
4.  Remove the outlier (100) and refit. Calculate MAE.
5.  Compare how much the line moved.
