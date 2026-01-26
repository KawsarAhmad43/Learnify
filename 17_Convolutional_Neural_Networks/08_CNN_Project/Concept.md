# CNN Project: The Full Pipeline

## 1. The Structure
A standard CNN classification pipeline includes:
*   **Backbone (Feature Extractor)**: Conv layers to understand the image (Conv -> ReLU -> Pool).
*   **Head (Classifier)**: Dense layers to make a decision (Flatten -> Dense -> ReLU -> Dense).

## 2. Flattening
To connect the 3D Feature Maps (e.g., 7x7x64) to the 1D Dense Neurons, we must **Flatten**.
*   $7 \times 7 \times 64 = 3136$ inputs.

## 3. Dropout
Inserted before Dense layers to prevent overfitting.
*   Randomly zeroes out neurons during training.

## 4. The Data Flow
Image $(28, 28, 1) \to$ Conv2D $(26, 26, 32) \to$ MaxPool $(13, 13, 32) \to$ Flatten $(5408) \to$ Dense $(128) \to$ Output $(10)$.
