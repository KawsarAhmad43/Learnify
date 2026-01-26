# Task: Reversibility

## Objective
Everything must be reversible.

## Setup
*   **Classical**: `AND` gate. Input: 0, 1 -> Output: 0.
*   If I tell you the Output is 0, can you tell me the Input? No. It could be (0,0), (0,1), or (1,0). Information was lost (Heat).
*   **Quantum**: All operations must be Unitary (Reversible). No info can be lost until measurement.
*   **Toffoli Gate**: The reversible version of AND. It needs 3 Qubits (Control 1, Control 2, Target).

## Task
1.  **Inverse**: Every gate has an inverse. $UU^\dagger = I$.
2.  **Task**: Create a circuit that does `H -> X -> H`. Run it in PennyLane.
3.  Then add the inverse operations: `H -> X -> H` followed by `H -> X -> H`. Since $X$ is its own inverse and $H$ is its own inverse, you should end up exactly where you started ($|0\rangle$).

## Question
What is 'Quantum Volume'?
*   Answer: A metric invented by IBM. It measures the *effective* power of a computer, combining Qubit Count, Error Rate, and Connectivity. 100 noisy qubits are useless. 10 perfect qubits are powerful.
