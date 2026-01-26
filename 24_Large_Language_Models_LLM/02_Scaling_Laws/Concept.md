# Scaling Laws

## 1. The Power Law
Performance (Test Loss) improves predictably as you increase compute ($C$), parameters ($N$), and data ($D$).
$L(N) \propto N^{-\alpha}$
It is not linear. It is a power law.

## 2. Kaplan vs Chinchilla
*   **Kaplan (2020)**: "Big models are king. Don't worry about data." (Led to GPT-3 being huge but undertrained).
*   **Chinchilla (DeepMind 2022)**: "Data matters more. For every 1 parameter, you should train on 20 tokens."
    *   **Optimal Ratio**: $D \approx 20N$.
    *   Example: Llama 7B should be trained on $7B \times 20 = 140B$ tokens.
    *   (Reality: Llama 3 was trained on 15 Trillion tokens. Far beyond Chinchilla optimal, because for *inference* cost purposes, we prefer smaller models trained longer).

## 3. Emergent Abilities
Small models can't do arithmetic.
Medium models can do addition.
Large models suddenly learn multiplication.
Some skills appear abruptly at certain scale thresholds.
