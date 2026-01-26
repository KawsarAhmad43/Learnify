# Task: Context Window Budget

## Objective
Optimize prompt space.

## Setup
*   Model Limit: 4096 tokens.
*   Question: 100 tokens.
*   System Prompt: 200 tokens.
*   Retrieved Chunks: 500 tokens each.

## Task
1.  Space Available: $4096 - 300 = 3796$ tokens.
2.  Max Chunks: $3796 / 500 = 7.5$.
3.  We can fit ~7 chunks.

## Question
If you retrieve 20 chunks but can only fit 7, which ones do you pick?
*   Answer: **Reranking**. Use a high-precision Cross-Encoder to re-score the 20 chunks and pick the absolute best 7.
*   Why not just use the top 7 from the Vector usage? Because Vector search is approximate. Reranking ensures quality.
