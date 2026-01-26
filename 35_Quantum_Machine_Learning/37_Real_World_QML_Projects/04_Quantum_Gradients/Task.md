# Task: Adjoint Differentiation

## Objective
Speed.

## Setup
*   **Parameter Shift**: Requires 2 runs per parameter. If you have 1 Million parameters, you need 2 Million runs. Too slow.
*   **Backpropagation**: Classical Neural Nets use backprop (1 forward, 1 backward pass).
*   **Adjoint Differentiation**: A quantum method similar to backprop. It stores the state vector at each step (requires memory) and reverses the computation.
*   **Cost**: Time $\approx$ 1 run. Memory $\approx$ High.

## Task
1.  **Comparison**: Use `diff_method="parameter-shift"` vs `diff_method="adjoint"` (if using `lightning.qubit` simulator).
2.  **Task**: Measure the wall-clock time for a circuit with 20 qubits and 50 parameters. Adjoint should be 10x faster.

## Question
What is 'Quantum Tangent Kernel'?
*   Answer: In the limit of infinite width, a Quantum Neural Network behaves like a Linear Model using a fixed Kernel (Quantum Tangent Kernel). This suggests that training deep QNNs might not be better than just using a good Kernel Method.
