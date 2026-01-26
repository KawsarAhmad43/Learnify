# Research Project: Reinforcement Learning (Inventory Control)

## 1. Problem Understanding
*   **Context**: A warehouse.
*   **Decisions**: Every day, decide how many units to order (`Action`).
*   **State**: Current Inventory Level, Demand Forecast.
*   **Reward**: Minimize Cost (Holding Cost + Missed Sales Penalty).
    *   If Inventory too high -> High Holding Cost.
    *   If Inventory too low -> Opportunity Cost (Lost Customer).
*   **Why RL?**: Demand is stochastic (random). Traditional formulas (EOQ) assume constant demand. RL learns to adapt to variance.

## 2. Research Strategy
*   **Environment**: Built on `gymnasium` (formerly OpenAI Gym).
    *   `reset()`: Start day 0 with 50 items.
    *   `step(action)`: Simulator. Subtract sales, add arriving orders, calculate cost, return `next_state` and `reward`.
*   **Algorithm**: PPO (Proximal Policy Optimization).
    *   Why? Stability. DQN is brittle. PPO is the industry standard for continuous control.
*   **Framework**: `Stable-Baselines3`.

## 3. Step-by-Step Plan
1.  **Define Gym Env**: `class InventoryEnv(gym.Env)`.
    *   Define `observation_space`: [Current_Stock].
    *   Define `action_space`: Discrete(0 to 20 units).
2.  **Reward Function**: `Reward = - (Stock * HoldingCost + Missed_Sales * Penalty)`. Note the negative sign (RL maximizes reward, so we maximize negative cost).
3.  **Training**: Run PPO for 10,000 timesteps.
4.  **Baseline Comparison**: Compare RL Agent vs "Order Minimum" Strategy.
