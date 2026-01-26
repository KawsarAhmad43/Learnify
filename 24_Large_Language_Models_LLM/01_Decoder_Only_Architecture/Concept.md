# Decoder-Only Architecture (GPT)

## 1. The Shift
*   **Encoder-Decoder (T5, BERT)**: Read input, then write output. Good for translation.
*   **Decoder-Only (GPT, Llama)**: Just write. Treat input as the "prefix" of the writing.

## 2. Causal Masking
In self-attention, token $i$ can usually see all tokens.
In Decoder-Only, token $i$ can ONLY see tokens $0...i$. It cannot see $i+1$ (the future).
*   **Mask**: A triangular matrix of $-\infty$ that blocks future positions.
*   **Why?**: During training, we feed the whole sentence "The cat sat on the mat". We want the model to predict "cat" given "The", "sat" given "The cat", etc., all in parallel. If it sees "mat", it cheats.

## 3. Next Token Prediction
The only objective: Maximize $P(w_i | w_{0...i-1})$.
This simple objective, scaled up, leads to emergent reasoning.
