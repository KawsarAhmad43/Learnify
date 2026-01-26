# Task: Inductive vs Transductive

## Objective
Generalization.

## Setup
*   **Transductive**: You execute on the WHOLE graph during training. You know all nodes. (e.g., standard GCN). If a new user joins, you must re-train the whole graph.
*   **Inductive**: You learn a function $f(neighborhood)$. If a new user joins, you just apply the function to their local neighborhood. No re-training needed. (e.g., GraphSAGE).

## Task
1.  Social networks change every second (Inductive needed).
2.  Citation networks (Papers citing papers) change slowly (Transductive okay).

## Question
Why 'SAGE'?
*   Answer: SAmple and aggreGatE. Instead of summing ALL 1000 friends (too slow), randomly sample 20 friends and sum them. This makes it scalable.
