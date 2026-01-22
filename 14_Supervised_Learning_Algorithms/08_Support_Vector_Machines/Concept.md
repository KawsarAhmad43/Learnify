# Support Vector Machines (SVM)

## 1. Scenario: Image Classification (Simple)
Classifying Handwritten Digits (MNIST) where the boundary might be high-dimensional and non-linear.

## 2. Key Concepts
*   **Hyperplane**: The line (or plane) that separates the classes.
*   **Margin**: The distance between the hyperplane and the nearest data points.
    *   **Goal**: Maximize the Margin. Wide streets are safer than narrow alleys.
*   **Support Vectors**: The specific data points located right on the edge of the margin. They are the "pillars" holding up the boundary.
*   **Kernel Trick**: What if data isn't linearly fitting?
    *   We project data into higher dimensions where it *becomes* linear.
    *   **RBF Kernel** (Radial Basis Function): The most common kernel for non-linear data.

## 3. Pros and Cons
*   **Pros**: Effective in high dimensional spaces.
*   **Cons**: Slow on large datasets. Hard to tune (C and Gamma parameters).
