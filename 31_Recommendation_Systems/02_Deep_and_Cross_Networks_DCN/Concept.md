# Deep & Cross Networks (DCN)

## 1. Feature Interaction
*   **Linear Model**: $y = w_1 x_1 + w_2 x_2$.
    *   Can learn: "People like Avengers".
    *   Cannot learn: "People like Avengers AND Popcorn". (Combined feature).
*   **Cross Network**: Explicitly learns interactions of bounded degree. $x_{next} = x_0 x^T w + b + x$.
*   **Deep Network**: Learns complex non-linear interactions implicitly.

## 2. The Architecture
*   **Input**: Dense Embeddings (User ID, Movie ID, Genre) + Dense Features (Age, Time of Day).
*   **Stack**: Parallel Deep Network and Cross Network.
*   **Output**: Probability of Click (CTR).

## 3. Why?
High-order feature crossing is critical for Ads Prediction.
"User is 18-25" AND "App is TikTok" AND "Time is Midnight" -> High Probability.
Linear models miss this. Deep models learn it slowly. DCN learns it explicitly and efficiently.
