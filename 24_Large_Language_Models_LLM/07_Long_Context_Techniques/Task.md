# Task: KV Cache Size

## Objective
Calculate VRAM cost of context.

## Setup
*   Model: Llama-3-70B.
*   Layers: 80.
*   Dim: 8192.
*   FP16: 2 bytes per element.
*   KV Cache stores 2 vectors (Key + Value) per token per layer.

## Task
1.  Size per token: $80 \times 8192 \times 2 \times 2 = 2.6$ MB per token.
2.  Context: 128k tokens.
3.  Total Size: $128,000 \times 2.6 \text{ MB} \approx 332$ GB.

## Question
The Model weights are only 140GB. Why does the Cache take 332GB?
*   Answer: Attention memory scales clearly with context length. For long context, the Cache is bigger than the Model.
*   **Solution**: GQA (Grouped Query Attention) reduces this by 8x by sharing Keys/Values heads.
