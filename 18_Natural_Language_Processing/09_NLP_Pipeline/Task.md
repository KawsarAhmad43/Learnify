# Task: Truncation Strategy

## Objective
Handle sequences that are too long.

## Constraints
*   Max Sequence Length = 5.
*   Input: `[1, 2, 3, 4, 5, 6, 7]`

## Strategies
1.  **Head-only**: Keep first 5.
2.  **Tail-only**: Keep last 5.
3.  **Head+Tail**: Keep first 2 and last 3.

## Task
Write a function `truncate(seq, strategy)` that implements these 3 logics.
Run it on the input.

## Why Head+Tail?
In sentiment analysis of long documents, the intro (Head) and conclusion (Tail) often contain the sentiment, while the middle is fluff.
