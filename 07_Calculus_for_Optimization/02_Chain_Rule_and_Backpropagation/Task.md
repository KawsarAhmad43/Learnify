# Task: Chain Rule & Backpropagation

## Objective
Perform Backpropagation manually on a computational graph.

## Tasks

### Task 1: Manual Backprop
Consider the expression:
$$f(x, y) = \frac{x + y}{x}$$
(Note: This can be rewritten as $f = (x + y) * (1/x)$)

Inputs:
*   x = 2
*   y = 4

1.  Draw the computational graph (on paper or mentally).
2.  Compute the forward pass to get $f$.
3.  Compute gradients $\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial y}$ manually using the Chain Rule.
4.  Write a Python script to verify your results (you can use PyTorch or just simple variables).
