# Task: Latency Cost

## Objective
Calculate the trade-off.

## Setup
*   Retrieval (Top 100): 50ms (Vector DB is fast).
*   Reranking (Score 1 pair): 10ms (BERT forward pass).
*   Total Search Time = Retrieval + (N_Rerank $\times$ Time_Rerank).

## Task
1.  Case A: Rerank Top 10.
    *   $50 + (10 \times 10) = 150$ms. (Fast).
2.  Case B: Rerank Top 100.
    *   $50 + (100 \times 10) = 1050$ms. (1 second).
3.  User Tolerance: < 500ms.

## Question
What is the optimal strategy?
*   Answer: Retrieve Top 100, Rerank Top 40. Or use a smaller/distilled Cross-Encoder (TinyBERT) that takes only 1ms.
