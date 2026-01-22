# Advanced Data Manipulation

## 1. GroupBy (Split-Apply-Combine)
The `groupby` operation is one of the most powerful tools in Pandas.
1.  **Split**: The data is split into groups based on criteria (e.g., group by 'Category').
2.  **Apply**: A function is applied to each group (e.g., sum, mean, count).
3.  **Combine**: The results are combined back into a data structure.

```python
df.groupby('Category')['Sales'].sum()
```

## 2. Merging and Joining
Used to combine multiple DataFrames (similar to SQL JOINs).
*   **`pd.merge(df1, df2, on='key', how='inner')`**:
    *   **Inner**: Keep only keys present in both.
    *   **Left**: Keep all keys from left, match with right (fill NaN if missing).
    *   **Right**: Keep all keys from right.
    *   **Outer**: Keep all keys from both.

## 3. Pivot Tables
Create a specialized Spreadsheet-style pivot table.
```python
df.pivot_table(values='Sales', index='Date', columns='Region', aggfunc='sum')
```

## 4. The Apply Function
Allows you to apply a custom function to every row or column.
```python
df['New_Col'] = df['Col'].apply(lambda x: x * 2)
```
*Note: Vectorized operations are generally preferred over `apply` for performance, but `apply` is very flexible.*
