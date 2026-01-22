# Task: Text and PCA

## Objective
Visualize unstructured and high-dimensional data.

## Tasks

### Task 1: Customer Review Cloud
1.  Create a large string containing simulated reviews (e.g., repeating words like "Great", "Bad", "Service", "Slow", "Fast").
2.  Generate and plot a **WordCloud**.

### Task 2: Wine Dataset PCA
1.  Load the Wine dataset (`sklearn.datasets.load_wine`). It has 13 features.
2.  Standardize the features (important for PCA!).
3.  Reduce it to 2 dimensions using `PCA`.
4.  Plot the scatter plot, coloring points by the wine class.
