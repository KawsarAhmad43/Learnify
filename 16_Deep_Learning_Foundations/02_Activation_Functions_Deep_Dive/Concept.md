# Activation Functions Deep Dive

## 1. The "Why": Non-Linearity
Without activation functions, a Neural Network is just a big Linear Regression model.
$$ Layer1 = W_1 x + b_1 $$
$$ Layer2 = W_2 (Layer1) + b_2 = W_2 (W_1 x + b_1) + b_2 = (W_2 W_1) x + (W_2 b_1 + b_2) $$
No matter how many layers you stack, it collapses into a single linear equation W*x + b.
**Activation functions introduce non-linearity**, allowing the network to learn complex curves and boundaries.

## 2. Classic Functions (The "Old Guard")

### Sigmoid ($\sigma$)
*   **Range**: (0, 1)
*   **Pros**: Good for probability outputs.
*   **Cons**:
    *   **Vanishing Gradient**: Deep networks stop learning because gradients become near-zero at the tails.
    *   **Not Zero-Centered**: Outputs are always positive, making optimization zigzag.

### Tanh (Hyperbolic Tangent)
*   **Range**: (-1, 1)
*   **Pros**: Zero-centered (better than Sigmoid).
*   **Cons**: Still suffers from Vanishing Gradient.

## 3. Modern Functions (The "New Standard")

### ReLU (Rectified Linear Unit)
$$ f(x) = max(0, x) $$
*   **Range**: [0, inf)
*   **Pros**:
    *   **Computationally Efficient**: Just check if x > 0.
    *   **No Vanishing Gradient** (for positive x).
*   **Cons**:
    *   **Dead ReLU**: If x < 0, gradient is 0. The neuron dies and never learns again.

### Leaky ReLU
$$ f(x) = max(0.01x, x) $$
*   **Fix**: Allows a small gradient when x < 0 to keep the neuron alive.

## 4. Output Layer Functions
*   **Binary Classification**: Sigmoid (Prob of class 1).
*   **Multi-Class Classification**: Softmax (Prob distribution summing to 1).
*   **Regression**: Linear (No activation, or Identity).
