# Task: Kernel Alignment

## Objective
Train the kernel.

## Setup
*   A fixed Quantum Feature Map (e.g., Angle Encoding) might not be good for your dataset.
*   **Trainable Kernels**: We can add parameters $\theta$ to the feature map $U(x, \theta)$.
*   We optimize $\theta$ to maximize the distance between classes in the Hilbert space.

## Task
1.  **Metric**: Kernel Alignment. It measures how well the Kernel Matrix $K$ matches the Ideal Target Matrix $y y^T$ (where 1 if same class, -1 if diff class).
2.  **Task**: Use `qml.kernels.target_alignment` to optimize the parameters of your feature map before training the SVM.

## Question
What is 'HHL Algorithm'?
*   Answer: Harrow-Hassidim-Lloyd. An algorithm to solve Linear Systems of Equations ($Ax = b$) exponentially faster than classical computers. It is the theoretical backbone of many QML proposals, but requires deep fault-tolerant circuits (not feasible on NISQ).
