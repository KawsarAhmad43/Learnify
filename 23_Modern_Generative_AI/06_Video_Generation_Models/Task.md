# Task: Memory Requirements

## Objective
Calculate VRAM usage for Video.

## Static Image
*   $512 \times 512 \times 4$ Latent $\approx 1$ MB per item in batch.

## Video
*   Duration: 4 seconds.
*   FPS: 24.
*   Total Frames: $4 \times 24 = 96$ frames.

## Task
1.  Calculate Memory Multiplier: 96x.
2.  If SD needs 8GB VRAM for 1 image batch, Video SD needs $8 \times 96 = 768$ GB.
3.  **Problem**: GPUs don't have 768 GB VRAM.

## Question
How do we solve this?
*   Answer: **Temporal Slicing** (Process 1 frame at a time in the Spatial Layers) or **Latent Compression** (Compress 4 frames into 1 latent frame using a 3D VAE).
