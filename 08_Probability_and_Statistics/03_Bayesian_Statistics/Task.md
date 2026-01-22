# Task: Bayesian Statistics

## Objective
Understand how Bayes' theorem applies to classification (Naive Bayes).

## Tasks

### Task 1: Simple Spam Filter (Manual Calculation)
You have the following data:
*   P(Spam) = 0.4
*   P(Not Spam) = 0.6
*   The word "Buy" appears in 50% of Spam emails: P("Buy" | Spam) = 0.5
*   The word "Buy" appears in 10% of Not Spam emails: P("Buy" | Not Spam) = 0.1

1.  Calculate **P(Spam | "Buy")** using Bayes' Theorem.
2.  If an email contains the word "Buy", is it more likely to be Spam or Not Spam?
3.  Write a Python function `bayes_update(prior, likelihood_true, likelihood_false)` to calculate this.

### Task 2: Beta Distribution Analysis
1.  Plot a Beta distribution with `alpha=2` and `beta=2`. What does it look like?
2.  Update it with data: **100 successes (heads)** and **100 failures (tails)**. Plot the new posterior.
3.  What happens to the width (variance) of the curve as you add more data? Explain why.
