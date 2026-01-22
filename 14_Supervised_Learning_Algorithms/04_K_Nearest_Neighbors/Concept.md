# K-Nearest Neighbors (KNN)

## 1. Scenario: User Recommendation
We want to recommend a movie to Alice.
*   **Logic**: Find 5 users who are most similar to Alice (her neighbors). If they liked "Titanic", Alice probably will too.

## 2. Key Concepts
*   **Lazy Learning**: KNN doesn't "train" a model. It just memorizes the training data. Predictions happen at runtime by searching.
*   **Distance Metrics**:
    *   **Euclidean**: Straight line distance ($ \sqrt{(x_1-x_2)^2 + ...} $).
    *   **Manhattan**: Grid distance ($ |x_1-x_2| + ... $).
*   **K**: The number of neighbors to vote.
    *   Small K (e.g., 1): Sensitive to noise (Overfitting).
    *   Large K: Smoother boundaries (Underfitting bias).

## 3. Pros and Cons
*   **Pros**: Simple, Handles non-linear data well.
*   **Cons**: Slow prediction on large datasets (must calculate distance to EVERY point).
