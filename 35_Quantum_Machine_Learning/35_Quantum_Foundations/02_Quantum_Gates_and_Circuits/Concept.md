# Quantum Gates and Circuits

## 1. Single Qubit Gates
*   **X (Pauli-X)**: Bit Flip. $|0\rangle \to |1\rangle$. (Like NOT).
*   **Z (Pauli-Z)**: Phase Flip. $|0\rangle + |1\rangle \to |0\rangle - |1\rangle$.
*   **H (Hadamard)**: Creates Superposition. $|0\rangle \to \frac{|0\rangle + |1\rangle}{\sqrt{2}}$.

## 2. Multi-Qubit Gates
*   **CNOT (Controlled-NOT)**: The "If" statement of Quantum.
    *   If Control Qubit is 1, Flip Target Qubit.
    *   If Control is 0, Do nothing.
*   **Importance**: CNOT creates **Entanglement**.

## 3. The Circuit Model
*   A Quantum Algorithm is just a sequence of Gates (Music Sheet).
*   Qubits flow left to right (Time).
*   Gates are the notes.
*   Measurement is the final bar line.
