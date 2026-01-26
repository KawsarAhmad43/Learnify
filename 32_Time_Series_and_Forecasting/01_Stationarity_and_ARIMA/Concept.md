# Stationarity and ARIMA

## 1. Stationarity
*   **Definition**: Mean and Variance do not change over time.
*   **Why it matters**: Standard statistics assumes the rules of the game don't change.
*   **Problem**: Stock prices are NOT stationary. They trend up. They have volatility shocks.
*   **Solution**: Differencing. $y'_t = y_t - y_{t-1}$. (Predict the *change*, not the price).

## 2. ARIMA Components
*   **AR (Auto-Regressive)**: Tomorrow depends on Today. $y_t = \alpha y_{t-1}$.
*   **I (Integrated)**: The number of times we Differenced the data to make it stationary.
*   **MA (Moving Average)**: Tomorrow depends on the *Error* we made today. $y_t = \beta \epsilon_{t-1}$.

## 3. The ACF Plot
*   **Auto-Correlation Function**: How correlated is Today with Yesterday? With 2 days ago?
*   If correlation drops to zero after Lag 1, use AR(1).
