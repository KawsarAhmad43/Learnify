# Task: Proxy Variables

## Objective
The Redlining problem.

## Setup
*   You remove \"Race\" from your dataset to be \"blind\".
*   You keep \"Zip Code\".
*   In segregated cities, Zip Code is highly correlated with Race.
*   The model learns to use Zip Code as a proxy for Race.
*   **Result**: The model is still racist, but now it's harder to prove.

## Task
1.  Identify proxies.
2.  Use **Adversarial Debiasing**.
    *   Train a \"Debiasing Network\" that tries to predict Race from the Embedding.
    *   Train the Main Network to maximize Accuracy BUT minimize the Debiasing Network's success.
    *   Result: An embedding that predicts the outcome but *contains no information* about Race.

## Question
What is 'Fairness through Unawareness'?
*   Answer: The (naive) idea that removing sensitive attributes solves bias. As shown above, it fails due to proxies.
