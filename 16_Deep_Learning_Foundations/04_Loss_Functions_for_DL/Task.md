# Task: Calculate the Loss

## Objective
Manually calculate the Binary Cross-Entropy Loss for a single example.

## The Data
*   **True Label ($y$)**: 1 (Positive Class)
*   **Prediction ($\hat{y}$)**: 0.2 (Model is 80% sure it's negative)

## Formula
$$ L = -[y \log(\hat{y}) + (1-y) \log(1-\hat{y})] $$

## Tasks
1.  Plug the numbers into the formula.
2.  Calculate the result (use `np.log` natural log).
    *   Note: $y=1$, so the second term $(1-1)$ becomes 0. You only need $-1 * \log(0.2)$.
3.  **Result Interpretation**: Is this valid? We predicted 0.2 for a 1. That's a bad prediction. Is the loss high or low?
    *   Compare it if the prediction was 0.9. (Calculate $-1 * \log(0.9)$).
