# LSTMs and GRUs

## 1. Long Short-Term Memory (LSTM)
Designed to solve the Vanishing Gradient problem.
*   **The Cell State ($C_t$)**: A super-highway for gradients. Information flows through it almost unchanged.
*   **Gates**: Neural networks (Sigmoids) that decide what to add/remove from the Cell State.
    *   **Forget Gate**: "Should I keep this old memory?"
    *   **Input Gate**: "Is this new info important?"
    *   **Output Gate**: "What should I reveal to the next layer?"

## 2. Gated Recurrent Unit (GRU)
A simplified LSTM.
*   Merges Cell State and Hidden State.
*   Merges Forget and Input gates into an "Update Gate".
*   Faster to train, often just as good.

## 3. Why they work
In a standard RNN, gradients multiply ($0.1 \times 0.1 \dots$).
In an LSTM, gradients **add** ($1 + \dots$) because of the linear self-connection in the Cell State.
