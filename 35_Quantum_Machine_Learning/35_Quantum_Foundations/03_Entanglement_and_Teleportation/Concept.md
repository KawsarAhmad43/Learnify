# Entanglement and Teleportation

## 1. Bell States
*   If we have a state $\frac{|00\rangle + |11\rangle}{\sqrt{2}}$, the two qubits are perfectly correlated.
*   If you measure Qubit A and see 0, Qubit B **instantly** becomes 0.
*   If you measure Qubit A and see 1, Qubit B **instantly** becomes 1.
*   This happens faster than the speed of light (Non-locality), but **cannot transmit information** faster than light (No-communication theorem).

## 2. Quantum Teleportation
*   **Goal**: Move a qubit state $|\psi\rangle$ from Alice to Bob.
*   **Method**:
    1.  Alice and Bob share an entangled pair.
    2.  Alice performs a measurement on her qubit and the entangled qubit.
    3.  Alice sends the 2 bits of measurement result to Bob (via classical phone/internet).
    4.  Bob applies a correction gate (X or Z) based on the 2 bits.
    5.  Bob's qubit transforms into $|\psi\rangle$.
*   **Result**: The state was destroyed at Alice's end and recreated at Bob's end. (Copying is impossible due to the No-Cloning Theorem).
