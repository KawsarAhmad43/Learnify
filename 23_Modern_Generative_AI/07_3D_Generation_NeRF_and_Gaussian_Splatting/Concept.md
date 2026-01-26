# 3D Generation: NeRF and Splats

## 1. NeRF (Neural Radiance Fields)
An object is defined by a Neural Network $F(x, y, z)$.
*   Input: Coordinate $(x, y, z)$ and Viewing Direction $(\theta, \phi)$.
*   Output: Color $(r, g, b)$ and Density $(\sigma)$.
*   **Rendering**: Shoot a ray through the pixel. Sample 100 points along the ray. Query the NN. Sum the colors (Volumetric Rendering).
*   **Pros**: Photo-realistic.
*   **Cons**: Slow (Millions of queries per frame).

## 2. 3D Gaussian Splatting (3DGS)
Instead of a Neural Network, store the scene as a cloud of millions of "3D Ellipsoids" (Gaussians).
*   Each Gaussian has Position, Color, Opacity, Scaling, Rotation.
*   **Rendering**: Project (Splat) these ellipsoids onto the 2D screen. Sort them back-to-front. Alpha blend.
*   **Pros**: Real-time (60 FPS on standard GPUs). Fast training.

## 3. Generative 3D (LGM)
*   **Input**: Single image of a Chair.
*   **Model**: Predicts the position/color of 10,000 Gaussians that represent that chair.
*   **Result**: Rotate the chair in 3D instantly.
