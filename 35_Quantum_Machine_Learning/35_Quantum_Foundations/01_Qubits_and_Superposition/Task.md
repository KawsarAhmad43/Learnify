# Task: The Bloch Sphere

## Objective
Visualization.

## Setup
*   A Qubit state $|\psi\rangle$ can be visualized as a point on the surface of a unit sphere.
*   North Pole = $|0\rangle$.
*   South Pole = $|1\rangle$.
*   Equator = Superposition states (e.g., $|+\rangle$).

## Task
1.  **Rotation**: If you apply an $X$ gate, you rotate 180 degrees around the X-axis (North Pole -> South Pole).
2.  **Rotation**: If you apply a $Y$ gate, you rotate around the Y-axis.
3.  **Task**: Start at $|0\rangle$. Apply $R_y(\pi/2)$. Where are you? (Answer: On the equator, $|+\rangle$).

## Question
What is 'Phase'?
*   Answer: The angle around the Z-axis (Longitude). Two states can have the same probability (50/50) but different phases (Positive vs Negative interference). This phase is crucial for algorithms like Grover's Search.
