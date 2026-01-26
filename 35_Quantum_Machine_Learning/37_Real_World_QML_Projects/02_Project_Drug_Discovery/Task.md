# Task: Tapering Qubits

## Objective
Optimization.

## Setup
*   $LiH$ requires 12 qubits naively.
*   But molecules have **Symmetries** (Z2 Symmetries).
*   If we know the total spin is 0, we can remove some qubits because their state is determined by the others.

## Task
1.  **Analyze**: Use `qml.qchem.taper_operation` to find symmetries in the $LiH$ Hamiltonian.
2.  **reduce**: Taper off 2-4 qubits.
3.  **Run**: Simulate the reduced Hamiltonian. It should run much faster and give the same result.

## Question
What is 'Active Space'?
*   Answer: Core electrons (deep inside) don't participate in bonding. We can "freeze" them and only simulate the valence electrons (Active Space). This drastically reduces the number of qubits needed.
