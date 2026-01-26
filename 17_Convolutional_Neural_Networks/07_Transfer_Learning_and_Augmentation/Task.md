# Task: Add Random Zoom

## Objective
Modify the augmentation pipeline.

## Task
1.  Copy the `augment` function from the implementation notebook.
2.  Add a "Zoom" step.
    *   Slice the center of the image (crop).
    *   Resize it back to original (Conceptually).
    *   Since we are using NumPy, just performing the crop is enough to simulate the "Zoom In" effect for now (assuming the downstream resizing happens later).
3.  Implement: `image[h_start:h_end, w_start:w_end]`.
4.  If the random chance > 0.5, perform a central crop of 80% of the image size.

## Example Code Idea
```python
h, w, _ = image.shape
start_h = int(h * 0.1)
end_h = int(h * 0.9)
# ...
crop = image[start_h:end_h, ...]
```
Note: You might need to resize it back if you want to stack them, but for this exercise, just returning the cropped numpy array is fine.
