# Policy Gradient Methods

## 1. Value Based vs Policy Based
*   **Value Based (DQN)**: Learn $Q(s, a)$. Then pick $a = \text{argmax}(Q)$. Indirect.
*   **Policy Based (REINFORCE)**: Learn $\pi(a|s)$ directly. The output is a probability vector.

## 2. Why Policy Gradient?
*   **Stochastic Policy**: Can learn to act randomly (useful in Rock-Paper-Scissors).
*   **Continuous Actions**: Robots don't just "Go Left". They "Rotate Joint 1 by 34.5 degrees". DQN can't handle infinite actions comfortably.

## 3. The Algorithm (REINFORCE)
1.  Play an entire episode using the current policy (Neural Net).
2.  If the episode was **Good** (High Return $G_t$): Increase the probability of ALL actions taken.
3.  If the episode was **Bad**: Decrease the probability.
4.  $\theta \leftarrow \theta + \alpha G_t \nabla \log \pi(a_t|s_t)$
