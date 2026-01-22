# Task: Time Series Analysis

## Objective
Analyze specific time periods and calculate changes.

## Tasks

### Task 1: Filter by Date
Using the dataset from the implementation notebook (generate it again):
1.  Filter the DataFrame to show only data for **February 2023**.
2.  Find the date with the **maximum price**.

### Task 2: Shifts and Changes
1.  Create a column `Daily_Return` calculated as: $\frac{\text{Price}_t - \text{Price}_{t-1}}{\text{Price}_{t-1}}$
    *(Hint: Use `.shift()` or `.pct_change()`)*
2.  Plot the histogram of daily returns. Is it normally distributed?
