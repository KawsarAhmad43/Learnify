# Optimization Algorithms

## 1. The Goal of Optimization
In Machine Learning, we define a **Loss Function** $L(\theta)$ that measures how "bad" our model is. Our goal is to find the parameters $\theta$ that minimize this loss:
$$\min_{\theta} L(\theta)$$

## 2. Gradient Descent
Since the gradient points in the direction of steepest ascent, we can move in the **opposite** direction to minimize the function.

### Update Rule
$$\theta_{new} = \theta_{old} - \alpha \nabla L(\theta_{old})$$
Here, $\alpha$ is the **Learning Rate**, a hyperparameter that controls how big of a step we take.

## 3. Convexity
*   **Convex Function**: Has a single global minimum (bowl shape). Gradient Descent is guaranteed to find it.
*   **Non-Convex Function**: Has many local minima and saddle points (e.g., Deep Neural Networks). Gradient Descent might get stuck in a local minimum.

## 4. Variants of Gradient Descent
*   **Stochastic Gradient Descent (SGD)**: Updates using one sample at a time. Noisy but fast.
*   **Mini-Batch SGD**: Updates using a small batch of samples (e.g., 32). The standard in Deep Learning.
*   **Momentum**: Accumulates past gradients to smooth out the updates.
