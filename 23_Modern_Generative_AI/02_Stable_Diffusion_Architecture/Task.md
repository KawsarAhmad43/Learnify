# Task: Dimensionality Reduction

## Objective
Calculate why Latent Diffusion is fast.

## Pixel Space
*   $512 \times 512 \times 3$ (RGB) = $786,432$ values.

## Latent Space (SD Standard)
*   Downsampling factor 8.
*   $64 \times 64 \times 4$ (Channels) = $16,384$ values.

## Task
1.  Calculate Ratio: $786,432 / 16,384$.
2.  Result: 48x reduction in data size.

## Question
Why does the model generate 4 channels instead of 3?
*   Answer: The VAE latent space doesn't map directly to RGB. It learns a dense representation where 4 channels capture structure, texture, and color more efficiently than RGB.
