# Task: Counting Parameters

## Objective
Visualize the memory savings of Freezing.

## Model
*   Layer 1: 100 params.
*   Layer 2: 200 params.
*   Head: 50 params.

## Task
1.  Case A: Train Everything. Total size = 350.
2.  Case B: Freeze Layer 1 & 2. Total Trainable size = 50.
3.  Case C: Unfreeze Layer 2. Total Trainable size = 250.

## Question
Why is Case B faster?
*   Forward pass is same speed.
*   Backward pass stops at the Head (no gradients computed for L1/L2).

Write a script to sum lists based on boolean flags.
