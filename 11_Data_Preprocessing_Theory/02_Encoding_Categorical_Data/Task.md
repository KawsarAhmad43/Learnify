# Task: Encoding Strategies

## Objective
Choose the right encoding for different column types.

## Data
*   **City**: ['New York', 'Paris', 'New York', 'Tokyo'] (Nominal)
*   **Quality**: ['Good', 'Excellent', 'Poor', 'Good'] (Ordinal)
*   **Temperature**: [20, 25, 15, 22] (Numerical - Keep as is)

## Tasks
1.  Create the DataFrame.
2.  Use **Label Encoding** (or Map) for 'Quality'. Make sure the order is Poor < Good < Excellent.
3.  Use **One-Hot Encoding** (or `pd.get_dummies`) for 'City'. Drop the first column to avoid the dummy trap.
4.  Print the final dataset vector.
