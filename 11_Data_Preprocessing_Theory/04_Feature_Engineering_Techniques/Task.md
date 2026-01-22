# Task: Feature Engineering

## Objective
Create new features to enrich a dataset.

## Data
Create a DataFrame:
*   **Length**: [10, 20, 30]
*   **Width**: [5, 10, 15]
*   **Date**: ['2023-01-01', '2023-07-04', '2023-12-25']

## Tasks
1.  **Interaction Feature**: Create a column `Area = Length * Width`.
2.  **Date Features**: Convert the Date column to datetime objects. Then create:
    *   `Month` column.
    *   `DayOfWeek` column.
3.  **Transformation**: Apply a log transformation to the `Area` column.
