# Task: The Log Trick

## Objective
Understand the math term $\nabla \log \pi(a|s)$.

## Calculus
Why do we use log probabilities?
*   Derivative: $\frac{d}{dx} \log(f(x)) = \frac{f'(x)}{f(x)}$
*   The "Score Function".

## Task
1.  Assume probability $p = 0.2$.
2.  Compute $\log(p)$.
3.  Compute $\log(p + 0.01)$.
4.  Notice the change.

## Question
Why don't we just maximize $p$ directly? Why $\log(p)$?
*   Answer: Numerical stability (probabilities get tiny, logs keep them manageable) and cleaner math for gradients.
*   Also, multiplying probabilities = adding logs.

Write a script to show that $\log(a \times b) = \log(a) + \log(b)$.
