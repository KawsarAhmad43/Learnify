# The Transfer Learning Pipeline

## 1. The Decision Chart
1.  **Is Target Data like Source Data?**
    *   Yes: Freeze backbone, train Head (Feature Extraction).
    *   No: Fine-tune backbone or Train from scratch.
2.  **Is Target Data Size Large?**
    *   Yes: Fine-tune entire model.
    *   No: Freeze backbone (Avoid overfitting).
3.  **Is Source Task similar to Target Task?**
    *   Yes: Standard TL.
    *   No: Watch out for Negative Transfer.

## 2. Discriminative Layer Learning Rates
Not all layers should learn at the same speed.
*   **Lower Layers** (Edges/Lines): Universal. Do not touch (LR = 0).
*   **Middle Layers** (Features): General. Touch gently (LR = 1e-5).
*   **Top Layers** (Objects): Specific to ImageNet. Change heavily (LR = 1e-3).
*   **New Head**: Randomly initialized. Needs fast training (LR = 1e-2).
