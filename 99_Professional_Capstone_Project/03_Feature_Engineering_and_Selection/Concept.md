# Feature Engineering and Selection

## 1. Domain-Driven Features
*   Raw sensor data is noisy.
*   **Smoothing**: Use Rolling Mean to see the trend.
*   **Volatility**: Use Rolling Standard Deviation. A failing machine vibrates more irregularly.
*   **change Rates**: First Derivative ($\Delta T$). Is temperature rising quickly?

## 2. Advanced Signal Processing
*   **Fast Fourier Transform (FFT)**: Converts time-domain vibration signal into frequency-domain. Failing bearings scream at specific frequencies (e.g., 20kHz).
*   **Lag Features**: $T_{t-1}, T_{t-2}$. Helps models (even non-recurrent ones like XGBoost) understand time dependency.

## 3. Feature Selection
*   **The Curse of Dimensionality**: More features $\ne$ better model. Too many features = Overfitting + Slow Inference.
*   **Techniques**:
    1.  **Variance Threshold**: Remove features that are constant (Variance = 0).
    2.  **Correlation Matrix**: Remove collinear features (if feature A and B are 99% correlated, drop B).
    3.  **Recursive Feature Elimination (RFE)**: Train model -> Check feature importance -> Drop lowest -> Repeat.
