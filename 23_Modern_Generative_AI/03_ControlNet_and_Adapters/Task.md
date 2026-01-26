# Task: Edge Detection Logic

## Objective
Understand input preparation.

## Canny Edge Detector
1.  Smoothing (Gaussian Blur).
2.  Gradient Calculation (Sobel Filter).
3.  Non-maximum Suppression (Thinner lines).
4.  Thresholding.

## Task
1.  Input: A photo of a minimal room with white walls.
2.  Sobel Filter: Detects changes in intensity (The corners where walls meet).
3.  Output: A black image with white lines showing the room geometry.

## Question
Why does the ControlNet need the Edge Map and not the original photo?
*   Answer: We want to disentangle \"Structure\" (Edges) from \"Style\" (The original wall color). We want SD to keep the Structure but invent a NEW Style (e.g., Brick walls instead of White).
