# Task: Simpson's Paradox

## Objective
Statistical traps.

## Setup
*   Hospital A has higher survival rate (90%) than Hospital B (80%).
*   Conclusion: Hospital A is better.

## Task
1.  Look closer (Break down by Difficulty).
2.  Easy Cases: Hospital A (95%), Hospital B (99%). (B is better).
3.  Hard Cases: Hospital A (50%), Hospital B (60%). (B is better).
4.  Why is A's total higher? Because A takes ONLY Easy Cases. B is a specialist center taking all the Hard cases.

## Question
How does this relate to XAI?
*   Answer: A model might learn \"feature importance\" that is misleading if confounders exist. Just because \"Hospital Name = A\" correlates with survival, doesn't mean it CAUSES survival. XAI explains *correlated* predictions, not necessarily *causal* truth.
