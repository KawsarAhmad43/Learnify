# Noise and Error Mitigation

## 1. NISQ Era
*   **Noisy Intermediate-Scale Quantum**.
*   Current Quantum Computers (IBM, Google, Rigetti) are **Noisy**.
*   **Decoherence**: The environment interacts with the Qubits, causing them to lose their information (collapse) before the calculation is done.
*   **Gate Errors**: A CNOT gate is only 99% accurate. After 100 gates, the result is garbage.

## 2. Quantum Error Correction (QEC)
*   **Idea**: Use many physical qubits to encode 1 logical qubit. (Repetition Code).
*   **Problem**: Requires millions of qubits. We only have hundreds.

## 3. Error Mitigation (The Band-Aid)
*   Since we can't correct errors perfectly yet, we mitigate them.
*   **Zero Noise Extrapolation (ZNE)**:
    1.  Run the circuit with noise level $L$.
    2.  Intentionally adding MORE noise (run with $2L$, $3L$).
    3.  Fit a curve and extrapolate back to $L=0$.
