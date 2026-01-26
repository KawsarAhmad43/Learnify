# Task: Add Validation Split

## Objective
Split the data *before* creating the Dataset objects.

## Context
You have `all_files` (list of 100 strings).

## Task
1.  Import `train_test_split` from `sklearn.model_selection`.
2.  Split `all_files` into `train_files` (80%) and `val_files` (20%).
3.  Create two instances of `ImageDataset`: `train_ds` and `val_ds`.
4.  Print their lengths.

## Hint
```python
train_X, val_X = train_test_split(all_files, test_size=0.2)
train_ds = ImageDataset(train_X, ...)
```
