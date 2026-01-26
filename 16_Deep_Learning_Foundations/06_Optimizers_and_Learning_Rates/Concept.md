# Optimizers & Learning Rates

## 1. The Gradient Descent Algorithm
Once we have the gradient (the direction of steepest ascent), we go the opposite way.
$$ Weight = Weight - (LearningRate \cdot Gradient) $$

### The Learning Rate ($\eta$)
*   **Too Small**: Training takes forever (baby steps).
*   **Too Big**: Training explodes or bounces around (overshooting).
*   **Just Right**: Converges quickly.

## 2. Advanced Optimizers (Smarter Descent)

### Momentum
Don't stop immediately if the gradient is 0. Keep moving like a heavy ball. Use past velocity.
*   Helps plow through local minima.

### RMSProp & Adagrad
Adaptive Learning Rates.
*   Parameters that change a lot get smaller learning rates.
*   Parameters that rarely change get larger learning rates.

### Adam (Adaptive Moment Estimation)
The King of Optimizers.
*   Combines **Momentum** + **RMSProp**.
*   Default choice for almost everything ($lr=0.001$).

## 3. Learning Rate Schedulers
Often we want to start high (to explore) and end low (to fine-tune).
*   **Step Decay**: Drop LR by half every 10 epochs.
*   **Cosine Annealing**: Smoothly decrease LR in a wave.
