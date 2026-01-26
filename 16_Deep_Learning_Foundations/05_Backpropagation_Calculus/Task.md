# Task: Chain Rule Exercise

## Objective
Calculate gradients for a slightly more complex function.

## The Function
$$ f(x, y) = (x * y) + max(0, x) $$
Let $x = 3, y = -2$.

## Steps
1.  **Forward Pass**: Calculate the value of $f$.
    *   Hint: $max(0, 3)$ is the ReLU part.
2.  **Backward Pass**: Calculate $df/dx$.
    *   Note that x appears in *two* places.
    *   The gradient adds up from both branches (Multivariate Chain Rule).
    *   Branch 1: Derivative of $(x*y)$ wrt x = y.
    *   Branch 2: Derivative of $max(0, x)$ wrt x = 1 (since x>0).
    *   Total $df/dx = y + 1$.

## Task
1.  Verify the math above.
2.  What if $x = -3$? How does the derivative change?
3.  Write code to print the Forward and Backward values for both cases ($x=3$ and $x=-3$).
