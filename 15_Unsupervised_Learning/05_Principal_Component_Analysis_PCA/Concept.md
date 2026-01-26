# Principal Component Analysis (PCA)

## 1. The Concept
PCA is a **Dimensionality Reduction** technique. It takes a dataset with many features (e.g., 50) and simplifies it to a few "Principal Components" (e.g., 2 or 3) while keeping as much information as possible.

## 2. How it works
1.  **Find Direction of Max Variance**: PCA looks for the direction in space where the data is most spread out. This becomes **PC1**.
2.  **Orthogonal Direction**: It then finds a second direction, perpendicular to PC1, that captures the *next* most variance. This is **PC2**.
3.  **Project**: The data is rotated and projected onto these new axes.

## 3. Key Terms
*   **Explained Variance Ratio**: How much of the total info does PC1 hold? (e.g., 85%).
*   **Eigenvalues**: The magnitude of variance in each direction.
*   **Scree Plot**: A chart showing variance vs component number. Used to decide how many components to keep.

## 4. Why use it?
*   **Visualization**: Plot high-D data in 2D.
*   **Compression**: Reduce file size.
*   **Noise Reduction**: Dropping lower components often removes noise.
