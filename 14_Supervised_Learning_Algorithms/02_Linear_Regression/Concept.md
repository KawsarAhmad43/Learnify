# Linear Regression

## 1. Scenario: Advertising Sales
A company wants to predict Sales based on how much they spend on TV, Radio, and Newspaper ads.
*   **Goal**: Find the relationship between Ad Spend ($X$) and Sales ($Y$).

## 2. Key Concepts
*   **The Equation**: $y = b_0 + b_1 x_1 + b_2 x_2 + ...$
    *   $b_0$: Intercept (Base sales with no ads).
    *   $b_1$: Coefficient for TV (How much sales increase for every $1 on TV).
*   **Cost Function (MSE)**: We want to minimize the Mean Squared Error (the distance between the line and the data points).
*   **Assumptions**:
    *   Linearity (The relationship is a straight line/plane).
    *   Homoscedasticity (Constant variance of errors).
    *   Normality of residuals.

## 3. Ordinary Least Squares (OLS)
The standard method for finding the best line using closed-form algebra.

## 4. Gradient Descent
An iterative method to find the best line by slowly moving "downhill" to minimize error. Used in large-scale ML (like Neural Networks) where OLS is too expensive.
