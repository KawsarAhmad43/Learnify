# Task: Readout Error Mitigation

## Objective
Fixing the sensor.

## Setup
*   Your Qubit is perfectly in state $|1\rangle$.
*   You measure it.
*   The measurement device has a 2% error rate. It reports 0.
*   This is a classical Readout Error.

## Task
1.  **Calibration Matrix (M)**: Measure a known state $|0\rangle$ 1000 times. Measure $|1\rangle$ 1000 times.
    *   Result: When prepared $|0\rangle$, measured 0 (98%), 1 (2%).
    *   Result: When prepared $|1\rangle$, measured 0 (3%), 1 (97%).
2.  **Inversion**: Calculate $M^{-1}$.
3.  **Task**: Apply $M^{-1}$ to your noisy experimental results to estimate the *true* probability distribution.

## Question
What is 'Shot Noise'?
*   Answer: Statistical noise. Even with a perfect quantum computer, you need to run the circuit many times (Shots) to estimate the probabilities $|\alpha|^2$. 10 shots is noisy. 10,000 shots is precise. (Law of Large Numbers).
