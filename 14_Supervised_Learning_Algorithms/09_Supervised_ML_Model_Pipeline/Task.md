# Task: Cascading Models (Regression -> Classification)

## Objective
Implement a "Cascading" pipeline where a Regression model helps a Classification model.

## Scenario: Used Car Sales
1.  **Model A (Regression)**: Predicts the *price* a car will sell for.
2.  **Model B (Classification)**: Uses the predicted price to classify if the sale is "Good Deal" (Price < Market Value).

## Tasks
1.  **Data**: Use the `diamonds` dataset (`sns.load_dataset('diamonds')`).
2.  **Step 1**: Train a `LinearRegression` to predict `price`.
    *   Generate predictions (`y_pred_price`) for the test set.
3.  **Step 2**: Create a classification target:
    *   `is_premium` = 1 if `cut` is 'Premium' or 'Ideal', else 0.
4.  **Step 3**: Train a `LogisticRegression` to predict `is_premium`.
    *   **Crucial**: Use `y_pred_price` as an **Input Feature** for this second model!
    *   Does knowing the predicted price help guess if it's a premium cut?
