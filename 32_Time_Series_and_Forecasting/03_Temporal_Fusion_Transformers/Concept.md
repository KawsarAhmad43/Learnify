# Temporal Fusion Transformers (TFT)

## 1. Why Transformers for Time Series?
*   LSTMs process step-by-step (Sequential).
*   Transformers process the whole history at once (Attention).
*   **Result**: They can catch long-range dependencies ("The sales spike every 4 years for the Olympics") much better.

## 2. Multi-Horizon Forecasting
*   **Goal**: Don't just predict $t+1$. Predict $[t+1, t+2... t+30]$ (Next 30 days) with confidence intervals.
*   **Static vs Dynamic Features**:
    *   **Static**: Store Location, ID. (Doesn't change).
    *   **Dynamic**: Price, Day of Week. (Changes).
    *   TFT treats these differently using specialized encoders.

## 3. Interpretable Attention
*   TFT is designed to be **Interpretable**.
*   It tells you: "I predicted high sales because I attended to the 'Holiday' feature 7 days ago."
