# Strides and Padding

## 1. The Shrinking Problem
When you convolve a 3x3 filter over a 5x5 image, the output is only 3x3.
*   **Why?** You can't center the kernel on the corner pixels (unless you go off the edge).
*   **Consequence**: If you have a deep network, your image shrinks to 1x1 very fast.

## 2. Padding (The Solution)
Add fake pixels (usually 0s) around the border.
*   **Valid Padding**: No padding. Output shrinks.
*   **Same Padding**: Pad enough so Output Size == Input Size.

## 3. Stride (The Skip)
Instead of sliding 1 pixel at a time, slide $S$ pixels.
*   **Stride 1**: Normal convolution.
*   **Stride 2**: Skip every other pixel. Output size is halved.
    *   This is an alternative to Pooling for dimensionality reduction.

## 4. The Formula
$$ Out = \frac{Input - Kernel + 2(Padding)}{Stride} + 1 $$
*   Memorize this! It's crucial for designing architectures.
