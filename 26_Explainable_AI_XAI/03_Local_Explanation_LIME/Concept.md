# LIME (Local Interpretable Model-agnostic Explanations)

## 1. The Intuition
The world is curved (Non-Linear). But if you zoom in enough, everything looks flat (Linear).
*   Deep Neural Networks have complex, curved decision boundaries.
*   **LIME** zooms in on a single data point and fits a simple Linear Regression model *locally* around that point.

## 2. The Process
1.  **Select Instance**: Pick the image/text you want to explain.
2.  **Perturb**: Create 1000 variations (add noise, hide chunks of text, gray out pixels).
3.  **Predict**: Feed these variations to the Black Box model.
4.  **Weight**: Validations closer to the original are weighted higher.
5.  **Fit Linear**: Train a weighted linear model on these variations.
6.  **Interpret**: The coefficients of this simple linear model explain the local behavior.

## 3. "Model Agnostic"
LIME doesn't need to know the weights of the model. It treats it as a function $f(x)$. It works for XGBoost, BERT, ResNet, anything.
