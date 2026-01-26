# Task: Quantile Loss

## Objective
Uncertainty.

## Setup
*   Your boss asks: \"What will sales be tomorrow?\"
*   You say: \"100 units\".
*   Tomorrow it is 80. You were wrong.
*   Better answer: \"Between 80 and 120 units with 90% confidence\".

## Task
1.  **Quantile Regression**: Instead of training to minimize MSE (Mean Squared Error), train to minimize Quantile Loss.
2.  Predict P10 (10th percentile), P50 (Median), and P90 (90th percentile).
3.  **Result**: You generate a \"Cone of Uncertainty\".

## Question
What is 'DeepAR'?
*   Answer: Amazon's autoregressive RNN. It predicts a probability distribution (Gaussian/NegativeBinomial) at each step, rather than a single number. This allows Monte Carlo sampling for future paths.
