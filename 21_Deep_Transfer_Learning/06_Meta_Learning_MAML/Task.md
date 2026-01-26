# Task: Gradient of Gradient

## Objective
Visualize the complexity.

## Concept
If $y = x^3$.
*   First derivative $y' = 3x^2$.
*   Second derivative $y'' = 6x$.
*   MAML needs to know $y''$ to optimize the learning process itself.

## Task
1.  Assume Loss function $L(\theta) = \theta^4$.
2.  Inner loop update: $\theta_{new} = \theta - \alpha (4\theta^3)$.
3.  Outer loop needs derivative of $\theta_{new}$.
    *   This involves differentiating $4\theta^3$, which is $12\theta^2$.

## Question
Why does MAML require double memory? (Because you have to store the computation graph of the inner loop to backpropagate through it).

Write a script using PyTorch `autograd.grad(create_graph=True)`.
