# Task: Sorting Gaussians

## Objective
Understand computational bottlenecks in 3DGS.

## 3DGS Rendering
1.  Project 1 Million Gaussians to 2D.
2.  **Sort** them by depth (Z-distance).
3.  Composite them.

## Task
1.  Sorting 1 Million items ($N$).
2.  Complexity: $O(N \log N)$.
3.  $1,000,000 \times 20 = 20,000,000$ operations per frame.
4.  At 60 FPS = 1.2 Billion ops.

## Question
Why is Radix Sort preferred on GPU for this task?
*   Answer: Radix Sort is $O(kN)$, which is linear. It is faster than comparisons on massive parallel hardware. This sorting speed is the main reason 3DGS is real-time.
