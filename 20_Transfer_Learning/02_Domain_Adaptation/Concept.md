# Domain Adaptation

## 1. The Problem: Covariate Shift
The model was trained on $P(X_{source})$, but the target data looks like $P(X_{target})$.
*   **Source**: Photos of products from Amazon (White background, perfect lighting).
*   **Target**: Photos of products from user phone cameras (Blurry, Cluttered, Dark).
*   **Labels**: The labels ($Y$) are the same (e.g., "Backpack", "Laptop"), but the inputs ($X$) are shifted.

## 2. Unsupervised Domain Adaptation (UDA)
We have labels for Source, but **no labels** for Target.
*   We want the model to learn features that are "invariant" to the domain.
*   A "Laptop" should look like a "Laptop" whether it's on a white background or a messy desk.

## 3. Techniques
*   **MMD (Maximum Mean Discrepancy)**: Minimize distance between Source and Target feature means.
*   **DANN (Domain Adversarial Neural Networks)**: A "Discriminator" tries to guess the domain. The Feature Extractor tries to fool it. (GAN-like logic).
