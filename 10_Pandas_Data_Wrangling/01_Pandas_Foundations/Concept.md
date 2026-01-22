# Pandas Foundations

## 1. Introduction
Pandas is the de facto standard library for structured data manipulation in Python. It provides high-performance, easy-to-use data structures.

## 2. Core Data Structures
### Series
A one-dimensional labeled array capable of holding any data type. It is essentially a column in an Excel sheet.
*   **Index**: Labels for the data points.
*   **Values**: The actual data.

### DataFrame
A two-dimensional labeled data structure with columns of potentially different types. It is like a SQL table or a spreadsheet.
*   A DataFrame is a collection of Series that share the same index.

## 3. Selecting and Indexing
*   **`.loc[row_label, col_label]`**: Label-based selection. Best for when you know the name of the row/column.
*   **`.iloc[row_pos, col_pos]`**: Integer-position based selection. Best for selecting by index number (e.g., proper slicing).
*   **`df['col_name']`**: Select a single column (returns a Series).
*   **`df[['col1', 'col2']]`**: Select multiple columns (returns a DataFrame).

## 4. Filtering (Boolean Indexing)
You can filter rows based on conditions:
```python
# Select rows where age is greater than 30
filtered_df = df[df['age'] > 30]
```
Multiple conditions need parentheses and bitwise operators (`&`, `|`, `~`):
```python
df[(df['age'] > 30) & (df['city'] == 'New York')]
```
