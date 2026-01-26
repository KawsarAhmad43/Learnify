# Loss Functions (The Scorecard)

## 1. What is a Loss Function?
To train a network, we need to know **how bad** it is doing.
*   **Loss ($L$)**: A single number representing the error for one example.
*   **Cost ($J$)**: The average loss over the entire dataset.
*   **Goal**: Minimize $J$ by adjusting weights.

## 2. For Regression (Predicting Numbers)
### Mean Squared Error (MSE)
$$ MSE = \frac{1}{N} \sum (y_{true} - y_{pred})^2 $$
*   **Why Squared?**: Punishes large errors more than small errors. Example: Error of 2 -> 4 penalty. Error of 10 -> 100 penalty.

## 3. For Classification (Predicting Categories)
### Binary Cross-Entropy (Log Loss)
Used for Yes/No problems (Sigmoid output).
$$ L = -[y \log(\hat{y}) + (1-y) \log(1-\hat{y})] $$
*   If $y=1$ and $\hat{y}=0.9$ (Good): Loss is low.
*   If $y=1$ and $\hat{y}=0.1$ (Bad): Loss is high.

### Categorical Cross-Entropy
Used for Multi-Class problems (Softmax output).
$$ L = -\sum y_{i} \log(\hat{y}_{i}) $$
Typically, we only care about the class that was *supposed* to be true (where $y_i=1$).
