# Task: The Diagonal Edge Detector

## Objective
Create a kernel that detects diagonal edges (lines going from Top-Left to Bottom-Right).

## The Kernel
Think about it:
*   Positive numbers on one diagonal.
*   Negative numbers on the other.
*   Example:
    ```
    [ 1,  0, -1]
    [ 0,  0,  0]
    [-1,  0,  1] or similar variations
    ```
    Actually, a better one for 45 degrees is:\
    ```
    [-1, -1,  2]
    [-1,  2, -1]
    [ 2, -1, -1]
    ```
    (Or simpler variations). 

## Task
1.  Define a 3x3 kernel that you think will catch diagonal lines.
2.  Apply it to the `china.jpg` image.
3.  Check if it highlights the diagonal architectural elements.
