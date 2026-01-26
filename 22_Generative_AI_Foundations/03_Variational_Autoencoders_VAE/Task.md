# Task: KL Divergence Calculation

## Objective
Measure how different our distribution is from Normal using the analytical VAE formula.

## Formula
$D_{KL} = -0.5 * \sum(1 + \log(\sigma^2) - \mu^2 - \sigma^2)$

## Task
1.  Assume a perfect encoding: $\mu=0, \sigma^2=1$.
    *   $1 + 0 - 0 - 1 = 0$. KL is 0. (Perfect).
2.  Assume a bad encoding: $\mu=5$ (Shifted), $\sigma^2=1$.
    *   $1 + 0 - 25 - 1 = -25$.
    *   $-0.5 * -25 = 12.5$. High penalty!
3.  Assume a tiny variance: $\sigma^2=0.01$ (Collapsed to point), $\mu=0$.
    *   $1 + \log(0.01) - 0 - 0.01$.
    *   $1 - 4.6 - 0.01 = -3.6$.
    *   $-0.5 * -3.6 = 1.8$. Penalty!

## Question
Why does the model want $\sigma^2$ to be 1? (To ensure the latent space has volume and overlaps, allowing meaningful interpolation).
