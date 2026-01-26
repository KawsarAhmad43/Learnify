# Task: Trace the Gradient

## Objective
Understand why ResNet learns.

## Scenario
*   Function: $y = x \cdot w + x$
*   Target: No target, just calculate derivative $dy/dx$.

## Derivative Rules
*   $\frac{d}{dx} (ax) = a$
*   $\frac{d}{dx} (x) = 1$

## Task
1.  Calculate derivative of $x \cdot w$ with respect to $x$. (Answer: w)
2.  Calculate derivative of $+ x$ with respect to $x$. (Answer: 1)
3.  Add them up.
4.  Total Gradient = $w + 1$.

## Question
If $w$ (weight) is very small (e.g., 0.0001), what is the gradient?
*   Without Skip: 0.0001 (Vanishing)
*   With Skip: 1.0001 (Healthy!)

Write a Python loop that multiplies a gradient by 0.01 ten times, versus multiplying by 1.01 ten times. Compare the result.
