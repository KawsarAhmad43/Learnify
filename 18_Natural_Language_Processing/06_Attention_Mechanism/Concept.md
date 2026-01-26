# The Attention Mechanism

## 1. The Bottleneck Problem
In RNN Encoder-Decoders (Sequence-to-Sequence), the Encoder must squash the entire source sentence into a **single** context vector.
*   Source: "The quick brown fox jumps over the lazy dog." (9 Words)
*   Context: `[0.1, -0.4, 0.9]` (Fixed size).
*   Result: Information Loss for long sentences.

## 2. Attention (Bahdanau, 2014)
The Decoder should look at the **entire** source sentence at every step, but focus only on relevant parts.
*   Translating "fox": Look at "fox".
*   Translating "jumps": Look at "jumps".

## 3. Keys, Queries, Values
Think of a Database.
*   **Query (Q)**: What I am looking for? ("The word related to 'jumping'").
*   **Key (K)**: The label of the data ("Action: Jump", "Subject: Fox").
*   **Value (V)**: The actual content.
*   **Score**: How well does Query match Key?
*   **Weighted Sum**: Result = $\sum Score \cdot Value$.

## 4. Self-Attention
When a sentence looks at *itself* to understand context.
*   "The animal didn't cross the street because **it** was too tired."
*   Does **it** refer to "animal" or "street"?
*   Self-Attention links "it" strongly to "animal".
