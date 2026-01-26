# Task: Rank Calculation

## Objective
Calculate Adapter Size.

## Setup
*   Layer: $4096 \times 4096$ Weights.
*   Full Layer Params: $16,777,216$.

## Task
1.  LoRA Rank $r = 16$.
2.  Matrix A: $4096 \times 16 = 65,536$.
3.  Matrix B: $16 \times 4096 = 65,536$.
4.  Total LoRA Params: $131,072$.
5.  Percentage: $131,072 / 16,777,216 \approx 0.0078 (0.78\%)$.

## Question
What happens if you increase Rank to 4096?
*   Answer: You are training the same number of parameters as the full layer. LoRA loses its advantage. LoRA hypothesis is that the \"True Rank\" of the change is low, so Low Rank is sufficient.
