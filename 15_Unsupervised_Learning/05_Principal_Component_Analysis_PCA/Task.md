# Task: The Scree Plot

## Objective
Determine how many components are needed to explain 95% variance of the Breast Cancer dataset (30 features).

## Data
`sklearn.datasets.load_breast_cancer()`

## Tasks
1.  **Fit PCA**: Use `n_components=None` to keep all components initially.
2.  **Plot Variance**: Plot `np.cumsum(pca.explained_variance_ratio_)`.
3.  **Find Threshold**: Identifying the index where cumulative variance crosses 0.95.
