# Research Project: Advanced House Price Prediction

## 1. Problem Understanding
*   **Context**: Predicting the final sale price of a home based on 79 variables (e.g., Basement Area, Year Built, Roof Style).
*   **The Data**: The [Ames Housing Dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques). A dataset famous for its complexity (mix of Nominal, Ordinal, Discrete, and Continuous features).
*   **The Trap**: Outliers. A 4000 sqft house selling for cheap (Foreclosure) will ruin your model's logic if not handled.

## 2. Research Strategy
*   **Target Transformation**: Price is usually right-skewed (Long tail of expensive houses). Models prefer Normal Distributions. We will predict `log(Price)` instead of `Price`.
*   **Feature Engineering**:
    *   **Ordinal Encoding**: `KitchenQual` (Ex, Gd, TA, Fa, Po) -> (5, 4, 3, 2, 1). This preserves the "rank".
    *   **One-Hot Encoding**: `Neighborhood` (No rank).
    *   **Interaction Features**: `TotalSqFt` = `BsmtFinSF1` + `1stFlrSF` + `2ndFlrSF`.
*   **Model Stacking**:
    *   A single model is rarely enough to win.
    *   **Level 1**: Ridge, Lasso, ElasticNet, GradientBoosting, XGBoost, LightGBM.
    *   **Level 2 (Meta-Model)**: A simple Lasso or Linear Regression that takes the predictions of Level 1 models as input and outputs the final price. This learns "Who to trust".

## 3. Step-by-Step Plan
1.  **EDA**: Check Skewness of Target. Log-transform it.
2.  **Cleaning**: Handle `NA`. In this dataset, `NA` in `PoolQC` means "No Pool", not "Missing Data". This is domain knowledge.
3.  **Encoding**: Manually map ordinal columns.
4.  **Training**: Train 5 different models.
5.  **Stacking**: Use `StackingCVRegressor` to combine them.
6.  **Submission**: Inverse transform the prediction `exp(pred)` to get real dollars.
