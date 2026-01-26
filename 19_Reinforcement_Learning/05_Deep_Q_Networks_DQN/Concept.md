# Deep Q-Networks (DQN)

## 1. The Problem with Tables
Q-Tables work for small states (GridWorld).
*   Atari Game Screen: $210 \times 160$ pixels $= 256^{33600}$ states.
*   The Universe runs out of atoms before you can build that table.

## 2. Function Approximation
Instead of a lookup table, use a Neural Network to **predict** $Q(s, a)$.
*   Input: Pixels (State).
*   Output: 4 Numbers (Q-values for Up, Down, Left, Right).

## 3. Tricks to make it Stable
Training RL with NNs is unstable (moving target).
1.  **Experience Replay**: Save memories $(s, a, r, s')$ in a buffer. Train on random batches (breaks correlation).
2.  **Target Network**: Use a frozen copy of the network to calculate the target ($R + \gamma \max Q_{target}(s', a')$), updating it only every 1000 steps.
