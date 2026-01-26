# Normalizing Flows and EBMs

## 1. The Search for Exact Likelihood
*   **GANs**: Good samples, but we don't know $P(x)$.
*   **VAEs**: We know a lower bound of $P(x)$ (ELBO).
*   **Flows**: We know the **EXACT** $P(x)$.

## 2. Change of Variables
If we have a simple distribution $Z \sim N(0, 1)$ and an invertible function $X = f(Z)$, we can calculate the probability of $X$.
*   $P(X) = P(Z) \cdot |\det(Jacobian)|^{-1}$.
*   **Intuition**: If the function $f$ stretches space (determinant > 1), the density goes down. If it squeezes space (determinant < 1), density goes up.

## 3. Energy Based Models (EBMs)
Inspired by Physics (Boltzmann distribution).
*   Assign low Energy $E(x)$ to real data (stable states).
*   Assign high Energy to fake data.
*   $P(x) = \frac{e^{-E(x)}}{Z}$.
*   Problem: $Z$ (the partition function) is impossible to calculate for images.
