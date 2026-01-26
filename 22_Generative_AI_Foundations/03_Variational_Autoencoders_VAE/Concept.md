# Variational Autoencoders (VAE)

## 1. The Problem with Standard AE
In a normal AE, the latent space is a mess.
*   Input 1 -> [-10.5, 3.2]
*   Input 2 -> [5.5, 0.1]
*   What happens if we decode [0, 0]? We get garbage, because the model never learned that region.
*   **Consequence**: You cannot "generate" new data by picking random points.

## 2. The Variational Solution
Force the latent space to be a smooth, continuous Gaussian Unit Sphere ($N(0, 1)$).
*   Input 1 -> Mean -10, Variance 0.1. (The point is a cloud).
*   **Loss Function**:
    1.  **Reconstruction**: Make the output look like the input.
    2.  **KL Divergence**: Force the distribution $q(z|x)$ to match $N(0, 1)$.

## 3. Reparameterization Trick
Backpropagation cannot flow through a random node (`z = random.normal(mu, sigma)`).
**Trick**:
*   Generate epsilon $\epsilon \sim N(0, 1)$ (Random constant).
*   $z = \mu + \sigma \cdot \epsilon$.
*   Now we can differentiate with respect to $\mu$ and $\sigma$.
