# Hierarchical Clustering

## 1. The Concept
Unlike K-Means, Hierarchical Clustering builds a hierarchy of clusters. It doesn't require pre-specifying $K$.
*   **Result**: A tree-like structure called a **Dendrogram**.

## 2. Types
1.  **Agglomerative (Bottom-Up)**: Start with $N$ data points as $N$ clusters. Merge the two closest ones. Repeat until only 1 cluster remains.
2.  **Divisive (Top-Down)**: Start with 1 giant cluster. Split recursively. (Less common).

## 3. Linkage Methods
How do we measure distance between two clusters?
*   **Ward**: Minimize variance (most common).
*   **Complete**: Distance between furthest points.
*   **Single**: Distance between closest points (Chain reaction risk).

## 4. Dendrogram
A visual diagram where the Y-axis represents the distance at which a merge happened.
*   **Cutting the Tree**: You can draw a horizontal line across the dendrogram to "cut" it into $K$ clusters.
