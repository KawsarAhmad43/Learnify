# The Convolution Operation

## 1. Why MLPs Fail on Images
*   **Too Many Weights**: A 1000x1000 image has 1M pixels. Fully connecting to just 1 neuron requires 1M weights.
*   **Loss of Topology**: Flattening an image into a 1D vector destroys the 2D relationships (a pixel is related to its neighbors).

## 2. The Filter (Kernel)
A **Filter** is a small grid of weights (e.g., 3x3).
*   It slides over the image (Convolution).
*   At each step, it performs a dot product (pixel * weight) and sums it up.
*   **Parameter Sharing**: The *same* filter is used for the entire image. This cuts parameters drastically.

## 3. What do Filters Learn?
*   **Low Level**: Edges, curves, blobs.
*   **High Level**: Eyes, wheels, text.
*   The "Feature Map" is the output grid showing *where* the filter found its pattern.

## 4. 2D Convolution Formula
$$ (I * K)(i, j) = \sum \sum I(i+m, j+n) K(m, n) $$
Where $I$ is Input, $K$ is Kernel.
