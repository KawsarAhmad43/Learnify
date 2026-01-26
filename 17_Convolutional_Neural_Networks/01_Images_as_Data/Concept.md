# Images as Data

## 1. What is an Image?
To a computer, an image is just a grid of numbers.
*   **Pixel**: The smallest unit of an image.
*   **Intensity**: The value of a pixel (0 = Black, 255 = White).

## 2. Channels (The 3rd Dimension)
*   **Grayscale**: 2D Grid (Height x Width). Shape: $(H, W)$.
*   **Color (RGB)**: 3D Grid. Shape: $(H, W, 3)$.
    *   3 Channels: Red, Green, Blue.
    *   Each channel is a separate 2D grid overlayed on top of each other.

## 3. Tensors and Shapes
In Deep Learning (PyTorch/TensorFlow), easy data is usually ordered as:
*   **NCHW**: (Batch Size, Channels, Height, Width) - PyTorch default.
*   **NHWC**: (Batch Size, Height, Width, Channels) - TensorFlow default.

## 4. Normalization
Neural networks hate large numbers like 255.
*   **Scaling**: Divide by 255 to get range [0, 1].
*   **Standardization**: Subtract mean, divide by std to get range [-1, 1].
