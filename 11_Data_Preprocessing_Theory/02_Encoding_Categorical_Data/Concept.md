# Encoding Categorical Data

## 1. Types of Categorical Data
*   **Ordinal**: Has an inherent order (e.g., Low, Medium, High).
*   **Nominal**: No inherent order (e.g., Red, Blue, Green; New York, London).

## 2. Encoding Strategies

### Label Encoding (Ordinal)
Assigns a unique integer to each category (e.g., Low=0, Med=1, High=2).
*   *Pros*: Compact, preserves order.
*   *Cons*: If used on nominal data, models might misinterpret the order ($Blue > Red$?).

### One-Hot Encoding (Nominal)
Creates a new binary column for each category.
*   *Pros*: No false ordinal relationship.
*   *Cons*: Can create massive dimensionality (Curse of Dimensionality) if high cardinality (too many unique categories).

### Target Encoding (Mean Encoding)
Replaces category with the mean of the target variable for that category.
*   *Pros*: Compact, informative.
*   *Cons*: High risk of data leakage/overfitting.

## 3. Dummy Variable Trap
When one-hot encoding, valid columns sum to 1. This creates multicollinearity (Column A can be predicted from B and C). Solution: Drop the first column (`drop_first=True`).
