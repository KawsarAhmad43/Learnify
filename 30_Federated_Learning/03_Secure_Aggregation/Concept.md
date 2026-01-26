# Secure Aggregation

## 1. The Problem
In FedAvg, the server sees $W_1, W_2, ... W_N$.
*   By looking at $W_1$, the server can reverse-engineer User 1's data (Model Inversion Attack).
*   **Goal**: The server should see ONLY the Sum $\sum W_i$, but never any individual $W_i$.

## 2. One Time Pad (Masking)
*   Client 1 and Client 2 agree on a random secret number $S$.
*   Client 1 sends: $W_1 + S$.
*   Client 2 sends: $W_2 - S$.
*   Server computes Sum: $(W_1 + S) + (W_2 - S) = W_1 + W_2$.
*   The mask cancels out! The server knows the Sum, but learned nothing about $W_1$ (because it looks like random noise).

## 3. Robustness
What if Client 2 drops out?
*   Server has $W_1 + S$. The mask doesn't cancel.
*   Protocols like **Bonawitz et al. (2017)** use Secret Sharing (Shamir's Secret Sharing) to allow the server to "recover" the mask $S$ only if enough users drop out, without recovering the user's data.
