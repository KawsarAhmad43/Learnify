# Probability Theory & Distributions

## 1. Introduction to Probability
Probability is the mathematical framework for quantifying uncertainty. In Machine Learning, it underpins everything from model training (Maximum Likelihood Estimation) to evaluation (confidence intervals) and generative modeling (VAEs, Diffusion Models).

### Key Concepts
*   **Sample Space ($S$)**: The set of all possible outcomes of an experiment.
*   **Event ($E$)**: A subset of the sample space.
*   **Probability ($P(E)$)**: A measure of the likelihood that event $E$ occurs, where $0 \le P(E) \le 1$.

## 2. Random Variables (RVs)
A Random Variable is a function that maps outcomes of a random process to numerical values.

*   **Discrete RV**: Takes on a countable number of distinct values (e.g., outcome of a dice roll).
*   **Continuous RV**: Takes on an infinite number of possible values within a range (e.g., height of a person).

## 3. Probability Functions

### Probability Mass Function (PMF) - Discrete
For a discrete RV $X$, the PMF gives the probability that $X$ takes the value $x$:
$$P(X=x)$$

### Probability Density Function (PDF) - Continuous
For a continuous RV $X$, the PDF $f(x)$ describes the relative likelihood of the RV taking a value near $x$. The probability of $X$ falling in an interval $[a, b]$ is the integral of the PDF:
$$P(a \le X \le b) = \int_{a}^{b} f(x) dx$$

### Cumulative Distribution Function (CDF)
The CDF $F(x)$ gives the probability that the RV $X$ will take a value less than or equal to $x$:
$$F(x) = P(X \le x)$$

## 4. Common Distributions

### Discrete Distributions
1.  **Bernoulli Distribution**: Models a single binary experiment (success/failure) with probability $p$.
2.  **Binomial Distribution**: Models the number of successes in $n$ independent Bernoulli trials.
3.  **Poisson Distribution**: Models the number of events occurring in a fixed interval of time/space.

### Continuous Distributions
1.  **Uniform Distribution**: All intervals of the same length are equally probable.
2.  **Normal (Gaussian) Distribution**: The most important distribution in statistics due to the Central Limit Theorem. Characterized by mean ($\mu$) and variance ($\sigma^2$).
    $$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}$$
3.  **Exponential Distribution**: Models the time between events in a Poisson point process.

## 5. Expectation and Variance
*   **Expectation (Mean)** $E[X]$: The weighted average of all possible values.
*   **Variance** $Var(X)$: Measures the spread of the distribution; average squared deviation from the mean.
    $$Var(X) = E[(X - E[X])^2]$$
