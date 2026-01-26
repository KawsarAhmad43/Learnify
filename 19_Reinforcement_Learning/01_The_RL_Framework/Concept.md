# The RL Framework

## 1. The Agent-Environment Loop
Reinforcement Learning is about an **Agent** interacting with an **Environment** to maximize **Reward**.
*   **Time ($t$)**: RL is sequential.
*   **State ($s_t$)**: What the agent sees (e.g., Camera pixels, Robot joint angles).
*   **Action ($a_t$)**: What the agent does (e.g., Move Left, Apply Brake).
*   **Reward ($r_t$)**: The immediate feedback (e.g., +10 points, -1 life).
*   **Next State ($s_{t+1}$)**: Where the agent ends up after the action.

## 2. The Goal: Maximizing Return
The goal is NOT to get the highest immediate reward, but the highest cumulative score (Return) over the episode.
*   $G_t = r_t + \gamma r_{t+1} + \gamma^2 r_{t+2} + \dots$
*   **Discount Factor ($\gamma$)**: A number between 0 and 1.
    *   $\gamma=0$: Greedy (Only care about now).
    *   $\gamma=1$: Patient (Care about the far future equally).

## 3. Markov Decision Process (MDP)
The mathematical name for this setup.
*   It assumes the **Markov Property**: The future depends only on the present, not the past.
