# Anomaly Detection

## 1. The Concept
Identifying data points that are significantly different from the majority.
*   **Novelty Detection**: The training data is "clean" (all normal), we want to see if new data is normal.
*   **Outlier Detection**: The training data contains outliers, we want to clean it.

## 2. Methods
*   **Isolation Forest**: Randomly splits data. Outliers are easy to isolate (shallow tree depth). Normal points are hard to isolate (deep tree depth).
    *   *Best for high-dimensional big data.*
*   **Local Outlier Factor (LOF)**: Compares the density of a point to its neighbors. If it's in a low-density region compared to neighbors, it's an outlier.

## 3. Applications
*   Fraud Detection.
*   System Health Monitoring.
*   Defect Detection.
