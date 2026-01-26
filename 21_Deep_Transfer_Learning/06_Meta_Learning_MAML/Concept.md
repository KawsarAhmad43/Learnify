# Meta-Learning (Learning to Learn)

## 1. The Core Idea
Standard Learning: "Given images of Cats, learn filters to detect Cats."
Meta-Learning: "Given a new task (Detecting anything), learn an initialization ($\theta$) that can adapt to that task in 1 step."

## 2. MAML (Model-Agnostic Meta-Learning)
*   **Inner Loop**: Take current weights $\theta$. Train on Task A for 1 step -> $\theta'_A$. calculate Loss A.
*   **Outer Loop**: Check how good $\theta'_A$ is. Update original $\theta$ to make the Inner Loop better next time.
*   **Goal**: Find a set of weights that is "neutral" enough to jump to any specific task quickly.

## 3. Second Order Derivatives
MAML requires calculating the gradient of a gradient ($\nabla_{\theta} L(\theta - \nabla L)$).
This is computationally expensive, so people use First-Order MAML (Reptile) approximations.
