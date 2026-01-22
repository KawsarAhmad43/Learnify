# Task: Probability & Distributions

## Objective
Apply your understanding of probability distributions to solve specific problems using Python.

## Instructions
1.  Open `Solution.ipynb` (or create a new notebook) to write your code.
2.  Use `scipy.stats` to answer the questions below.

## Tasks

### Task 1: The Normal Distribution
A machine packs bags of chips. The weight of the bags follows a Normal distribution with a **mean of 150g** and a **standard deviation of 2g**.

1.  What is the probability that a randomly selected bag weighs **less than 148g**?
2.  What is the probability that a bag weighs **between 149g and 151g**?
3.  What is the weight threshold such that **95% of bags** weigh less than this amount? (Hint: Use PPF/Inverse CDF)

### Task 2: The Poisson Distribution
A website receives an average of **5 concurrent users per minute**.

1.  What is the probability that exactly **7 users** visit in a given minute?
2.  What is the probability that **3 or fewer users** visit in a minute?
3.  Simulate the number of users per minute for an hour (60 samples) and plot the histogram.

### Task 3: Central Limit Theorem (Preview)
1.  Generate 1000 samples from a **Uniform Distribution** between 0 and 1.
2.  Plot the histogram.
3.  Now, generate 1000 experiments where each experiment consists of taking the **mean of 30 samples** from the Uniform distribution.
4.  Plot the histogram of these means. Does it look different from the first histogram?
