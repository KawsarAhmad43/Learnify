# Task: Compression Ratio

## Objective
Calculate bits per pixel.

## Problem
*   Input: $28 \\times 28$ grayscale (8-bit) image. Size $= 784$ bytes.
*   Latent: 32 floats (32-bit). Size $= 32 \\times 4 = 128$ bytes.

## Task
1.  Calculate Ratio: $784 / 128$.
2.  If we used a 2-bit quantization on the latent space, size becomes $32 \\times 0.25 = 8$ bytes.
3.  New Ratio: $784 / 8$.

## Question
Why is the reconstructed image blurry?
*   Answer: High frequency details (sharp edges) are expensive to store. The model throws them away to focus on the general shape, resulting in blur (L2 Loss prefers average blur over sharp wrongness).
