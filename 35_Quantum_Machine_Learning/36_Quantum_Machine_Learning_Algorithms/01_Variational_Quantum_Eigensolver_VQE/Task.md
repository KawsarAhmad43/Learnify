# Task: The Ansatz

## Objective
The architecture of the circuit.

## Setup
*   **Ansatz**: The template of the quantum circuit. It has adjustable parameters $\theta$.
*   **Hardware Efficient Ansatz**: Designed to run easily on specific hardware (e.g., only using nearest-neighbor CNOTs).
*   **Chemically Inspired Ansatz (UCCSD)**: Designed based on electron orbitals. More accurate but much deeper (more gates).

## Task
1.  **Barren Plateaus**: This is the "Vanishing Gradient" problem of Quantum. If your Ansatz is too deep and random, the gradient becomes exponentially small. You can't train it.
2.  **Task**: Change the Ansatz in the implementation. Add more layers ('Strongly Entangling Layers'). Observe if it converges faster or slower.

## Question
What is 'Trotterization'?
*   Answer: Simulating time evolution $e^{-iHt}$. If H = A + B, and A and B don't commute, we approximate it as $(e^{-iAt/n} e^{-iBt/n})^n$. This breaks a continuous time evolution into discrete gate steps.
