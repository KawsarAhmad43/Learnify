# Evaluators: NDCG and MRR

## 1. Why NOT Accuracy?
*   In RecSys, we don't care if you predicted 0 or 1 for *every item*.
*   We care about the **Top 10**.
*   If the user likes "Star Wars", and you put it at Rank #1000, that's a failure (even if you correctly predicted "User likes Star Wars").
*   **Rank Matters**.

## 2. MRR (Mean Reciprocal Rank)
*   Used when there is only *one* correct answer (e.g., Next Word Prediction, or "Find the exact item I searched for").
*   Formula: $1 / \text{Rank}$.
    *   Found at Rank 1 -> Score = 1.0.
    *   Found at Rank 2 -> Score = 0.5.
    *   Found at Rank 10 -> Score = 0.1.

## 3. NDCG (Normalized Discounted Cumulative Gain)
*   Used when there are *multiple* good answers, and they have relevancy scores (5 stars vs 3 stars).
*   **CG**: Sum of relevance scores in Top K.
*   **DCG**: Discount the score if it's lower in the list (divide by $\log_2(\text{rank}+1)$).
*   **NDCG**: Normalize so the perfect ordering has a score of 1.0.
