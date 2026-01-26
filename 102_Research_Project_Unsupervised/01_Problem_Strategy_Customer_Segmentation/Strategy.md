# Research Project: Customer Segmentation (RFM)

## 1. Problem Understanding
*   **Context**: An E-commerce store (like [Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail)) wants to personalize marketing.
*   **The Data**: Transaction logs (`InvoiceNo`, `StockCode`, `Quantity`, `InvoiceDate`, `CustomerID`, `UnitPrice`).
*   **The Problem**: "One size fits all" marketing is expensive. We need to group customers into "Whales", "New Users", "Lost Customers", "Loyalists".
*   **Challenge**: There are no labels (Unsupervised). We don't know the truth. We have to *discover* it.

## 2. Research Strategy
*   **Feature Engineering (RFM)**:
    *   **Recency**: How many days since last purchase? (Lower is better).
    *   **Frequency**: How many purchases total? (Higher is better).
    *   **Monetary**: How much total spend? (Higher is better).
*   **Skewness Handling**: Money/Frequency usually follow Power Law (80/20 rule). We must log-transform them, otherwise K-Means will just group by monetary value and ignore everything else.
*   **Clustering**: K-Means.
    *   **Elbow Method**: To find optimal `K` (number of clusters).

## 3. Step-by-Step Plan
1.  **Data Cleaning**: Remove negative quantities (Returns) and null CustomerIDs.
2.  **Aggregation**: Group by `CustomerID` and compute R, F, M.
3.  **Preprocessing**: Log Transform -> Standard Scaling. (K-Means is distance-based, so scale matters).
4.  **Modeling**: Run K-Means for K=1 to 10. Plot Elbow curve. Choos K (e.g., 3).
5.  **Interpretation**: Calculate average R, F, M for each cluster to name them (e.g., "High Spenders", "Churn Risk").
6.  **Visualization**: Use PCA (Principal Component Analysis) to project the 3D data onto 2D for plotting.
