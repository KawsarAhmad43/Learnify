# Quantum Neural Networks (QNN)

## 1. Parameterized Quantum Circuits (PQC)
*   A QNN is not typically a translation of a classical Neuron (Sum -> Activation).
*   It is a **Circuit** with gates that have trainable parameters (e.g., $R_x(\theta)$).
*   **Input**: Data $x$ (Encoded into state).
*   **Weights**: Gate angles $\theta$ (Variational).
*   **Output**: Measurement Expectation Value.

## 2. Hybrid Training
*   **Forward**: CPU sends data to QPU. QPU runs circuit, returns measurement.
*   **Backward**: CPU asks QPU for gradients (using Parameter Shift Rule). CPU updates $\theta$ using Adam/SGD.
*   **Integration**: This fits perfectly into PyTorch (`torch.nn.Module`). The QPU is just another "Layer" (like a Conv2D layer) but running on a different chip.

## 3. Expressibility vs Trainability
*   **Expressibility**: A QNN can represent functions that are hard for classical NNs to represent (e.g., discrete logarithm).
*   **Trainability**: But they are notorious for Barren Plateaus (Gradients vanishing to 0).
