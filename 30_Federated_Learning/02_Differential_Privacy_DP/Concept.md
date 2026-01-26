# Differential Privacy (DP)

## 1. The Membership Inference Attack
Can I tell if YOU were in the training set?
*   If the model predicts "Cancer" for your medical record with 99.99% confidence, but only 60% for a random person...
*   It probably *memorized* your record.
*   This breaches your privacy.

## 2. Plausible Deniability
DP gives you a mathematical guarantee: "The output of the model would be basically the same whether your data was included or not."
*   $\epsilon$ (Epsilon): The privacy budget. Smaller $\epsilon$ = More Privacy (More Noise).

## 3. The Mechanism: Noise
*   **Laplace Mechanism**: Add random noise to the answer.
    *   True Answer: 100 people have cancer.
    *   DP Answer: 103 people. (Or 98).
*   **DP-SGD**: Add noise to the *gradients* during training.
    1.  Compute Gradient.
    2.  Clip Gradient (Limit the max influence of one person).
    3.  Add Gaussian Noise.
    4.  Update Weights.
