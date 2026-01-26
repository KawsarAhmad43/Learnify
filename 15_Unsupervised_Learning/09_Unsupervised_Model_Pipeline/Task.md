# Task: The Anomaly Pipeline

## Objective
Build a robust anomaly detection pipeline for "noisy" cancer data.

## Data
`sklearn.datasets.load_breast_cancer()`

## Tasks
1.  **Pipeline**:
    *   `RobustScaler`: Scales data but is immune to outliers (unlike StandardScaler).
    *   `PCA`: Reduce to 10 components.
    *   `IsolationForest`: Detect anomalies.
2.  **Run**: Fit on the data.
3.  **Count**: How many outliers (-1) did it detect?
