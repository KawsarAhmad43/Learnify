# Task: Weird Digits

## Objective
Train a One-Class SVM or Isolation Forest on distinct digits (e.g., '0') and see if it can flag different digits (e.g., '9') as anomalies.

## Data
`sklearn.datasets.load_digits()`

## Tasks
1.  **Train Data**: Filter dataset to only contain digit '0'.
2.  **Test Data**: Create a set containing digit '0' and digit '1'.
3.  **Detect**: Train `IsolationForest` on the Train Data (only 0s). Predict on Test Data.
4.  **Check**: Does it correctly label the '1's as outliers (-1)?
