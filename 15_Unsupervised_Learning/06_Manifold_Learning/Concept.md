# Manifold Learning (t-SNE & UMAP)

## 1. The Concept
PCA is linear (it rotates the data). But what if the data is a rolled-up scroll (Swiss Roll)? Use a ruler to measure distance between points on the roll would be wrong. You need to "unroll" the manifold.
*   **Goal**: Non-linear dimensionality reduction.

## 2. t-SNE (t-Distributed Stochastic Neighbor Embedding)
*   **Focus**: Keeping neighbors close. If A is close to B in high dimensions, they must be close in 2D.
*   **Cost**: It doesn't care about global distance. Far away points might end up anywhere.
*   **Use Case**: Visualization of clusters (MNIST, Fashion MNIST).

## 3. UMAP (Uniform Manifold Approximation and Projection)
*   **Focus**: Like t-SNE but faster and preserves more global structure.
*   **Trend**: UMAP is replacing t-SNE in many fields (especially single-cell biology).
