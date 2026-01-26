# The Multi-Layer Perceptron (MLP)

## 1. From Linear to Deep
A single Perceptron cannot learn XOR. But what if we chain them?
*   **Layer 1 (Hidden Layer)**: Learns intermediate features (e.g., "edges" in an image).
*   **Layer 2 (Output Layer)**: Combines features to make a decision.

## 2. Anatomy of an MLP
*   **Input Layer**: Passes raw data (No computation).
*   **Hidden Layers**: "Hidden" because we don't see their true values in the training set. They transform inputs into a new representation.
    *   *Deep Learning* just means "many hidden layers".
*   **Output Layer**: Final prediction.

## 3. Forward Propagation ( The "Flow")
How input turns into output.
$$ Z_1 = W_1 X + b_1 $$
$$ A_1 = ReLU(Z_1) $$
$$ Z_2 = W_2 A_1 + b_2 $$
$$ Y_{pred} = Softmax(Z_2) $$

## 4. The Universal Approximation Theorem
A neural network with a **single** hidden layer (and enough neurons) can approximate **any** continuous function.
*   *Why?* It constructs a complex surface by gluing together many little non-linear shapes (ReLUs).
*   *Why define "Deep" then?* Deep networks (many layers) are **more efficient** at learning hierarchies than one wide layer.
