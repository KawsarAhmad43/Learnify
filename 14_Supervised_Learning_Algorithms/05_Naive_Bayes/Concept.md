# Naive Bayes

## 1. Scenario: Spam Filtering
We want to classify an email as Spam or Ham based on words.
*   **Logic**: If an email contains "VIAGRA" and "FREE", the probability of it being Spam is high.

## 2. Key Concepts
*   **Bayes Theorem**: $P(A|B) = \frac{P(B|A) P(A)}{P(B)}$
*   **"Naive" Assumption**: We assume all features (words) are **independent** of each other.
    *   This is obviously False (words appear in phrases), but the model works surprisingly well anyway.
*   **Types**:
    *   **Gaussian**: For continuous data.
    *   **Multinomial**: For word counts (NLP).
    *   **Bernoulli**: For binary features (Word present/absent).

## 3. Pros and Cons
*   **Pros**: Extremely fast, works great for Text.
*   **Cons**: Fails if Independence assumption is heavily violated.
