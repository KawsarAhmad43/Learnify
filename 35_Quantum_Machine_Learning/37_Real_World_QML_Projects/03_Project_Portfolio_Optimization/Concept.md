# Project: Portfolio Optimization (QAOA)

## 1. The Problem
*   You have \$1M. You want to buy stocks.
*   **Goal**: Maximize Return, Minimize Risk.
*   **Risk**: Variance (Volatility) and Covariance (Correlation). If Stock A falls, does Stock B fall too?

## 2. Modern Portfolio Theory (Markowitz)
*   Minimize $\sum \sigma_{ij} w_i w_j$ subject to $\sum \mu_i w_i = TargetReturn$.
*   If we restrict weights $w_i$ to be binary (Buy or Don't Buy), this becomes a combinatorial optimization problem (Knapsack-style).

## 3. Quantum Approach
*   Map the Covariance Matrix to an Ising Hamiltonian.
*   Pairs of stocks with high negative correlation correspond to "Ground State" configurations where you pick one but not the other (Anti-ferromagnetic).
*   Run QAOA to find the optimal bitstring.
