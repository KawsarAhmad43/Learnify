# Task: Active vs Total Params

## Objective
Calculate efficiency.

## Setup (Mixtral 8x7B)
*   Experts: 8.
*   Size per Expert: 7B.
*   Shared Attention Params: 10B.
*   Total Params: $8 \times 7 + 10 = 66B$. (Rough math).
*   Active Experts: 2.

## Task
1.  Calculate Active Params: $2 \times 7 + 10 = 24B$.
2.  Calculate Ratio: $24 / 66 \approx 0.36$.
3.  We run 36% of the brain for each token.

## Question
Why don't we activate all experts (Ensemble)?
*   Answer: It would be 3x slower. The goal of MoE is to maintain constant cost while increasing total knowledge capacity.
