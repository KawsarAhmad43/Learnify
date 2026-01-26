# Self-Supervised Learning (SSL)

## 1. The Bottleneck of Labels
*   **Supervised Learning**: Needs (Image, Label) pairs. Humans are slow/expensive annotators.
*   **Self-Supervised Learning**: Uses the data itself to generate labels.
*   **Idea**: "If I rotate this picture of a Cat, it's still a Cat. If I look at a picture of a Dog, it should be different from the Cat."

## 2. Contrastive Learning (SimCLR)
1.  Take an image $X$.
2.  Create two augmented versions: $X_i$ (Cropped) and $X_j$ (Color Jittered).
3.  These are a **Positive Pair**. Their embeddings should be close.
4.  Take a different image $Y$.
5.  $X$ and $Y$ are a **Negative Pair**. Their embeddings should be far apart.

## 3. Masked Image Modeling (MAE)
1.  Take an image.
2.  Delete 75% of the pixels (patches).
3.  Ask the model to reconstruct the missing pixels.
4.  To do this, the model MUST understand shapes, textures, and objects. ("I see a tail, so the missing part must be a body").
