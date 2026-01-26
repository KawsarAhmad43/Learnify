# Task: QRAM

## Objective
The bottleneck.

## Setup
*   Loading 1 million images into a quantum computer is slow.
*   You need $O(N)$ gates to prepare a state representing $N$ data points. This kills the speedup.
*   **QRAM (Quantum RAM)**: A bucket-brigade architecture that can query $N$ memory cells in $O(\log N)$ superposition.

## Task
1.  **Simulation**: Since QRAM hardware doesn't exist, simulate it.
2.  **Task**: Create a circuit that takes an address sequence (e.g., $|01\rangle$) and retrieves the data from a hardcoded list $[5, 9, 2, 7]$.
    *   If input $|01\rangle$ (Index 1), Output should be $|9\rangle$ (Value 9).
    *   Hint: Use Controlled-SWAP gates (Fredkin Gates).

## Question
What is 'Quantum Supremacy'?
*   Answer: The moment a Quantum Computer performs a task that is *impossible* for any Classical Supercomputer to do in reasonable time. Google claimed this in 2019 (Sycamore processor, 53 qubits) with a Random Circuit Sampling task.
