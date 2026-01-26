# Quantum Approximate Optimization Algorithm (QAOA)

## 1. The Problem: MaxCut
*   Imagine a graph with Nodes and Edges.
*   **Goal**: Color the nodes Black or White such that the number of edges connecting a Black node to a White node is MAXIMIZED.
*   This is an NP-Hard problem (Combinatorial Optimization).
*   Real world: VLSI Chip Layout, Portfolio Optimization, Logistics.

## 2. The Algorithm
*   QAOA is a specialized version of VQE.
*   **Mixer Hamiltonian ($H_M$)**: Encourages exploration (Superposition).
*   **Cost Hamiltonian ($H_C$)**: Encodes the problem (MaxCut).
*   **Strategy**: Apply $H_C$ for time $\gamma$, then $H_M$ for time $\beta$. Repeat $p$ times.
*   $|\psi(\gamma, \beta)\rangle = \dots e^{-i\beta H_M} e^{-i\gamma H_C} |+\rangle$.
*   This is inspired by **Adiabatic Quantum Computing** (Slowly evolving from a simple Hamiltonian to the complex one).

## 3. Quantum Advantage?
*   QAOA is one of the strongest candidates for proving that a Quantum Computer can beat a Classical Computer (at least for approximation ratios) in the NISQ era.
