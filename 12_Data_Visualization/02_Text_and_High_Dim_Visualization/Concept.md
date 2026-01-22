# Text and High-Dimensional Visualization

## 1. Text Data
Text is unstructured. We visualize it by frequency or by embedding space.
*   **Word Cloud**: Size of the word represents its frequency compared to others.
*   **Bar Chart (Frequent Words)**: Simple counts of top-N words.

## 2. High-Dimensional Data
We often work with data with many features (10, 100, 1000 dimensions). We can't plot 1000 dimensions.
*   **Dimensionality Reduction**: Projecting data down to 2D or 3D for visualization.
    *   **PCA (Principal Component Analysis)**: Preserves global structure/variance. Good linear projection.
    *   **t-SNE (t-Distributed Stochastic Neighbor Embedding)**: Preserves local structure. Good for visualizing clusters, but computationally huge.
    *   **UMAP**: Faster alternative to t-SNE.

## 3. Scatter Plot of Embeddings
Once reduced to 2D, we just use a scatter plot. Points close together share similar features/meaning.
