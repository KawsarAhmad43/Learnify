# Task: Sybil Attacks

## Objective
The malicious user.

## Setup
*   In FL, users control the update $W_L$.
*   A hacker can spin up 1000 fake users (Sybils).
*   They all send $W_{poison} = - W_G$.
*   **Result**: They cancel out the learning of legitimate users, or worse, inject a backdoor (e.g., \"If input contains 'Trigger', predict 'Safe'\").

## Task
1.  How to prevent this?
2.  **Robust Aggregation**: Instead of Mean (which is sensitive to outliers), use **Median** or **Trimmed Mean** (discard top/bottom 10% updates).
3.  **Client Authentication**: Ensure each update comes from a valid, unique hardware device (Attestation).

## Question
What is 'Homomorphic Encryption' (HE)?
*   Answer: The Holy Grail. Doing math on encrypted data. $Enc(A) + Enc(B) = Enc(A+B)$. You never need to decrypt. It is currently very slow (1000x slower), but the future of privacy.
