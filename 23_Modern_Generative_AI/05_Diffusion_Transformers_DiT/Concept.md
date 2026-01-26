# Diffusion Transformers (DiT)

## 1. U-Net Limitations
The U-Net was designed for images. It uses Convolution layers ($O(N)$ efficiency).
But Transformers (Attention) scale better with massive data and compute laws.

## 2. DiT Architecture
1.  **Patchify**: Chop the latent image ($32 \times 32 \times 4$) into $2 \times 2$ patches.
2.  **Flatten**: Convert patches into a sequence of tokens ($16 \times 16 = 256$ tokens).
3.  **Transformer Blocks**: Standard GPT-like blocks (Self-Attention, MLP, LayerNorm).
4.  **Conditioning**: Time ($t$) and Class/Text ($y$) are injected via AdaLN (Adaptive Layer Norm).

## 3. Why DiT?
**Scalability**.
If you double the parameters of a U-Net, it gets slightly better.
If you double the parameters of a Transformer, it gets *predictably* much better (Scaling Laws).
Used by **Sora** (OpenAI) and **Stable Diffusion 3**.
