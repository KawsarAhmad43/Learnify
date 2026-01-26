# Professional ML: Problem Definition

## 1. The Business Context
*   **The Problem**: A specific Turbofan Engine part costs \$2M. If it fails mid-flight, it's catastrophic. If we replace it too early, we waste money.
*   **The Goal**: Predict the **Remaining Useful Life (RUL)** of the engine based on sensor data (Temperature, Vibration, Fuel Flow).
*   **Constraints**:
    *   **Latency**: Predictions must be made every 5 seconds (Real-time).
    *   **Interpretability**: Mechanics need to know *why* the model says it's failing (High Vibration?).

## 2. Metric Strategy
*   **Accuracy is useless**: In maintenance, 99.9% of the time, the machine is fine. A model that always says "Working" is 99.9% accurate but useless.
*   **Regression Metrics (for RUL)**:
    *   **RMSE (Root Mean Square Error)**: Penalizes large errors heavily. Good for general fit.
    *   **Asymmetric Loss**: Late prediction (predicting 50 days when truth is 10) is WORSE than early prediction (predicting 10 days when truth is 50). We must penalize overestimation of RUL.

## 3. Data Strategy
*   **Type**: Time-Series Sensor Data (Multivariate).
*   **Frequency**: 1Hz sampling.
*   **Challenge**: Noisy sensors, Missing Data during maintenance downtime.
*   **Train/Test Split**: CANNOT be random. Must be **Temporal Split**. (Train on Jan-Oct, Test on Nov-Dec).
