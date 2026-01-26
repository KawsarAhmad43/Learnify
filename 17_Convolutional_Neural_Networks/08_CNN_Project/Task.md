# Task: Add Dropout

## Objective
Modify the `SimpleCNN` class to include Dropout.

## Task
1.  Copy the code from the Implementation notebook.
2.  Insert a `"Dropout(50%)"` layer after the Flatten layer.
3.  Why there? Because the Dense layer explains most of the parameters (and thus overfitting).

## Expected Output
```
...
MaxPooling(2x2)
Flatten
Dropout(50%)  <-- New
Dense(128 Neurons)
...
```
