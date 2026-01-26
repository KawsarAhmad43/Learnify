# Task: Two-Headed Network

## Objective
Design the architecture of an Actor-Critic Network.

## Input
State Vector $s$ (Size 4).

## Output
1.  **Actor Head**: Action Probabilities (Size 2: Left/Right). Output activation?
2.  **Critic Head**: State Value (Size 1: Scalar). Output activation?

## Task
1.  Define layers.
    *   Shared Dense(64) -> Relu.
    *   Actor Branch: Dense(2) -> Softmax (Probabilities).
    *   Critic Branch: Dense(1) -> Linear (No activation, values can be anything).
2.  Write pseudocode or PyTorch/Keras code snippet.

## Question
Why share the first layer?
Answer: Features useful for deciding action (e.g., "enemy is close") are also useful for judging value ("I am in danger").
