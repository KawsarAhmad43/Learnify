# Modern RL (PPO)

## 1. Proximal Policy Optimization (PPO)
The current "King" of RL. Used by OpenAI to train ChatGPT (RLHF).
*   **Problem with Gradient Updates**: If you update the policy TOO much, you ruin it.
    *   Example: You find "Going Left" is good. You change the weights massively. Now the probability of "Left" is 100%. But wait, sometimes "Right" is necessary! You moved into a "Collapse" zone and can't explore anymore.

## 2. Clipped Objective
PPO limits how much the policy can change in a single step.
*   Ratio $r(\theta) = \frac{\pi_{new}}{\pi_{old}}$.
*   We want to maximize reward, BUT we clip this ratio to be between $[0.8, 1.2]$.
*   "Don't become more than 20% different from the old you."

## 3. Why it matters
Stability. Use defaults (Learning rate 3e-4, Clip 0.2) and it just works. No hyperparameter tuning hell like DQN.
