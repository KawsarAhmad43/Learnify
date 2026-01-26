# Task: Compute vs Quality Tradeoff

## Objective
Design a pipeline budget.

## Setup
*   Model Inference Cost: $0.01 per image.
*   Reward Model Cost: $0.001 per image.
*   Budget: $10.00.
*   Target: Get the single best image possible.

## Task
1.  Strategy A: Generate 1 image. Cost $0.01. (Standard).
2.  Strategy B: Generate 1000 images, Score them, keep top 1.
    *   Gen Cost: $1000 \times 0.01 = \$10.00$.
    *   Score Cost: $1000 \times 0.001 = \$1.00$.
    *   Total: \$11.00 (Over budget!).
3.  Optimize Strategy B to fit budget.

## Question
How many images can we generate and score for exactly $10?
*   $N \times 0.01 + N \times 0.001 = 10$.
*   $N(0.011) = 10$.
*   $N = 909$.
*   Answer: Generate 909 images, pick the best one. This result will be significantly better than Strategy A.
