# Task: Pipeline Construction

## Objective
Refactor spaghetti code into a clean Scikit-Learn Pipeline.

## The Messy "Spaghetti" Code
Imagine this workflow:
1.  `df['Age'].fillna(df['Age'].mean(), inplace=True)`
2.  `df['Salary'] = scaler.fit_transform(df[['Salary']])`
3.  `model.fit(df, y)`

## Tasks
1.  Create a fresh dataset with 'Age' (missing values), 'Salary' (needs scaling), and 'Quality' (Category).
2.  Build a `ColumnTransformer` that:
    *   Imputes 'Age' with **Median**.
    *   Scales 'Salary' with **RobustScaler**.
    *   Ordinally Encodes 'Quality' (Map: Low=0, High=1).
3.  Fit the pipeline (Transformer + Logistic Regression) and make a prediction.
