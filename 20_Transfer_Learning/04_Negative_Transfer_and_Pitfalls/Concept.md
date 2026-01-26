# Negative Transfer

## 1. When Helping Hurts
Transfer Learning usually helps. But sometimes, using a Source model makes performance **worse** than random initialization.
*   **Case**: Training on ImageNet (Natural Photos) -> Inferring on X-Rays (Grayscale, Transparency).
*   **Reason**: The features learned (color textures, dog ears) are actively misleading for detecting bone fractures.

## 2. Pitfalls
1.  **Domain Gap**: Source and Target represent fundamentally different physics.
2.  **Task Mismatch**: Source was trained for "Diversity" (1000 classes), Target needs "Granularity" (Cancer vs Non-Cancer).
3.  **Over-specialization**: Strategies like Batch Norm statistics frozen from Source might ruin Target data distribution.

## 3. Mitigation
*   **Train from Scratch**: If you have >100k data points, scratch might beat ImageNet.
*   **Intermediate Pre-training**: ImageNet -> [Chest X-Ray 100k] -> [Your Specific Lung Disease Dataset].
