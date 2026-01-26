# Regularization & Norms

## 1. The Villain: Overfitting
When your model memorizes the training data but fails on new data.
*   **Symptoms**: Low Training Loss, High Validation Loss.
*   **Cause**: The model is too complex (too many neurons) or training too long.

## 2. L1 and L2 Regularization (Weight Decay)
We force the weights to be small. Large weights suggest overfitting (over-sensitivity to one feature).
$$ Loss = MSE + \lambda \sum W^2 $$

### L1 (Lasso)
*   Adds the *absolute value* of weights.
*   Result: Makes weights exactly 0. Leads to **Sparse Models** (Feature Selection).

### L2 (Ridge)
*   Adds the *squared value* of weights.
*   Result: Makes weights very small but not 0. Preferred for Deep Learning.

## 3. Dropout (The Specific DL Trick)
Randomly turn off neurons during training.
*   **Why?** Prevents neurons from co-adapting (relying too much on each other).
*   Forces the network to be redundant and robust.
*   *Note*: Only use dropout during training. Turn it off for testing/prediction.

## 4. Early Stopping
Stop training when Validation Loss starts to go up, even if Training Loss is still going down.
