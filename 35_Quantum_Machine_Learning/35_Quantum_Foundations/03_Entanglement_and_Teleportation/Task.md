# Task: Superdense Coding

## Objective
Efficiency.

## Setup
*   **Teleportation**: Send 2 Classical Bits -> Transmit 1 Qubit.
*   **Superdense Coding**: Send 1 Qubit -> Transmit 2 Classical Bits.

## Task
1.  Alice wants to send "00", "01", "10", or "11" to Bob.
2.  She has 1 Qubit (entangled with Bob).
3.  She applies a gate:
    *   buffer ("00") -> Do nothing (I).
    *   buffer ("01") -> Z gate.
    *   buffer ("10") -> X gate.
    *   buffer ("11") -> iY gate.
4.  She sends HER qubit to Bob.
5.  Bob now has BOTH qubits. He performs a Bell Measurement.
6.  **Task**: Implement this circuit. Verify that Bob recovers the 2 bits.

## Question
What is 'Monogamy of Entanglement'?
*   Answer: If A is maximally entangled with B, neither A nor B can be entangled with C. You cannot clone entanglement.
