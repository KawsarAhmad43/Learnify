# Task: Handling Missing Data

## Objective
Apply different strategies for filling missing data.

## Tasks

### Task 1: Identify Missingness
1.  Load the dataset (provided in Solution).
2.  Count the number of null values per column (`df.isnull().sum()`).
3.  Visualize the missingness (optional: `import seaborn as sns; sns.heatmap(df.isnull())`).

### Task 2: Strategy Application
1.  Fill the 'Category' column (categorical) using the **Mode** (Most Frequent).
2.  Fill the 'Score' column (numerical) using the **Median**.
3.  Drop rows where 'Critical_Feature' is missing.
