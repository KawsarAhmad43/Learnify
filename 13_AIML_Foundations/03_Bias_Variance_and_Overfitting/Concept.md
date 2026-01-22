# Bias, Variance, and Overfitting

## 1. Scenario: Real Estate Price Prediction
Imagine you are trying to predict housing prices based on interest rates.
*   **Truth**: The relationship is curved. As rates drop, prices skyrocket exponentially. As rates rise, prices cool down but don't go negative.

## 2. Underfitting (High Bias)
You assume the relationship is a **Straight Line** ($y = mx + b$).
*   **Result**: The model is too simple. It fails to capture the "skyrocketing" prices at low rates.
*   **Diagnosis**: High Error on Training Data AND High Error on Test Data.
*   **The Fix**: Increase Model Complexity (use a curve/polynomial).

## 3. Overfitting (High Variance)
You use a **15th-Degree Polynomial** that passes through every single data point perfectly, including the random noise (outliers).
*   **Result**: The curve wiggles wildly. If you predict for a new interest rate slightly different from your training data, the prediction will be completely wrong.
*   **Diagnosis**: Zero Error on Training Data but Huge Error on Test Data.
*   **The Fix**:
    *   **More Data**: Forces the model to smooth out.
    *   **Regularization**: Constrain the model (Ridge/Lasso).
    *   **Simplify**: Use a lower degree polynomial.

## 4. The Sweet Spot
A model (e.g., Degree 2 or 3) that captures the main trend but ignores the noise.
