# Feature Scaling and Normalization

## 1. Why Scale?
Many Machine Learning algorithms perform poorly if features have different scales (e.g., Age: 0-100 vs Salary: 0-100,000).
*   **Gradient Descent**: Converges much faster on scaled data (circular vs elliptical error surface).
*   **Distance-Based Algorithms (KNN, K-Means, SVM)**: Dominated by large features if unscaled.
*   **Tree-Based Algorithms (Decision Trees, Random Forest)**: Generally **invariant** to scaling.

## 2. Techniques

### Standardization (Z-score Normalization)
Rescales data to have a Mean ($\mu$) of 0 and Standard Deviation ($\sigma$) of 1.
$$x' = \frac{x - \mu}{\sigma}$$
*   **Use when**: The distribution is roughly Normal. Less sensitive to outliers than Min-Max.

### Normalization (Min-Max Scaling)
Rescales data to a fixed range, usually [0, 1].
$$x' = \frac{x - \min(x)}{\max(x) - \min(x)}$$
*   **Use when**: You need a bounded range (e.g., for Neural Networks).

### Robust Scaling
Uses the Median and Interquartile Range (IQR).
$$x' = \frac{x - \text{median}}{IQR}$$
*   **Use when**: Data has significant **outliers**.
