# Task: Epsilon Decay

## Objective
Balance Exploration and Exploitation over time.

## Concept
*   Start: $\epsilon = 1.0$ (Total Chaos/Exploration).
*   End: $\epsilon = 0.01$ (Total mastery).
*   Decay: $\epsilon = \epsilon \times \text{decay\_rate}$ every episode.

## Task
1.  Start $\epsilon = 1.0$.
2.  Decay rate = $0.995$.
3.  Minimum $\epsilon = 0.01$.
4.  Simulate 1000 episodes.
5.  At which episode does $\epsilon$ drop below 0.1?

## Importance
If you decay too fast, the agent stops learning before finding the optimal path. If too slow, training takes forever.
