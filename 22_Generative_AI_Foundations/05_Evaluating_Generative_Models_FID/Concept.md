# Evaluating GenAI (FID)

## 1. Why Accuracy is Useless
We can't calculate "Accuracy" for a generator.
*   "Generate a Cat."
*   If the model generates a NEW cat that resembles a Persian Cat, but the ground truth was a Siamese Cat, is it wrong?
*   MSE (Pixel Distance) says YES (100% Error).
*   Human says NO (It's a valid cat).

## 2. Inception Score (IS)
*   Uses a pre-trained InceptionV3 Classifier.
*   **Condition 1 (Realism)**: P(y|x) should be sharp. The classifier should be confident it's a cat.
*   **Condition 2 (Diversity)**: P(y) should be broad. The model should generate Cats, Dogs, Boats, etc., not just Cats.

## 3. Fréchet Inception Distance (FID) - The Gold Standard
IS only looks at the *generated* images. FID compares *Generated* vs *Real*.
1.  Pass 10k Real Images through InceptionV3 -> Get features. Calculate Mean ($\mu_r$) and Covariance ($\Sigma_r$).
2.  Pass 10k Fake Images -> Get Mean ($\mu_g$) and Covariance ($\Sigma_g$).
3.  Calculate distance between these two Gaussian distributions.
*   **Lower FID = Better**. Matches the real distribution more closely.
