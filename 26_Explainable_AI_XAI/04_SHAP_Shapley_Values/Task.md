# Task: Computational Complexity

## Objective
The price of truth.

## Setup
*   $N$ features.
*   Shapley value requires iterating through all possible subsets (Coalitions).
*   Number of subsets: $2^N$.

## Task
1.  If $N = 10$, $2^{10} = 1024$. (Fine).
2.  If $N = 100$, $2^{100} \approx 10^{30}$. (Impossible).

## Question
How do we use SHAP on large datasets (e.g., Images with 1M pixels)?
*   Answer: Approximations.
    *   **KernelSHAP**: Uses sampling (like LIME) but with specific weights to approximate Shapley values.
    *   **TreeSHAP**: Optimized for Decision Trees (XGBoost), runs in $O(TLD^2)$ time instead of exponential time.
