# Task: Customer Churn (Imbalance)

## Objective
Handle imbalance in a churn dataset.

## Simulation
A telecom company has 1000 customers. Only 50 of them churned (5%).
Features: `Usage_Minutes`, `Contract_Length`.

## Tasks
1.  **Generate Data**: Use the provided code in the solution to generate this imbalanced dataset.
2.  **Baseline**: Train a Random Forest classifier. Check the F1-score for class 1 (Churn).
3.  **Improve**:
    *   Method A: Use `class_weight='balanced'` in Random Forest.
    *   Method B: Upsample the minority class manually using `sklearn.utils.resample` (replace=True).
4.  Compare the results. Which method gave better Recall for Churn?
