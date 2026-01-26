# Multi-Task Learning (MTL)

## 1. Why learn one thing?
Humans learn to see edges once, and use that skill for reading, driving, and recognizing faces.
MTL forces a model to learn a **General Representation** that is useful for multiple distinct tasks.
*   **Input**: Image.
*   **Output 1**: Is it a Cat? (Classification).
*   **Output 2**: Where is the Cat? (Bounding Box Regression).

## 2. Architecture
*   **Hard Parameter Sharing**: Shared Backbone (ResNet) -> Split Heads. Most common.
*   **Soft Parameter Sharing**: Two separate models, but we force their weights to be similar ($L2$ distance penalty).

## 3. The Loss Balancing Act
$L_{total} = w_1 L_1 + w_2 L_2$.
*   If Task A is easy (Loss 0.1) and Task B is hard (Loss 100), the model will ignore A and focus only on B.
*   **Uncertainty Weighting**: Let the model learn $w_1$ and $w_2$ automatically ($\sigma$).
