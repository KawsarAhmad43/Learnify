# Continual Learning

## 1. The Plasticity-Stability Dilemma
*   **Plasticity**: Ability to learn new tasks (Task B).
*   **Stability**: Ability to remember old tasks (Task A).
*   **Neural Networks**: Highly plastic (Gradient Descent overwrites weights), Low stability.
*   **Catastrophic Forgetting**: Train on A -> Weights Optimized for A. Train on B -> Weights Optimized for B (A is erased).

## 2. Strategies
1.  **Replay (Rehearsal)**: Keep a small buffer of data from Task A and mix it into the training batch for Task B.
2.  **Regularization (EWC)**: Identify which weights were "important" for Task A (high Fisher Information) and discourage changing them heavily while learning B.
3.  **Expansion**: Add new neurons for Task B, freeze weights for Task A. ('Progressive Neural Networks').

## 3. Real World Need
Robots interact with the world for years. They can't just define "The Dataset" once and never learn again.
