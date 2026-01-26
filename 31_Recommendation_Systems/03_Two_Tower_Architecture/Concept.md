# Two-Tower Architecture

## 1. The Bottleneck
*   Traditional models take (User, Item) pairs as input.
*   To find the best movie for User A, you must pair User A with *every single movie* in the database (Millions).
*   Latency = O(N). Too slow.

## 2. The Solution: Two Towers
*   **User Tower**: Processes User Features -> User Vector $u$.
*   **Item Tower**: Processes Item Features -> Item Vector $v$.
*   **Crucial Insight**: The Item Vector $v$ ONLY depends on the item. It does not depend on the user.
    *   This means we can **Pre-compute** all Item Vectors and store them in a FAISS index (Vector DB).

## 3. Inference
*   When User A logs in, we compute $u$.
*   We query the Vector DB: "Find the 10 $v$'s closest to $u$". (Approximate Nearest Neighbor).
*   Latency = O(log N). Highly scalable.
