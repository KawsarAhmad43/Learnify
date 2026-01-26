# Task: Feasibility Constraints

## Objective
Reality Check.

## Setup
*   Model predicts House Price.
*   Input: {Bedrooms: 3, Lat: 40.7, Long: -74.0}.
*   Counterfactual Optimizer wants to increase Price by $100k.
*   Result: {Bedrooms: 3.2, Lat: 40.7, Long: -74.0}.

## Task
1.  Critique this explanation.
    *   **Fractional Bedrooms**: You can't have 3.2 bedrooms. Must constrain to Integers.
    *   **Location**: It didn't suggest moving the house (Lat/Long are usually immutable for a specific house).
2.  Better Explanation: \"Add a bathroom\" or \"Increase square footage by 500 sqft\".

## Question
Why is 'Diversity' of counterfactuals important?
*   Answer: Giving the user 3 options (Earn more OR Pay off debt OR Get a co-signer) is better than forcing one path.
