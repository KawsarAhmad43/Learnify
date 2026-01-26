# Gaussian Mixture Models (GMM)

## 1. The Concept
K-Means generates **Hard Labels** (Point A belongs to Cluster 1, 100%).
GMM generates **Soft Labels** (Point A is 80% Cluster 1, 20% Cluster 2).
*   **Idea**: Not all clusters are circles. GMM allows clusters to be stretched (ellipses) and calculates the *probability* of belonging to each.

## 2. Methodology (EM Algorithm)
1.  **Expectation (E)**: Calculate the probability of each point belonging to each Gaussian distribution.
2.  **Maximization (M)**: Update the mean and covariance of the Gaussians to fit the points better.

## 3. Selecting Components
We use **BIC** (Bayesian Information Criterion) or **AIC** to pick the number of components. Lower is better.
