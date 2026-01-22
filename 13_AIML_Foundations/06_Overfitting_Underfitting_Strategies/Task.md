# Task: The Doctor is In

## Objective
Diagnose and fix a model based on the Train/Test metrics.

## Scenario
You are using a **K-Nearest Neighbors (KNN)** classifier to predict diabetes outcome.
You trained it with `n_neighbors=1` (KNN-1).

## Initial Diagnosis
*   **Train Accuracy**: 100% (It memorized everyone because k=1 looks at itself).
*   **Test Accuracy**: 62% (Terrible generalization).

## Tasks
1.  **Replicate**: Create a dataset using `load_breast_cancer`. Split it. Fit `KNeighborsClassifier(n_neighbors=1)`. Confirm the scores.
2.  **Fix**: This is clearly **Overfitting** (High Variance).
    *   **Action**: Simplify the model by *increasing* `n_neighbors` (smoothing the boundary).
    *   Try `n_neighbors` = 5, 10, 20.
    *   Find the value that maximizes **Test Accuracy**.
