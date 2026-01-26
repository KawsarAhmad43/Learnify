# LSTM for Time Series

## 1. Sliding Windows
*   **Method**: Convert a Time Series problem into a Supervised Learning problem.
*   **Input**: $[t-3, t-2, t-1]$.
*   **Target**: $[t]$.
*   If we have 1000 days of data, we create 997 training examples of window size 3.

## 2. Why LSTM?
*   ARIMA is linear. It fails on complex patterns (e.g., "If stocks fell for 3 days, they usually rebound, UNLESS it's a Friday").
*   RNNs/LSTMs have **Internal State (Memory)**.
*   They can sequence historical context that is longer than the sliding window is explicitly showing, if trained statefully.

## 3. The Vanishing Gradient Problem
*   Standard RNNs forget things after 10 time steps.
*   LSTMs (Long Short-Term Memory) use **Gates** (Input, Forget, Output) to keep information alive for 1000+ steps.
