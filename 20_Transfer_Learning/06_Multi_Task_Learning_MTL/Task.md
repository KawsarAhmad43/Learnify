# Task: Combined Gradients

## Objective
Calculate gradient manually for a shared weight.

## Setup
*   $y = w \cdot x$
*   Task 1 Loss: $L_1 = (y - 1)^2$
*   Task 2 Loss: $L_2 = (y - 2)^2$
*   $x=1, w=0, y=0$.

## Task
1.  Calculate $\frac{\partial L_1}{\partial w}$.
    *   $L_1 = (0-1)^2 = 1$. Gradient = $2(y-1)x = 2(-1)(1) = -2$.
2.  Calculate $\frac{\partial L_2}{\partial w}$.
    *   $L_2 = (0-2)^2 = 4$. Gradient = $2(y-2)x = 2(-2)(1) = -4$.
3.  Combine.
    *   Gradient Total = $-2 + (-4) = -6$.
4.  Update $w$: $w = w - \alpha (-6) = 0 + 0.1(6) = 0.6$.

## Question
Does moving $w$ to 0.6 help both tasks?
*   Task 1 Target is 1. 0.6 is closer to 1 than 0. (Yes)
*   Task 2 Target is 2. 0.6 is closer to 2 than 0. (Yes)
*   MTL Success!
