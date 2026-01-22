# Task: Will we play Tennis?

## Objective
Build a decision tree from manual attributes.

## Data
*   **Outlook**: [Sunny, Sunny, Overcast, Rain, Rain]
*   **Humidity**: [High, High, High, Normal, Normal]
*   **Wind**: [Weak, Strong, Weak, Weak, Strong]
*   **Play**: [No, No, Yes, Yes, No]

Note: You will need to **Encode** these strings into numbers (OneHot or Label) first!

## Tasks
1.  **Encode**: Convert the categorical data to numbers.
2.  **Train**: Fit a `DecisionTreeClassifier`.
3.  **Visualize**: Plot the tree. Does it learn that "Overcast" is always Yes?
