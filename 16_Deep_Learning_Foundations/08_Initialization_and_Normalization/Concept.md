# Initialization & Normalization

## 1. The Initialization Problem
If we start with $Weights = 0$:
*   All neurons in a hidden layer calculate the **same** output.
*   They behave like 1 single neuron.
*   This is called "Symmetry", and we must break it with random numbers.

### Bad Initialization
*   **Too Small**: Signal dies out (Vanishing Gradient).
*   **Too Large**: Signal explodes (Exploding Gradient).

### The Solution: Xavier & He
Mathematical recipes to pick the "Just Right" random numbers based on the number of inputs.
*   **Xavier (Glorot)**: For Sigmoid/Tanh.
*   **He Initialization**: For ReLU.

## 2. Normalization (Data Hygiene)
Neural networks like inputs to be centered around 0 with manageable variance (e.g., -1 to 1).

### Batch Normalization (The Fixer)
A layer that re-centers the data *inside* the network.
*   $x' = \frac{x - mean}{std}$
*   It makes the network robust to bad initialization and allows higher learning rates.
*   Added *after* the linear step ($Wx+b$) but *before* the activation function (usually).
