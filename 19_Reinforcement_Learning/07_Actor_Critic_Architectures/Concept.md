# Actor-Critic

## 1. Best of Both Worlds
*   **Policy Gradient (The Actor)**: Good at actions, but high variance (noisy learning).
*   **Value Function (The Critic)**: Good at judging states (low variance), but can't find actions directly without a table.

## 2. The Setup
*   **Actor**: "I say we go Left." ($\pi(a|s)$)
*   **Critic**: "Going Left from here usually results in +10 points." ($V(s)$)
*   **Environment**: "You actually got +15 points."
*   **Advantage**: +15 (Actual) > +10 (Predicted). "Wow, that was better than expected!"
*   **Update**: Strengthen the "Go Left" action because it surprised the Critic.

## 3. A2C / A3C
Advantage Actor Critic. The standard stable learning algorithm before PPO took over.
