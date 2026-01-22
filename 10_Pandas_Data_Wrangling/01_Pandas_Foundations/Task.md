# Task: Pandas Foundations

## Objective
Practice selecting and filtering data using Pandas.

## Dataset
Use the built-in dataset creation code provided in the solution notebook (or similar dictionary-based data).

## Tasks

### Task 1: Basic Stats
Create a DataFrame with at least 10 rows containing: 'Product', 'Price', 'Category', 'Rating'.

1.  Display the first 5 rows (`head`).
2.  Display summary statistics (`describe`) for the numerical columns.
3.  Display the data types (`dtypes`) of all columns.

### Task 2: Advanced Filtering
1.  Select all products that belong to the 'Electronics' **Category** AND have a **Price** greater than 500.
2.  Select the **Product** and **Rating** columns for items with a **Rating** less than 3.0.

### Task 3: Indexing
1.  Set the 'Product' column as the index of the DataFrame.
2.  Select the row for a specific product using its name (use `.loc`).
