# Generative vs Discriminative Models

## 1. The Fundamental Difference
*   **Discriminative ($P(Y|X)$)**: Draw a line separating Cats from Dogs. It doesn't care what a Cat *is*, only what makes it *not* a Dog.
*   **Generative ($P(X)$ or $P(X, Y)$)**: Learn to draw a Cat from scratch. You must understand ears, whiskers, and fur.

## 2. Analogy
*   **Discriminative**: An Art Critic. Can tell a Van Gogh from a Picasso, but can't paint either.
*   **Generative**: An Artist (Forger). Can paint a new "Van Gogh" that never existed before.

## 3. Why Generative is Harder
To classify an image, you can ignore 90% of the pixels (background).
To generate an image, you must fill in 100% of the pixels perfectly. One artifact ruins the illusion.

## 4. Types of Generating
*   **Explicit Density**: Predicting the exact probability of every pixel (e.g., PixelCNN).
*   **Implicit Density**: Learning to map random noise to an image (e.g., GANs).
