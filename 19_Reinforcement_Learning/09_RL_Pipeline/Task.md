# Task: Reward Clipping Wrapper

## Objective
Implement a wrapper that clips rewards to [-1, 1].

## Reasoning
In games like Pong, rewards might be large. Clipping stabilizes gradients.

## Task
1.  Define `RewardClipWrapper`.
2.  Override the `step` method.
3.  Logic: `new_reward = clip(original_reward, -1, 1)`.

## Test
*   Input Reward: 100 -> Output: 1
*   Input Reward: -50 -> Output: -1
*   Input Reward: 0.5 -> Output: 0.5
