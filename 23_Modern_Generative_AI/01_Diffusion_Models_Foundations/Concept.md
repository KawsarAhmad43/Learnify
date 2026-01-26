# Diffusion Models

## 1. The Physics of Destruction (Forward Process)
Imagine dropping a drop of ink into water. It slowly diffuses until the water is uniformly light blue (pure noise).
*   $q(x_t | x_{t-1})$: Add a tiny bit of Gaussian noise at each step.
*   After $T=1000$ steps, the image $x_0$ becomes isotropic Gaussian noise $x_T$.

## 2. The Art of Restoration (Reverse Process)
If we could reverse time, we could turn the blue water back into the ink drop.
*   $p_\theta(x_{t-1} | x_t)$: Predict the noise $\epsilon$ that was added, and subtract it.
*   **Model**: A U-Net that takes $(NoisyImage, TimeStep)$ and outputs $(PredictNoise)$.

## 3. Training Objective
We don't need to generate images during training.
1.  Take a real image $x_0$.
2.  Sample a random timestep $t$.
3.  Add noise $\epsilon$ to get $x_t$.
4.  Ask the model: "What noise did I add?"
5.  Loss = MSE(PredictedNoise, RealNoise).

## 4. Sampling (DDPM)
start with random noise $x_T$.
Loop $t$ from $T$ down to 0:
    $x_{t-1} = \frac{1}{\sqrt{\alpha_t}} (x_t - \frac{1-\alpha_t}{\sqrt{1-\bar{\alpha}_t}} \epsilon_\theta(x_t, t)) + \sigma_t z$
    (Subtract predicted noise, add a tiny bit of random noise for stability).
