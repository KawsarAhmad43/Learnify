# Instruction Tuning and RLHF

## 1. Pre-training vs Post-training
*   **Pre-training**: Predicting the next word on Wikipedia.
    *   Result: A model that knows facts but is socially awkward.
    *   Prompt: "What is the capital of France?" -> Model: "And what is the capital of Germany?" (It thinks it's completing a list of questions).
*   **Instruction Tuning (SFT)**: Fine-tuning on Q&A pairs.
    *   Result: A model that answers questions.
    *   Constraint: Writing ground truth answers is expensive (Expert Humans needed).

## 2. RLHF (Reinforcement Learning from Human Feedback)
Instead of forcing humans to Write answers, ask them to Rank answers.
*   Model generates Two answers (A and B).
*   Human says: "A is better than B".
*   **Reward Model**: Learn a classifier that predicts reward $r(x)$.
*   **PPO (Proximal Policy Optimization)**: Use RL to update the LLM to maximize $r(x)$.

## 3. DPO (Direct Preference Optimization)
RL is unstable and hard to tune.
**DPO** mathematically proves that you don't need a Reward Model or PPO loop.
You can optimize the preference likelihood directly using a simple Cross-Entropy-like loss.
*   State of the Art (used by Mistral, Llama 3).
