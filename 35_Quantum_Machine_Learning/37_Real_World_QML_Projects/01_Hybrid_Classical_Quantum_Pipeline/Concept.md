# Hybrid Classical-Quantum Pipeline

## 1. Use the Right Tool for the Job
*   **Classical Computer**: Great at Data Loading, Matrix Multiplication (GPU), Optimization (Adam), and Non-linear activations (ReLU).
*   **Quantum Computer**: Great at Sampling from complex distributions, Interference, and High-dimensional feature mapping.
*   **Hybrid**: Combine them.

## 2. The Transfer Learning Pipeline
*   **Goal**: Classify Medical Images (high resolution).
*   **Step 1 (Classical)**: Use a pre-trained ResNet-50. Remove the last layer.
*   **Step 2 (Feature Extraction)**: Run the image through ResNet. Output: A 512-dimensional vector.
*   **Step 3 (Dimension Reduction)**: Use classical PCA to reduce 512 -> 4 dimensions (to fit on 4 qubits).
*   **Step 4 (Quantum)**: Feed the 4 values into a 4-Qubit Variational Circuit. Measure output.
*   **Step 5 (Result)**: "Cancer" vs "Benign".

## 3. Why?
*   The Quantum Circuit adds a "Quantum Kernal" non-linearity that might capture features ResNet missed.
*   It serves as a playground to test QML on real data without needing 1000 qubits.
