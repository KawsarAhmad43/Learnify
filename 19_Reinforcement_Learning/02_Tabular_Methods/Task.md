# Task: Manual Update

## Objective
Perform one Bellman Update by hand.

## Setup
*   Current State $S$. Neighbor 1 (N1), Neighbor 2 (N2).
*   $V(N1) = 50$.
*   $V(N2) = 20$.
*   Reward to go to N1 is -1.
*   Reward to go to N2 is -1.
*   Gamma $\gamma = 0.9$.

## Task
1.  Calculate value of choosing N1: $R + \gamma V(N1)$.
    *   $-1 + 0.9 \times 50 = ?$
2.  Calculate value of choosing N2: $R + \gamma V(N2)$.
    *   $-1 + 0.9 \times 20 = ?$
3.  $V(S) = \max(\text{Option 1}, \text{Option 2})$.

## Question
Which neighbor does the agent prefer? N1 (Value 50) or N2 (Value 20)?
Clearly N1, but verifying the math confirms it.
