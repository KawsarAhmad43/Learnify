# Task: Softening Distributions

## Objective
Visualize the effect of Temperature ($T$).

## Setup
*   Logits: $[2.0, 4.0]$.

## Task
1.  Calculate Softmax with $T=1$ (Standard).
2.  Calculate Softmax with $T=4$ (Soft).
3.  Observe how the gap shrinks.

## Formula
$p_i = \frac{e^{z_i/T}}{\sum e^{z_j/T}}$

## Question
Why does high temperature help? (It stops the largest class from dominating the gradient. If probability is 0.999, the gradient is ~0. If it becomes 0.6, there is a strong gradient signal).
