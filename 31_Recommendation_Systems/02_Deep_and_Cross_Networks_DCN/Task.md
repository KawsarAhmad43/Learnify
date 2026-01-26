# Task: Feature Crossing

## Objective
Manual vs Learned.

## Setup
*   **Manual**: You write code: `df['combo'] = df['country'] + '_' + df['language']`. (e.g., \"US_en\").
*   **Learned**: You feed `country` and `language` into a Cross Network.

## Task
1.  Manual crossing is exhaustive (Combinatorial Explosion). If you have 10 features, you need 45 pairs. 120 triples.
2.  DCN does this automatically.
3.  **Task**: Use `torch.nn.Linear` to approximate a Cross Layer. Is it possible?
    *   Yes, theoretically (Universal Approximation Theorem).
    *   No, practically. MLP needs HUGE width to learn multiplicative interactions (X * Y). Cross Layer does it naturally.

## Question
What is 'Wide & Deep'?
*   Answer: The predecessor to DCN. It had a Linear part (Wide) for memorization and a MLP part (Deep) for generalization.
