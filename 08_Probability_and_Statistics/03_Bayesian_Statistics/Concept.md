# Bayesian Statistics

## 1. Frequentist vs. Bayesian
*   **Frequentist**: Probability is the long-run frequency of an event occurring (e.g., if we flip this coin infinite times, 50% will be heads). Parameters are fixed, unknown constants.
*   **Bayesian**: Probability is a measure of belief or certainty. Parameters are random variables with their own distributions. We update our beliefs as we see data.

## 2. Bayes' Theorem
The core mathematical foundation:
$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

In the context of Machine Learning parameters ($\theta$) and Data ($D$):
$$P(\theta|D) = \frac{P(D|\theta) \cdot P(\theta)}{P(D)}$$

*   **Prior $P(\theta)$**: Our belief about the parameters *before* seeing the data.
*   **Likelihood $P(D|\theta)$**: How probable is the data given specific parameters?
*   **Posterior $P(\theta|D)$**: Our updated belief about the parameters *after* seeing the data.
*   **Evidence $P(D)$**: A normalizing constant (often hard to compute, leading to methods like MCMC or VI).

## 3. Key Concepts
*   **Maximum A Posteriori (MAP)**: Finding the parameter $\theta$ that maximizes the posterior. This is similar to MLE (Maximum Likelihood Estimation) but includes the Prior (regularization).
    *   L2 Regularization (Ridge) corresponds to a Gaussian Prior.
    *   L1 Regularization (Lasso) corresponds to a Laplacian Prior.
*   **Conjugate Priors**: If the Prior and Likelihood share a certain mathematical structure, the Posterior will be in the same family as the Prior (algebraically closed).
    *   Beta prior + Binomial likelihood -> Beta posterior.
    *   Normal prior + Normal likelihood -> Normal posterior.

## 4. Why Bayesian?
1.  **Uncertainty Quantification**: We get a full distribution of parameters, not just point estimates.
2.  **Incorporating Prior Knowledge**: Useful when data is scarce.
3.  **Online Learning**: Yesterday's posterior becomes today's prior.
