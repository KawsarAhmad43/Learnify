# Recurrent Neural Networks (RNNs)

## 1. The Memory Problem
Standard Neural Networks (FNN/CNN) have no memory.
*   Input: "Dog". Output: "Animal".
*   Input: "House". Output: "Building".
*   They don't know that "Dog" came before "House".

## 2. The Recurrent Solution
An RNN loops on itself.
*   **Hidden State ($h_t$)**: The "Memory" of the network at time $t$.
*   **Formula**: $h_t = \tanh(W \cdot x_t + U \cdot h_{t-1})$
    *   New Memory = Function(Current Input + Old Memory).

## 3. Unrolling
To train an RNN, we "unroll" it over time.
*   $t=0$: Compute $h_0$ from $x_0$.
*   $t=1$: Compute $h_1$ from $x_1$ and $h_0$.
*   ...
*   This looks like a very deep neural network, where each layer is a time step.

## 4. Problem: Vanishing Gradient
Because it's so deep (e.g., a sentence with 50 words = 50 layers), gradients vanish. RNNs forget early words.
