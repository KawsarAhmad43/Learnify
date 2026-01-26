# Task: Image Bloat

## Objective
Efficiency.

## Setup
*   Base Image: `ubuntu:latest` (80MB).
*   Install PyTorch: +2GB.
*   Your Code: 5KB.
*   Total Size: ~2GB.

## Task
1.  Every time you deploy, you upload 2GB.
2.  If you have 100 nodes pulling this image, that's network congestion.
3.  **Optimization**: 
    *   Use `python:3.9-slim` (Smaller base).
    *   Use Multi-Stage Builds (Compile C++ deps in one stage, copy only binaries to final stage).
    *   Use CPU-only versions of PyTorch if inference is on CPU (`pip install torch --extra-index-url https://download.pytorch.org/whl/cpu`). Reduces size by 70%.

## Question
What is 'Layer Caching'?
*   Answer: Docker caches each line of the Dockerfile. If you change your code (last line), Docker reuses the cached \"Install PyTorch\" layer (middle line). This makes rebuilds fast.
