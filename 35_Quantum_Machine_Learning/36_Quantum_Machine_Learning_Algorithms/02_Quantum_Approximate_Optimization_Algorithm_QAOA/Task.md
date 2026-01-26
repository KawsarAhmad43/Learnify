# Task: QUBO Formulation

## Objective
Translation.

## Setup
*   Before running QAOA, you must translate your real-world problem into math.
*   **QUBO**: Quadratic Unconstrained Binary Optimization.
*   $f(x) = x^T Q x$.
*   Where $x$ are binary variables (0 or 1).

## Task
1.  **Knapsack Problem**: You have a bag with weight limit $W$. You have items with values $v_i$ and weights $w_i$.
2.  **Task**: Write the Cost Function.
    *   Maximize Value: $\sum v_i x_i$.
    *   Constraint: $\sum w_i x_i \le W$.
    *   Penalty Method: $Cost = -(\sum v_i x_i) + \lambda (\sum w_i x_i - W)^2$.
    *   Convert this to Pauli Z operators ($x_i \to (I-Z_i)/2$).

## Question
What is 'Quantum Annealing'?
*   Answer: D-Wave's approach. It's hardware specifically built to solve QUBOs. It physically evolves the system to the ground state. It is NOT a universal quantum computer (no gates), but it has 5000+ qubits and works for optimization today.
