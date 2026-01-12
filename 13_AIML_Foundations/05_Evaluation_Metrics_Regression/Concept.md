# Evaluation Metrics: Regression

In Regression, we predict continuous numbers (like House Price). Concepts like "Accuracy" or "Precision" don't exist here.

## Core Metrics

### 1. Mean Absolute Error (MAE)
$$ MAE = \frac{1}{m} \sum |y_{true} - y_{pred}| $$
*   **Intuition**: The average magnitude of error. "On average, our house price prediction is off by $5k".
*   **Pros**: Robust to outliers. Interpretability.

### 2. Mean Squared Error (MSE)
$$ MSE = \frac{1}{m} \sum (y_{true} - y_{pred})^2 $$
*   **Intuition**: Penalizes large errors heavily (because of squaring).
*   **Cons**: Hard to interpret (units are squared dollars).

### 3. Root Mean Squared Error (RMSE)
$$ RMSE = \sqrt{MSE} $$
*   **Intuition**: Same units as target.
*   **Use Case**: Standard metric for most regression problems.

### 4. R-Squared ($R^2$)
Measures "Goodness of Fit".
*   $R^2 = 1.0$: Perfect predictor.
*   $R^2 = 0.0$: Same performance as just predicting the mean of the data.
*   $R^2 < 0$: Worse than predicting the mean (the model is terrible).
