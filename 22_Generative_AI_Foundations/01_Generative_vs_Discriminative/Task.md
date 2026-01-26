# Task: Probability Math

## Objective
Distinguish $P(Y|X)$ vs $P(X, Y)$.

## Setup
*   Dataset: [Image, Label] pairs.

## Task
1.  **Discriminative**: We want to find the label $Y$ that maximizes probability given image $X$.
    *   $\text{argmax}_Y P(Y|X)$.
2.  **Generative**: We want to learn the joint probability of pixels and labels.
    *   $P(X, Y) = P(X|Y)P(Y)$.
    *   $P(X|Y)$: \"What does a Cat ($Y$) look like ($X$)?\"
    *   $P(Y)$: \"How common are Cats?\"

## Question
If you have a perfect Generative Model $P(X, Y)$, can you build a Classifier?
*   Yes! Using Bayes Rule: $P(Y|X) = \frac{P(X|Y)P(Y)}{P(X)}$.
*   If you can create it, you can classify it. (But it's overkill).
