# Task: Iris Clustering

## Objective
Group Iris flowers into 3 clusters using K-Means.

## Data
`sklearn.datasets.load_iris()`

## Tasks
1.  **Load Data**: Use `iris.data`. Ignore targets.
2.  **Find Optimal K**: Plot the Elbow Curve for K=1 to 10. (Verify the elbow is around 3).
3.  **Cluster**: Fit K-Means with `n_clusters=3`.
4.  **Visualize**: Scatter plot 2 dimensions (e.g., Sepal Length vs Width) colored by cluster label.
