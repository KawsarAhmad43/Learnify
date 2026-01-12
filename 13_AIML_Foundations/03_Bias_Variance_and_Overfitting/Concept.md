# Bias, Variance, and Overfitting

Success in ML is about finding the balance between simplicity and flexibility.

## 1. Definitions
*   **Bias (Underfitting)**: The error due to erroneous assumptions in the learning algorithm. High bias can cause an algorithm to miss the relevant relations between features and target outputs (underfitting).
    *   *Symptom*: High Train Error, High Test Error.
    *   *Analogy*: Studying for a Math test by only memorizing "1+1=2". You fail the test because you assume everything is addition.

*   **Variance (Overfitting)**: The error from sensitivity to small fluctuations in the training set. High variance can cause an algorithm to model the random noise in the training data, rather than the intended outputs (overfitting).
    *   *Symptom*: Low Train Error, High Test Error.
    *   *Analogy*: Memorizing every single practice question answer verbatim. If the test questions are slightly different, you fail.

## 2. The Tradeoff
*   **Simple Models** (e.g., Linear Regression) tends to have High Bias, Low Variance.
*   **Complex Models** (e.g., Deep Decision Trees, High-degree Polynomials) tend to have Low Bias, High Variance.

## 3. How to Fix It?
### Fixing High Bias (Underfitting)
*   Make model more complex (add features, add layers).
*   Train longer.

### Fixing High Variance (Overfitting)
*   **Regularization**: Penalize large weights (L1/L2).
*   **Data**: Get more training data.
*   **Feature Selection**: Remove irrelevant features (noise).
*   **Early Stopping**: Stop training before it memorizes noise.
