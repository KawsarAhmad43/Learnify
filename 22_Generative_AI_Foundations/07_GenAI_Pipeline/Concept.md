# The Generative Pipeline

## 1. Generation is Rarely One-Shot
Expecting a model to output the perfect result in one go is naive.
**Best Practice**: Rejection Sampling (Best-of-N).
1.  Generate 100 images.
2.  Use a Discriminator (Reward Model) to score them.
3.  Pick the top 1.

## 2. Iterative Refinement
Instead of generating pixels directly, generate a "Sketch" then refine it.
*   **Coarse-to-Fine**: Generate 64x64 image -> Upscale to 256x256 -> Upscale to 1024x1024.
*   Similar to how human artists work.

## 3. Human in the Loop (RLHF)
Generative models drift towards "easy" outputs (Mode Collapse).
Humans provide feedback ("This hand has 6 fingers").
We train a Reward Model to predict human preference, then force the Generator to maximize that reward (PPO).
