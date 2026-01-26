# Long Context

## 1. The Bottleneck: Attention $O(N^2)$
Standard attention scales quadratically.
*   4k context: cheap.
*   100k context: $625 \times$ cost.
*   1M context: Impossible (VRAM OOM).

## 2. RoPE (Rotary Positional Embeddings)
Absolute Position Embeddings (adding a vector for position 0, 1, 2) fail at length extrapolation. If trained on 2048, pos 2049 is undefined.
**RoPE**:
*   Encodes position by **Rotating** the key/query vector in complex space.
*   $RelativeDist = Rotation(k) - Rotation(q)$.
*   Allows models to generalize to longer sequences than trained on ("Extrapolation").

## 3. Ring Attention
How do you train on 1 Million tokens?
Split the Sequence across 512 GPUs.
*   GPU 1 computes Attention for tokens 0-2000.
*   GPU 2 computes Autention for tokens 2001-4000.
*   Pass Key/Value blocks in a Ring (P2P communication).
*   Allows theoretically infinite context.
