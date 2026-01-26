# Autoencoders

## 1. The Bottleneck
*   **Encoder**: $z = f(x)$. Compresses input (784 pixels) to a latent vector (32 floats).
*   **Decoder**: $x' = g(z)$. Tries to recreate the input from the compressed code.
*   **Loss**: $MSE(x, x')$.

## 2. Learning Latent Representation
Because the bottleneck is small (32 vs 784), the network CANNOT memorize the pixels.
It forces the network to learn efficient concepts:
*   "This is a digit 7."
*   "It is tilted 30 degrees."
*   "The stroke is thick."
If `z` contains this info, the decoder can redraw it.

## 3. Applications
1.  **Denoising**: Train on (Noisy Input, Clean Target). The bottleneck filters out random noise (because noise has no structure to compress).
2.  **Anomaly Detection**: If an input is weird (e.g., a photo of a Cat in a Digit dataset), the Autoencoder will fail to compress it properly. High reconstruction error = Anomaly.
