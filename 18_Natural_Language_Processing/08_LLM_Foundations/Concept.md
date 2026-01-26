# Large Language Models (LLMs)

## 1. Scaling Laws
It turns out, if you just make the Transformer BIGGER (more layers, more data), magic happens.
*   **Emergent Abilities**: Models start doing things they weren't explicitly trained for (like math or coding).

## 2. GPT (Generative Pre-trained Transformer)
*   **Next Token Prediction**: The only goal is "What word comes next?".
*   **Context Window**: Input limit (e.g., 4096 tokens).
*   **Temperature**: Randomness controls creativity.
    *   Temp 0: Deterministic (Fact-based).
    *   Temp 1: Creative (Story-telling).

## 3. RLHF (Reinforcement Learning from Human Feedback)
Raw GPT is like a super-smart parrot (it finishes sentences, even bad ones).
*   **InstructGPT / ChatGPT**: Humans rank outputs ("This answer is helpful", "This answer is toxic").
*   The model learns to align with human intent.

## 4. Prompt Engineering
The art of talking to the model.
*   **Zero-Shot**: "Translate this."
*   **Few-Shot**: "Here are 3 examples. Now do this one."
*   **Chain-of-Thought**: "Let's think step by step."
