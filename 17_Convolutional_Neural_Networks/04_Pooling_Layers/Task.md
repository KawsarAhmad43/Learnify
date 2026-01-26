# Task: Implement Average Pooling

## Objective
Max Pooling is good, but sometimes Average Pooling is smoother.

## Task
1.  Copy the code from the Implementation notebook.
2.  Create a new function `avg_pool(image)`.
3.  Change `np.max` to `np.mean`.
4.  Run it on the same 4x4 mock data.

## Mock Data
```python
 [[1, 3, 2, 4],
  [5, 6, 1, 2],
  [8, 2, 1, 0],
  [1, 0, 7, 5]]
```

## Expectation
*   Top-Left (1,3,5,6) -> Average is 3.75.
*   Top-Right (2,4,1,2) -> Average is 2.25.
