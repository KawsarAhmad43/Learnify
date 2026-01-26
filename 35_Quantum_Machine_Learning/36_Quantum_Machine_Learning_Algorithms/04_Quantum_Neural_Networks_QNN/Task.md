# Task: Quantum Convolution

## Objective
The Filter.

## Setup
*   Classical Conv2D: Slide a 3x3 filter over an image. Dot product.
*   Quantum Conv2D: Slide a small 4-qubit circuit over the image. Measure expectation.
*   **Quanvolutional Neural Network**: A classical CNN where the first layer is replaced by a Quantum Transformation (to extract "Quantum Features").

## Task
1.  **Input**: MNIST Image (28x28). Downscale to 14x14.
2.  **Filter**: 2x2 window -> 4 values -> Encode into 4 Qubits.
3.  **Circuit**: Apply random gates. Measure Pauli Z on Qubit 0.
4.  **Output**: A new 14x14 feature map.
5.  **Task**: Feed this feature map into a Classical Forest to classify digits.

## Question
What is 'Overfitting' in QML?
*   Answer: Same as classical. If your Quantum Circuit has too many parameters (gates) relative to the data, it will memorize noise. QNNs need regularization too.
