# Unsupervised Learning Foundations

## 1. What is Unsupervised Learning?
Learning **without a teacher**.
*   **No Labels**: We do not have "Right Answers" ($Y$). We only have Data ($X$).
*   **Goal**: Find hidden structures, patterns, or groupings in the data.

## 2. Core Paradigms
We are usually asking one of three questions:

### A. "Who is like whom?" (Clustering)
Grouping similar data points together.
*   **Scenario**: Customer Segmentation.
*   **Problem**: You have 1M users. You want to send 3 different emails. Who gets which?
*   **Solution**: Group users by behavior (Spenders, Browsers, Inactive).

### B. "What is weird?" (Anomaly Detection)
Finding points that don't belong.
*   **Scenario**: Credit Card Fraud.
*   **Problem**: Detecting a purchase that deviates from the user's normal pattern.
*   **Solution**: Flag points that are far from the "dense" clusters of normal behavior.

### C. "Can we simplify this?" (Dimensionality Reduction)
Reducing complexity while keeping information.
*   **Scenario**: Visualizing DNA (20,000 Genes).
*   **Problem**: You can't plot 20,000 axes.
*   **Solution**: Squash the data into 2D or 3D using PCA or t-SNE while preserving the relationships.

## 3. Real-Life Use Case Catalog

### Marketing & Retail
*   **Market Basket Analysis**: "People who buy Bread also buy Butter". (Association Rules).
*   ** recommender Systems**: "Users like you watched this". (Collaborative Filtering).

### Security
*   **Network Intrusion**: Identifying abnormal packet traffic.
*   **Manufacturing**: Detecting defective parts on an assembly line by spotting visual outliers.

### Biology
*   **Genomics**: Grouping patients by genetic expression profiles to discover new disease subtypes.
