# Video Generation

## 1. The Temporal Dimension
Video is just a stack of images ($T \times H \times W$).
Problem: If you generate $T$ frames independently, the "Cat" will change color in every frame (Flickering).
**Constraint**: Frame $t$ must resemble Frame $t-1$.

## 2. 3D Attention
Instead of standard Self-Attention (Spatial), we use **Spatio-Temporal Attention**.
*   **Spatial Attention**: Pixels in Frame 1 talk to other pixels in Frame 1.
*   **Temporal Attention**: Pixel $(x, y)$ in Frame 1 talks to Pixel $(x, y)$ in Frame 2, 3, 4...

## 3. Motion Modules (AnimateDiff)
*   Take a pre-trained Static Image Generator (Stable Diffusion).
*   Insert "Motion Adapter" layers.
*   Train ONLY the Motion Adapters on video clips.
*   Result: The model learns "How things move" while retaining SD's knowledge of "What things look like".
