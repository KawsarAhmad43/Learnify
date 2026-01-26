# Project: Drug Discovery (VQE)

## 1. The Challenge
*   Simulating molecules is exponential. $LiH$ (Lithium Hydride) is simple. Caffeine is impossible for classical supercomputers.
*   **Problem**: We want to find the Ground State Energy vs Bond Length (Potential Energy Surface).
*   **Goal**: Understanding this allows us to predict reaction rates.

## 2. Molecular Hamiltonian
*   We convert the electrons and orbitals into Qubits using **Jordan-Wigner Mapping**.
*   Electron exists = $|1\rangle$. Electron missing = $|0\rangle$.
*   Hamiltonian $H = \sum h_i P_i$ (Weighted sum of Pauli strings).

## 3. The Algorithm (VQE)
*   **Ansatz**: UCCSD (Unitary Coupled Cluster Singles and Doubles).
*   **Optimizer**: L-BFGS-B (Classical).
*   **Result**: We get a curve. The minimum point is the equilibrium bond length.
