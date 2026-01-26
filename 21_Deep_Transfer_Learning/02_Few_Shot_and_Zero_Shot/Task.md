# Task: 3-Way 1-Shot

## Objective
Simulate an episode.

## Support Set
1.  **Class A**: Vector [0, 0]
2.  **Class B**: Vector [10, 0]
3.  **Class C**: Vector [0, 10]

## Query
*   Vector Q: [2, 2]

## Task
1.  Calculate distance to A: $\sqrt{(2-0)^2 + (2-0)^2}$.
2.  Calculate distance to B: $\sqrt{(2-10)^2 + (2-0)^2}$.
3.  Calculate distance to C: $\sqrt{(2-0)^2 + (2-10)^2}$.

## Question
Which class is Q?
*   A is roughly 2.8 distance.
*   B is roughly 8.2 distance.
*   C is roughly 8.2 distance.
*   Answer: A.

Write a script to confirm.
