# Modern Architectures

## 1. The Vanishing Gradient Problem Returns
When VGG gets too deep (e.g., 20 layers), it stops learning.
*   Gradients get multiplied by small numbers over and over, effectively becoming zero.

## 2. ResNet (2015) - The Skip Connection
He et al. introduced the **Residual Block**.
*   **Idea**: Let the signal jump over the layers.
*   $Output = F(x) + x$
*   **Benefit**: The detailed information ($x$) is preserved. The layers $F(x)$ only need to learn the "Residual" (the difference/correction).
*   Result: Can train 1000+ layers.

## 3. Inception (GoogLeNet)
*   **Idea**: Why choose between 3x3 or 5x5? Use both!
*   **Inception Module**: Run 1x1, 3x3, and 5x5 filters in parallel and concatenate them.
*   **1x1 Convolution**: Used to squash channels (dimensionality reduction) before expensive 5x5 operations.

## 4. MobileNet & EfficientNet
*   **Depthwise Separable Convolution**: Splitting the conv operation to be faster on phones.
*   **EfficientNet**: Scaling Width, Depth, and Resolution simultaneously.
