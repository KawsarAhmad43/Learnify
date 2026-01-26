# Task: Option Pricing

## Objective
Monte Carlo simulation.

## Setup
*   **Problem**: Estimating the fair price of an Option involves calculating the Expected Value of the underlying stock price distribution.
*   **Classical**: Monte Carlo Integration. Convergence rate: $O(1/\sqrt{N})$.
*   **Quantum**: Quantum Amplitude Estimation (QAE). Convergence rate: $O(1/N)$.
*   **Speedup**: Quadratic speedup. (1 Million samples -> 1000 samples).

## Task
1.  **Input**: A probability distribution $P(x)$ (e.g., Log-Normal for stocks). Load it into a quantum state.
2.  **Operator**: Create an operator $A$ that encodes the payoff function.
3.  **Task**: Use `qml.AmplitudeEstimation` to estimate $\langle A \rangle$.
4.  **Compare**: Check precise convergence vs classical Monte Carlo.

## Question
What is 'Reverse Annealing'?
*   Answer: A technique in D-Wave. Start in a classical state (Candidate Solution), turn *on* quantum fluctuations (Tunneling), let it explore locally, then freeze it again. Great for refining existing good solutions.
