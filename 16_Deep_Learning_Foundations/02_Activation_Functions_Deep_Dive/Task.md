# Task: The "Dead Neuron" Problem

## Objective
Visualize the difference between ReLU, Leaky ReLU, and ELU (Exponential Linear Unit).

## Tasks
1.  **Define ELU**: Implement the ELU function.
    $$ f(x) = x \text{ if } x > 0 \text{ else } \alpha(e^x - 1) $$
    (Assume alpha = 1.0)
2.  **Generate Data**: Create an array `x` from -5 to 5.
3.  **Plot**:
    *   Plot ReLU in blue.
    *   Plot Leaky ReLU (alpha=0.1) in green.
    *   Plot ELU in red.
4.  **Analysis**: Zoom in or look closely at the negative side (x < 0). Why is ELU sometimes preferred over Leaky ReLU? (Hint: Smoothness/Differentiability at 0).
