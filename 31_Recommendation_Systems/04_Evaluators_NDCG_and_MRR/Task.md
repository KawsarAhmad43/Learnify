# Task: Diversity vs Relevance

## Objective
The Filter Bubble.

## Setup
*   Your model has perfect NDCG.
*   It recommends 10 items.
*   **Result**: 10 distinct versions of \"Spiderman\".
*   The user is bored. \"I already saw Spiderman, show me something else.\"

## Task
1.  **MMR (Maximal Marginal Relevance)**:
    *   Select Item 1 (Best Match).
    *   Select Item 2 (Best Match but *Dissimilar* to Item 1).
    *   Trade-off: $\lambda \cdot \text{Rel} - (1-\lambda) \cdot \text{Sim}$.
2.  **Serendipity**: Surprise the user with something they didn't know they liked.

## Question
What is 'Hit Rate'?
*   Answer: The simplest metric. Did the relevant item appear *anywhere* in the Top K? Yes/No. (Binary version of Recall).
