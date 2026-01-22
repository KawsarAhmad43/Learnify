# Logistic Regression

## 1. Scenario: Student Admission
A university wants to predict if a student will be Admitted (1) or Rejected (0) based on their Exam Score.
*   **Goal**: Find the probability of Admission.

## 2. Key Concepts
*   **Logistic Function (Sigmoid)**: S-shaped curve that squashes any output between 0 and 1.
    *   $\sigma(z) = \frac{1}{1 + e^{-z}}$
*   **Decision Boundary**: The threshold (usually 0.5). If $P(y=1) > 0.5$, classify as 1.
*   **Log Loss (Binary Cross-Entropy)**: The cost function. We penalize confident wrong predictions heavily.

## 3. Why not Linear Regression?
*   Linear regression predicts values like -5 or 150, which makes no sense for probability.
*   Linear regression fits a straight line, which doesn't handle the "S-shape" transition from 0 to 1 well.
