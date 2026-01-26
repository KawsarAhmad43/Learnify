# K-Means Clustering

## 1. The Concept
K-Means is the most popular clustering algorithm. It partitions data into **K** distinct non-overlapping subgroups (clusters).
*   **Centroid**: The center of a cluster.
*   **Goal**: Minimize the distance between points and their respective cluster centroid (Inertia).

## 2. How it works (Iterative)
1.  **Initialize**: Pick $K$ random points as centroids.
2.  **Assign**: Assign every data point to the nearest centroid.
3.  **Update**: Move the centroid to the *mean* (average) of the points assigned to it.
4.  **Repeat**: Steps 2-3 until centroids stop moving.

## 3. Choosing K (The Elbow Method)
How do we know if we need 3 clusters or 5?
*   Run K-Means for $K=1$ to $10$.
*   Calculate **Inertia** (Sum of Squared Errors) for each.
*   Plot Inertia vs K.
*   Look for the "Elbow" where the curve bends. That is the optimal K.
