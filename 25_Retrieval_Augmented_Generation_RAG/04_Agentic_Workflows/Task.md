# Task: Plan Generation

## Objective
Decomposition.

## Query
\"Create a summary of the impact of interest rates on tech stocks in 2022 vs 2023.\"

## Task
1.  If sent to Vector DB as one query, it might fail (documents talk about 2022 OR 2023, rarely both in contrast).
2.  Decompose into sub-questions:
    *   Q1: \"Interest rates 2022 impact tech stocks\"
    *   Q2: \"Interest rates 2023 impact tech stocks\"
    *   Q3: \"Comparison of 2022 and 2023 tech stock performance\"
3.  Retrieve for Q1, Q2, Q3.
4.  Combine context.

## Question
Why is single-step retrieval bad for complex queries?
*   Answer: Semantic drift. The vector for the complex query is an \"average\" location that might be far from the specific data points needed.
