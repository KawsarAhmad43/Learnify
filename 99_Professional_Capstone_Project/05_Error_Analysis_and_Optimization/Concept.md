# Error Analysis and Optimization

## 1. Opening the Black Box
*   Engineers will not trust your "AI Magic Box" if you just say "Replace the engine".
*   **SHAP (Shapley Additive Explanations)**: Game theory approach. "This prediction is 50 days RUL. Why? Because Temp is +10 (contributed -20 days) and Vibration is Normal (contributed +5 days)."
*   **Global Interpretability**: Which features matter most overall?
*   **Local Interpretability**: Why did THIS specific engine get a low score?

## 2. Automated Optimization (Optuna)
*   Grid Search is slow. Random Search is dumb.
*   **Bayesian Optimization (Optuna)**: Smart search. It assumes a probability model of the objective function and explores promising regions of hyperparameter space.
*   **Pruning**: If a trial looks bad at Epoch 10, kill it. Don't waste resources training to Epoch 100.

## 3. Deployment Considerations
*   **Model Size**: A 5GB model is too big for an Edge Device on a plane.
*   **Quantization**: Convert float32 weights to int8. 4x smaller, 2x faster, <1% accuracy loss.
*   **Drift Monitoring**: In production, we track the *distribution* of input data. If it changes (Covariate Shift), we trigger retraining.
