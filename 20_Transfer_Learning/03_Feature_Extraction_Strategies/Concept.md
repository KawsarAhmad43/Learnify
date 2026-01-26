# Feature Extraction vs Fine-Tuning

## 1. Feature Extraction (The "Frozen" Approach)
*   Treat the Pre-trained model as a fixed function $f(x)$.
*   Pass your image $x$ through $f(x)$ to get a vector (embedding).
*   Train a small, shallow model (Logistic Regression, SVM, or 1 Linear Layer) on top of this vector.
*   **Pros**: Super fast, no risk of breaking the pre-trained weights.
*   **Cons**: The backbone doesn't adapt to nuances of your new data.

## 2. Fine-Tuning (The "Unfrozen" Approach)
*   Initialize with Pre-trained weights.
*   Set a very small learning rate (e.g., $1e-5$).
*   Update ALL weights (Backbone + Head).
*   **Pros**: Higher accuracy potential.
*   **Cons**: Slow, requires more data, risk of "Catastrophic Forgetting".

## 3. The Hybrid Strategy
1.  **Freeze** Backbone. Train Head for 5 epochs. (Stabilize gradients).
2.  **Unfreeze** last 2 blocks of Backbone. Train for 10 epochs.
3.  **Unfreeze** everything (optional).
