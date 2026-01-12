# Task: Data Splitting

## Task 1: Stratified Split
Sometimes your classes are imbalanced (e.g., 90% Cat, 10% Dog). A random split might put all Dogs in the test set.
1.  Create a dummy dataset where 90 samples are class '0' and 10 samples are class '1'.
2.  Use `train_test_split` with `stratify=y` parameter.
3.  Verify that both train and test sets have roughly the same 9:1 ratio.

## Task 2: Time Series Split
For stock prices, random splitting is wrong (predicting yesterday using tomorrow's data).
1.  Research `sklearn.model_selection.TimeSeriesSplit`.
2.  Apply it to a list `[1, 2, 3, 4, 5, 6]`.
3.  Print the indices for 3 splits. Observe how the training set grows.

## Task 3: The Leakage Trap
Write a short paragraph explaining why doing `Function(Whole_Dataset).Split()` is usually wrong compared to `Split().Function(Train).Function(Test)`.
