# Task: Sequence Length

## Objective
Calculate compute cost.

## Setup
*   Image: $256 \times 256$.
*   Patch Size: $2 \times 2$.
*   Attention Cost: $O(N^2)$.

## Task
1.  Calculate N (Number of Patches).
    *   $256 / 2 = 128$ patches per side.
    *   $128 \times 128 = 16,384$ tokens.
2.  Compute $N^2$.
    *   $16,384^2 \approx 268$ Million operations per layer.

## Question
If we increase image size to $512 \times 512$ (2x side len, 4x pixels), how does cost scale?
*   N becomes $4 \times 16,384$.
*   Cost becomes $(4N)^2 = 16N^2$.
*   **16x Cost** for 4x pixels.
*   This is why we need Latent Space (Compression) even for DiT.
