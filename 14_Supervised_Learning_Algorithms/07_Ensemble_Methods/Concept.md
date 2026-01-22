# Ensemble Methods

## 1. Scenario: High-Stakes Kaggle Competition
A single Decision Tree is good, but 1000 trees are better.
*   **Ideally**: We want the "Wisdom of Crowds". Aggregating guesses usually beats a single expert.

## 2. Bagging (Bootstrap Aggregating)
*   **Example**: **Random Forest**.
*   **How**: Train hundreds of trees on random subsets of the data (Bootstrap). Let them **vote**.
*   **Why**: Reduces Variance (Overfitting). A single tree is noisy; the average of 100 trees is robust.

## 3. Boosting
*   **Example**: **XGBoost, Gradient Boosting, AdaBoost**.
*   **How**: Train trees **sequentially**. Tree 2 tries to fix the mistakes of Tree 1. Tree 3 fixes Tree 2, etc.
*   **Why**: Reduces Bias. Can maximize accuracy on difficult data.
*   **Note**: Boosting is currently the state-of-the-art for tabular data.
