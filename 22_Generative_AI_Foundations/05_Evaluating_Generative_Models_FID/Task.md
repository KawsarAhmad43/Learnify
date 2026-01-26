# Task: Distribution Matching

## Objective
Understand why mean and variance matter.

## Setup
*   Real Data (Cars): Average color is Red (Mean 200), Variance is high (Red, Blue, Black).
*   Fake Data A (Red blobs): Average color is Red (Mean 200), Variance is 0 (Only Red).
*   Fake Data B (Rainbow): Average color is Red (Mean 200), Variance is high (Red, Blue, Black).

## Task
1.  Evaluate A: Means match, but Covariance is wrong. FID penalty. (Mode Collapse).
2.  Evaluate B: Means match, Covariance matches. Low FID. (Good Geometry).

## Question
Why is it better to generate \"Bad quality but diverse\" images than \"High quality but identical\" images?
*   Answer: Diversity is key for generalization. If a car simulator only generates red cars, the self-driving AI will crash into a blue truck.
