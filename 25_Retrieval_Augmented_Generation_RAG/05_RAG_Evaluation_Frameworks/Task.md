# Task: Context Precision

## Objective
Measure Retrieval Quality.

## Setup
*   Query: \"Who is the CEO?\"
*   Retrieved Chunks (in order): [Chunk A (irrelevant), Chunk B (relevant), Chunk C (irrelevant)].
*   Ground Truth: The answer is in Chunk B.

## Task
1.  The relevant chunk is at Rank 2.
2.  Precision@1 = 0.
3.  Precision@2 = 0.5 (1 relevant / 2 total).
4.  Precision@3 = 0.33 (1 relevant / 3 total).
5.  Mean Reciprocal Rank (MRR) = $1 / Rank = 1/2 = 0.5$.

## Question
Why is MRR important?
*   Answer: Because humans rarely scroll past the first result. You want the Gold Chunk to be at Rank 1. Rerankers improve MRR significantly.
