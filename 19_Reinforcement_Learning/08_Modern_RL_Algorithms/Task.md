# Task: Clipping Math

## Objective
Calculate the clipped ratio.

## Constants
*   Epsilon $\epsilon = 0.2$.
*   Bounds: $[0.8, 1.2]$.

## Scenarios
1.  Old Prob = 0.5, New Prob = 0.55. Ratio = 1.1. Clipped?
2.  Old Prob = 0.5, New Prob = 0.8. Ratio = 1.6. Clipped?

## Task
1.  Calculate Ratio ($new / old$) for both cases.
2.  Apply `clip(ratio, 0.8, 1.2)`.
3.  State the final value used in the loss function.

## Interpretation
For Case 2, the ratio is capped at 1.2. The model \"wants\" to change the probability by factor 1.6, but PPO says \"No, we treat it as if you only changed it by 1.2\".
