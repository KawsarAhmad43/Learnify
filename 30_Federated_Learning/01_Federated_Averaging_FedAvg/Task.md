# Task: Non-IID Data

## Objective
The Data Distribution problem.

## Setup
*   **IID (Independent and Identically Distributed)**: Everyone's data looks like the global average. (e.g., Everyone types a mix of words).
*   **Non-IID**:
    *   User A talks ONLY about Sports.
    *   User B talks ONLY about Cooking.
*   If User A trains the model, it forgets Cooking (Catastrophic Forgetting).
*   If User B trains the model, it forgets Sports.

## Task
1.  When you average them, the gradients might cancel out or point in a weird direction.
2.  **FedProx**: An improvement on FedAvg that adds a \"proximal term\" to the loss function, preventing the local model from drifting too far from the global model during local training.

## Question
What is 'System Heterogeneity'?
*   Answer: User A has an iPhone 15 (Fast). User B has an Android from 2015 (Slow). User B might drop out or take forever. FL algorithms must be robust to \"Stragglers\".
