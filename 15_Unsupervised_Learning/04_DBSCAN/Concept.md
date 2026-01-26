# DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

## 1. The Concept
K-Means assumes clusters are spherical and fails on weird shapes (like moons or rings). DBSCAN looks for "dense" regions.
*   **Core Idea**: A cluster is a region where many points are packed closely together.

## 2. Key Parameters
*   **Epsilon ($\epsilon$)**: The radius around a point to search for neighbors.
*   **MinPts**: The minimum number of neighbors required to form a "Core Point".

## 3. Point Types
*   **Core Point**: Has at least MinPts within Epsilon.
*   **Border Point**: Within Epsilon of a Core Point, but has fewer than MinPts itself.
*   **Noise Point**: Neither Core nor Border. Effectively an outlier.

## 4. Pros and Cons
*   **Pros**: Finds arbitrary shapes. Robust to outliers (noise). No need to specify $K$.
*   **Cons**: Struggles if clusters have *varying* densities. Sensitive to Epsilon parameter.
