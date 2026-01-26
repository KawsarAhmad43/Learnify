# Task: Probability Density

## Objective
Use GMM to estimate the density of Iris data.

## Data
`sklearn.datasets.load_iris()`

## Tasks
1.  **Fit GMM**: Use `n_components=3`.
2.  **Generate Samples**: Use `gmm.sample(100)` to generate *new, synthetic* Iris flowers.
3.  **Check Probabilities**: Pick a real sample and use `score_samples` to see its log-likelihood.
