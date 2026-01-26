# Task: Stability of Explanation

## Objective
Robustness.

## Setup
*   LIME relies on Random Sampling (Perturbation).
*   Run LIME on the same image twice.

## Task
1.  Run 1: Says \"Ears\" are most important.
2.  Run 2: Says \"Nose\" is most important.
3.  This is **Instability**.

## Question
Why is LIME unstable?
*   Answer: Because the local linear model is an *approximation* built on random noise. If you don't sample enough points, the line wiggles.
*   **Fix**: Increase `num_samples` (e.g., from 1000 to 5000), or use SHAP (which guarantees consistency).
