# Tabular Data Visualization

## 1. Introduction
One of the most important skills in Data Science is choosing the right chart for the job.

## 2. Univariate (Single Variable)
*   **Numerical**:
    *   **Histogram**: Shows frequency distribution/shape.
    *   **Boxbplot**: Shows median, quartiles, and outliers.
    *   **KDE (Kernel Density Estimate)**: Smoothed version of a histogram.
*   **Categorical**:
    *   **Bar Chart**: Count of each category.
    *   **Pie Chart**: Avoid unless strictly showing parts-of-a-whole (and few categories).

## 3. Bivariate (Two Variables)
*   **Num vs Num**:
    *   **Scatter Plot**: Shows relationship/correlation.
*   **Num vs Cat**:
    *   **Boxplot (grouped)**: Comparison of distributions across groups.
    *   **Bar Chart (agg)**: Comparison of means across groups.
*   **Cat vs Cat**:
    *   **Heatmap**: Frequency/Contingency table.
    *   **Stacked Bar**: composition within groups.

## 4. Multivariate (3+ Variables)
*   **Hue/Color**: Map a 3rd variable to color.
*   **Size**: Map a variable to point size (Bubble chart).
*   **FacetGrid**: Create small multiples (subplots) based on a categorical variable.
