# Handling Missing Data

## 1. Why is Data Missing?
Understanding the *mechanism* of missingness is crucial.
*   **MCAR (Missing Completely at Random)**: No pattern. Safe to drop if small amount.
*   **MAR (Missing at Random)**: Missingness depends on *observed* data (e.g., men are less likely to report depression, but we have gender data). Can be imputed.
*   **MNAR (Missing Not at Random)**: Missingness depends on the *unobserved* value itself (e.g., high income earners not reporting income). Hardest to deal with.

## 2. Strategies

### Deletion
*   **Listwise Deletion**: Drop entire rows with any missing value. Fast, but loses data.
*   **Pairwise Deletion**: Use available data for specific stats (e.g., correlation).

### Imputation (Filling)
*   **Mean/Median**: Fill with the average. Good baseline, but reduces variance.
*   **Mode**: For categorical data.
*   **KNN Imputation**: Find 'k' most similar rows and average their values. More accurate.
*   **MICE (Multivariate Imputation by Chained Equations)**: Models each missing feature as a function of others. State of the art.

## 3. Indicator Flags
Sometimes the fact *that* the data is missing is a signal in itself. Creating a binary `Is_Missing` column can help the model learn this pattern.
