# Transfer Learning Foundations

## 1. The Core Idea
"Stand on the shoulders of giants."
Instead of training a neural network from scratch (Random weights -> Converged), we start with a network that has already learned to see (Pre-trained on ImageNet).

## 2. Definitions
*   **Source Domain ($D_S$)**: Where we learned (e.g., ImageNet, Wikipedia). High data availability.
*   **Target Domain ($D_T$)**: Where we want to apply knowledge (e.g., Medical X-rays, Legal Documents). Low data availability.
*   **Task**: The specific goal (Classification, Regression).

## 3. Why it works
Deep Neural Networks learn hierarchical features:
*   **Layer 1-3**: Edges, Circles, Corners (Universal to all vision).
*   **Layer 4-20**: Textures, Patterns (General).
*   **Layer 50+**: Object parts (Specific to Source).

If $D_S$ and $D_T$ share low-level physics (both are natural images), we can re-use the lower layers.

## 4. Types
*   **Inductive TL**: Labeled data in Target. (Most common).
*   **Transductive TL**: No labeled data in Target, but we have the Source labels.
*   **Unsupervised TL**: No labels anywhere (Self-Supervised).
