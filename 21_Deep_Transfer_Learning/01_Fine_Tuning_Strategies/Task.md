# Task: Learning Rate Decay

## Objective
Calculate Discriminative Learning Rates.

## Formula
$\eta^{l-1} = \eta^l / 2.6$ matches the ULMFiT paper recommendation.

## Setup
*   Top Layer (Head) LR: $1e-2$ (0.01).
*   We have 3 layers below it.

## Task
1.  Calculate LR for Layer -1 (0.01).
2.  Calculate LR for Layer -2 (0.01 / 2.6).
3.  Calculate LR for Layer -3 (LR_2 / 2.6).

## Question
Why do we divide? Why not multiply?
*   Answer: The lower layers need to stay closer to their pre-trained values (Lower LR = Less change). The top layers need to adapt fast.
