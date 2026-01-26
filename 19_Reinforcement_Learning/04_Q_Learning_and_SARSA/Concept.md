# Q-Learning and SARSA

## 1. Temporal Difference (TD) Learning
Monte Carlo is slow (must wait for episode end).
TD updates **every step**.
*   "I walked right. I got rewards, and I ended up in a new State that *looks* good (high value). So my previous action must have been good."
*   Bootstrapping: Guessing based on a guess.

## 2. Q-Learning (Off-Policy)
Learn the optimal policy while behaving randomly.
*   $Q(s, a) \leftarrow Q(s, a) + \alpha [ R + \gamma \max_{a'} Q(s', a') - Q(s, a) ]$
*   "Assume I will play perfectly next turn ($max_{a'}$)."

## 3. SARSA (On-Policy)
Learn the policy you are actually following.
*   $Q(s, a) \leftarrow Q(s, a) + \alpha [ R + \gamma Q(s', a') - Q(s, a) ]$
*   "I actually played $a'$ next turn (maybe I explored randomly), so I should use that real value."

## 4. Exploration vs Exploitation
*   **Epsilon-Greedy**:
    *   90% of time: Pick Best Action (Exploit).
    *   10% of time: Pick Random Action (Explore).
