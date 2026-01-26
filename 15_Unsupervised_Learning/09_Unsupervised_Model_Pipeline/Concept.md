# Unsupervised Model Pipelines

## 1. Why Pipelines here?
In Supervised learning, Pipelines prevent data leakage. In Unsupervised learning, Pipelines are about **Architecture**.
*   **The Problem**: "Curse of Dimensionality". K-Means fails if you have 10,000 features (like pixels or words).
*   **The Solution**: Chain a **Dimensionality Reducer** (PCA/SVD) before the **Clusterer**.

## 2. Common Architectures
*   **The "Standard" Clusterer**:
    *   `StandardScaler` (Normalize range)
    *   `PCA` (Remove noise/Reduce dims)
    *   `KMeans` (Cluster)
*   **The "LSA" (Latent Semantic Analysis) for Text**:
    *   `TfidfVectorizer` (Text to Sparse Matrix)
    *   `TruncatedSVD` (Sparse Matrix to Dense Concepts)
    *   `KMeans` (Cluster on Concepts)

## 3. Searching for Hyperparameters
Even without labels, we can tune!
*   How many clusters ($K$)?
*   How many PCA components?
*   Use `GridSearchCV` with a custom scorer (like `silhouette_score`) to find the best pipeline configuration.
