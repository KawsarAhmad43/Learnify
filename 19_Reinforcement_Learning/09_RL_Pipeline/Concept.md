# The RL Pipeline (Gymnasium)

## 1. The Standard Interface
Before 2016, every RL researcher wrote their own `class Environment`.
*   Code was incompatible.
*   OpenAI released `Gym` (now `Gymnasium`).
*   Standard methods: `reset()`, `step(action)`, `render()`.

## 2. Vectorized Environments
Training on 1 game at a time is slow.
*   **VectorEnv**: Run 32 copies of Super Mario Bros in parallel.
*   Input: Batch of 32 Actions.
*   Output: Batch of 32 States, Rewards, Dones.
*   GPU Utilization: Keeps the GPU fed with data.

## 3. Wrappers
Don't rewrite the environment code to change observation shape. Wrap it.
*   `ResizeObservation`: Downscale pixels.
*   `GrayScaleObservation`: Remove color.
*   `FrameStack`: Stack 4 frames.
*   **Pipeline**: Env -> Wrapper 1 -> Wrapper 2 -> Agent.
