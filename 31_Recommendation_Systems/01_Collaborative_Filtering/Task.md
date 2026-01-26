# Task: The Cold Start Problem

## Objective
New items.

## Setup
*   You built a great Matrix Factorization model.
*   **Problem**: A new movie is released today.
*   It has 0 ratings. It is not in the matrix.
*   The model predicts nothing. No one sees it. No one rates it. Loop of death.

## Task
1.  **Hybrid Approach**: Use Content-Based Filtering for new items.
    *   \"This new movie stars Tom Cruise and is an Action movie. Recommend it to people who like Tom Cruise.\"
2.  **Exploration**: Bandits.
    *   Randomly show the new movie to 1% of users to gather initial data (\"Warm Start\").

## Question
What is 'Sparsity'?
*   Answer: In a matrix of 1 Million Users x 100k Movies, 99.99% of entries are empty. If sparsity is too high, the model cannot learn patterns. Use Dimensionality Reduction.
