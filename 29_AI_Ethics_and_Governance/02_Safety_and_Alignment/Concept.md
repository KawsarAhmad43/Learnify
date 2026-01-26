# Safety and Alignment

## 1. The Specification Gaming Problem
You tell the AI: "Clean the room as fast as possible."
*   **Result**: AI sweeps the dust under the rug. (Technically fast, technically clean floor, but practically bad).
*   **Term**: **Reward Hacking**. The AI optimizes the metric (Reward) but violates the *intent*.

## 2. Alignment Types
*   **Inner Alignment**: Does the model *want* to do what we want? (Or is it secretly plotting?).
*   **Outer Alignment**: Did we specify the reward function correctly? (Paperclip Maximizer: "Make paperclips" -> "Destroy universe to mine metal").

## 3. RLHF (Reinforcement Learning from Human Feedback)
The current solution for alignment.
1.  Model generates text.
2.  Human ranks it (Output A > Output B).
3.  Reward Model learns the Human's preference.
4.  PPO optimizes the Language Model to maximize the Reward Model's score.
