# Task: Optimization Algorithms

## Objective
Implement Gradient Descent for a multivariable function.

## Tasks

### Task 1: 2D Gradient Descent
Find the minimum of the function:
$$f(x, y) = x^2 + y^2 + 10$$

1.  Calculate derivatives $\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial y}$ symbolically or manually.
2.  Write a Python function `gradient_descent_2d(start_x, start_y, lr, epochs)` that updates both x and y.
3.  Start at $(x=3, y=4)$. What is the final position after 50 epochs with $lr=0.1$?

### Task 2: Effect of Learning Rate
Using the same function from Task 1:
1.  Try a very large learning rate (e.g., $lr=1.1$). What happens?
2.  Try a very small learning rate (e.g., $lr=0.0001$). What happens?
