# GANs (Generative Adversarial Networks)

## 1. The Adversarial Game
*   **Generator (G)**: The Counterfeiter. Tries to create fake money from random paper ($z$).
*   **Discriminator (D)**: The Police. Tries to distinguish Real Money ($x$) from Fake Money ($G(z)$).

## 2. Nash Equilibrium
*   Step 1: G makes bad fakes. D catches them easily (Accuracy 100%).
*   Step 2: G learns *why* it got caught. It improves.
*   Step 3: D has to look harder. It improves.
*   **Goal**: Optimal state where G is perfect ($P_{fake} = P_{real}$) and D is confused (Accuracy 50%, random guessing).

## 3. Problems
*   **Mode Collapse**: G finds ONE image that fools D (e.g., a perfect number "1") and produces *only* that image forever.
*   **Vanishing Gradients**: If D is too good too early, G gets no gradient signal (Loss is 0) and stops learning.
