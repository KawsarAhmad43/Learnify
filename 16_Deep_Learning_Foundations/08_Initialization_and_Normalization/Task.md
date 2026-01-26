# Task: Standardization (Z-Score)

## Objective
Normalize a feature so it helps the optimizer.

## Data (House Prices)
*   **Price**: `[100, 200, 300]` (in thousands)
*   **Range**: Huge compared to something like "Bedrooms" (1-5).

## Formula
$$ z = \frac{x - \mu}{\sigma} $$
$\mu$ = Mean
$\sigma$ = Standard Deviation

## Tasks
1.  Calculate Mean.
2.  Calculate Std Dev (Population or Sample is fine, just be consistent).
3.  Calculate transformed values.
4.  **Check**: The new mean should be 0. The new Std Dev should be 1.

Write a script to do this using NumPy.
