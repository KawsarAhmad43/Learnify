# Stable Diffusion Architecture

## 1. Latent Diffusion Models (LDM)
Standard Diffusion works on Pixels ($512 \times 512 \times 3$). This is slow.
**LDM Trick**: Use a VAE to compress pixels to Latent Space ($64 \times 64 \times 4$).
*   Diffusion happens in this small latent space (Faster!).
*   VAE Decoder converts the final latent back to $512 \times 512$.

## 2. The U-Net Backbone
The core engine that predicts noise.
*   **ResNet Blocks**: Process the visual data.
*   **Self-Attention**: Helps pixels talk to each other (Global context).
*   **Cross-Attention**: Injects the Text Prompt.

## 3. Conditioning (CLIP)
How does it know what a "Cat" is?
1.  **Tokenizer**: "Photo of a cat" -> [492, 1120, 330].
2.  **CLIP Text Encoder**: Converts tokens to Embeddings ($77 \times 768$).
3.  **Injection**: The U-Net Cross-Attention layers query these embeddings.
    *   Visual Features = Query (Q).
    *   Text Embeddings = Key (K), Value (V).
    *   $Attention(Q, K, V)$.
