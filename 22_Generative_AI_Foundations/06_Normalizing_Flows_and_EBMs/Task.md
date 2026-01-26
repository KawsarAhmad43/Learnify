# Task: Energy Calculation

## Objective
The Physics Connection.

## Concept
Data tries to minimize its energy (roll down a hill).
$P(x) \propto e^{-E(x)}$.

## Task
1.  Assume a data point $x$ sits at the bottom of a well ($E(x) = 0$).
    *   $P(x) = e^{-0} = 1$. High probability.
2.  Assume a data point $y$ sits on a hill ($E(y) = 10$).
    *   $P(y) = e^{-10} = 0.000045$. Low probability.

## Question
In Langevin Dynamics training, we update $x$ by $x_{new} = x - \nabla_x E(x)$. What is this equivalent to?
*   Answer: Gradient Descent on the Energy landscape. It pushes the noise down into the data manifold.
