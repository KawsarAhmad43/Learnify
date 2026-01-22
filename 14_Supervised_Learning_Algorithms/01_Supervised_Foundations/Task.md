# Task: Diamonds - Classify or Regress?

## Objective
Convert a dataset into both a Regression problem and a Classification problem.

## Data
Use `sns.load_dataset('diamonds')`.
*   Features: `carat` (Weight).
*   Target: `price` ($).

## Tasks
1.  **Regression**: Train a Linear Regression model to predict `price` based on `carat`. Report the MSE.
2.  **Classification**: Create a new target column `is_expensive`.
    *   Set it to 1 if `price` > 5000, else 0.
    *   Train a Logistic Regression to predict `is_expensive` based on `carat`.
    *   Report the Accuracy.
