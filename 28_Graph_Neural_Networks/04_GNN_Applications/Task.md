# Task: Cold Start Problem

## Objective
New users.

## Setup
*   GNNs are great at recommending things to existing users (High Degree nodes).
*   **New User**: Degree = 0 (No friends, no clicks).
*   GNN fails because there are no messages to pass.

## Task
1.  Strategy 1: Fallback to Content-Based Recommendation (Use their demographic info).
2.  Strategy 2: **Self-Supervised Learning**.
    *   Pre-train the GNN by masking edges and asking it to predict them.
    *   This forces the model to learn general rules about node features ("Young people usually connect with Music nodes") even before specific edges are formed.

## Question
What is 'Temporal Graph Network'?
*   Answer: A GNN that handles time. Edges have timestamps. Standard GNNs assume static snapshots. TGNs process events as a stream.
