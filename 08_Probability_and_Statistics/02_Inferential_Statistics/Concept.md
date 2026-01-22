# Inferential Statistics

## 1. Introduction
Inferential Stats allows us to make predictions or inferences about a population based on a sample of data. In Machine Learning, this is crucial for:
*   Comparing model performance (is Model A *significantly* better than Model B?).
*   Understanding feature importance.
*   A/B Testing.

## 2. Sampling Distributions & CLT
*   **Sampling Distribution**: The probability distribution of a given statistic (e.g., the mean) based on a random sample.
*   **Central Limit Theorem (CLT)**: The distribution of sample means approximates a normal distribution as the sample size becomes larger ($n > 30$), regardless of the population's shape.
    *   This is why Normal distribution is so ubiquitous in statisics.

## 3. Hypothesis Testing
A formal procedure for investigating our ideas about the world.

### Steps:
1.  **Null Hypothesis ($H_0$)**: The default position (e.g., "The coin is fair", "There is no difference between Model A and Model B").
2.  **Alternative Hypothesis ($H_1$ or $H_a$)**: What we want to prove (e.g., "The coin is biased").
3.  **Significance Level ($\alpha$)**: The probability of rejecting the null hypothesis when it is true (Type I error). Common value is 0.05.
4.  **Calculate Test Statistic**: A standardized value calculated from sample data (e.g., t-score, z-score).
5.  **Calculate p-value**: The probability of observing results as extreme as the sample data, assuming $H_0$ is true.
    *   **If p-value < $\alpha$**: Reject $H_0$ (Statistically Significant).
    *   **If p-value $\ge \alpha$**: Fail to reject $H_0$.

## 4. Common Tests

### T-Test
Used to compare the means of two groups.
*   **One-sample t-test**: Compare sample mean to a known population mean.
*   **Independent two-sample t-test**: Compare means of two independent groups (e.g., Control vs. Treatment).
*   **Paired t-test**: Compare means from the same group at different times (e.g., Before vs. After).

### ANOVA (Analysis of Variance)
Used to compare means across 3 or more groups. It tests if at least one group mean is different from the others.

### Chi-Square Test
Used for categorical data to check independence between two variables.

## 5. Confidence Intervals
A range of values used to estimate a population parameter. A 95% Confidence Interval means if we repeated the sampling method many times, 95% of the calculated intervals would contain the true population parameter.
