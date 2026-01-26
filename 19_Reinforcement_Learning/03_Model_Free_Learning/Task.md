# Task: Calculate Return

## Objective
Compute $G_t$ (Return) for an episode.

## Episode
1.  State A, Action Right, Reward 0.
2.  State B, Action Right, Reward 0.
3.  State C, Action Exit, Reward 10.
4.  Terminal.

## Discount ($\gamma = 0.9$)
Returns decay over time.

## Task
1.  Calculate Return at Step 3 ($G_2$).
    *   Immediate reward 10. Future is 0. So 10.
2.  Calculate Return at Step 2 ($G_1$).
    *   Immediate reward 0. Discounted Future $0.9 \times 10 = 9$. Total 9.
3.  Calculate Return at Step 1 ($G_0$).
    *   Immediate reward 0. Discounted Future $0.9 \times 9 = 8.1$. Total 8.1.

## Question
Why is the value of State A (8.1) lower than State C (10)? (Because you have to wait/survive to get the reward).

Write a script to verify this backwards calculation.
