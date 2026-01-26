# Variational Quantum Eigensolver (VQE)

## 1. The Physics Problem
*   Nature seeks the lowest energy state (Ground State).
*   Finding this state for a molecule tells us its chemical properties.
*   Schrödinger's Equation is hard to solve classically ($2^N$ complexity).

## 2. The Variational Principle
*   If you guess a wave function $|\psi\rangle$, its energy $E$ will always be greater than or equal to the true ground state energy $E_0$.
*   $E(\theta) = \langle \psi(\theta) | H | \psi(\theta) \rangle \ge E_0$.
*   **Goal**: Minimize $E(\theta)$ by tweaking parameters $\theta$.

## 3. Hybrid Algorithm
*   **Quantum Part**: Prepare state $|\psi(\theta)\rangle$ and measure energy $E$.
*   **Classical Part**: Use a classical optimizer (like Gradient Descent or COBYLA) to update $\theta$.
*   **Loop**: Repeat until convergence.
*   This is the "Hello World" of useful Quantum Computing.
