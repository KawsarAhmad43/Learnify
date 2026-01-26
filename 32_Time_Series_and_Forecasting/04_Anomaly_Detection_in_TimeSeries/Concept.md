# Anomaly Detection in Time Series

## 1. Point Anomalies vs Contextual Anomalies
*   **Point**: A credit card purchase of $500,000. (Obvious outlier).
*   **Contextual**: A credit card purchase of $10 at 4 AM in a different country. ($10 is normal, but the context is suspicious).

## 2. AutoEncoders
*   **Method**: Train an LSTM AutoEncoder on *Normal Data* only.
*   **Reconstruction**: It learns to compress and decompress normal daily patterns.
*   **Detection**: When an Anomaly comes in, the AutoEncoder fails to reconstruct it (High Reconstruction Error).
*   **Threshold**: If Error > 3 StdDevs, Flag it.

## 3. Isolation Forest
*   For non-contextual point anomalies.
*   It randomly splits the data. Anomalies are "easy to isolate" (require fewer splits to separate).
*   Very fast, effectively O(N).
