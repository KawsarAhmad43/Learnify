# Task: Implement Momentum

## Objective
Standard Gradient Descent can get stuck in "flat" spots. Momentum allows it to power through.

## The Formula
Instead of $x = x - lr * grad$, we introduce velocity $v$.
1.  $v = \beta \cdot v - lr \cdot grad$
2.  $x = x + v$
(Where $\beta$ is friction, usually 0.9. $v$ starts at 0).

## Task
1.  Modify the `gradient_descent` function to accept a `momentum` parameter ($\beta$).
2.  Test it on a "plateau" function: $f(x) = x^4 - 2x^2$ (looks like a W).
    *   This function has local minima.
3.  Start at $x=0$ (which is a local maximum/flat spot). 
    *   Standard GD will stuck if gradient is 0.
    *   Momentum might push it off? Or start at $x=0.1$ and see if Momentum gets to the global minimum faster.

## Expected Result
Momentum should result in larger steps initially and might overshoot slightly, but settles faster or escapes shallow traps.
