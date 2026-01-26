# Task: Latent Space Disentanglement

## Objective
Concept purity.

## Setup
*   You define a \"Stripes\" concept.
*   But all your Zebra photos (Stripes) are also Black and White.
*   The Probe might learn \"Black and White\" instead of \"Stripes\".

## Task
1.  How to verify?
2.  Test against a \"Chessboard\" concept (Black and White but NOT striped).
3.  If the vector activates on Chessboards, your concept definition is flawed (Confounded).

## Question
Why is TCAV better than Saliency?
*   Answer: Saliency is local (per image). TCAV is global (per class). It tells you general rules the model follows ("Zebra requires Stripes"), rather than anecdotal evidence ("This zebra has a stripe here").
