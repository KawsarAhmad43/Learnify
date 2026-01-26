# Collaborative Filtering

## 1. The Core Intuition
*   **User A** likes: Star Wars, Matrix, Inception.
*   **User B** likes: Star Wars, Matrix.
*   **Prediction**: User B will probably like "Inception".
*   Why? Because User A and User B are *similar*.

## 2. Matrix Factorization (SVD)
*   Imagine a giant matrix $R$ where rows are Users and columns are Movies.
*   Most entries are empty (Sparse).
*   We decompose $R \approx U \times V^T$.
    *   $U$: User Embeddings (Preferences).
    *   $V$: Item Embeddings (Characteristics).
*   Prediction = $u_i \cdot v_j$ (Dot Product).

## 3. Explicit vs Implicit Feedback
*   **Explicit**: 5-star ratings. (High signal, but rare).
*   **Implicit**: Clicks, Watch Time, "Add to Cart". (Noisy, but massive volume).
*   Modern RecSys relies almost entirely on Implicit Feedback.
