# Task: Word Error Rate (WER)

## Objective
Evaluation.

## Setup
*   **True**: \"The cat sat on the mat.\"
*   **Pred**: \"The cat sat mat.\" (Deletion error).
*   **Pred**: \"The cat hat on the mat.\" (Substitution error).
*   **Pred**: \"The cat sat on the the mat.\" (Insertion error).

## Task
1.  **Levenshtein Distance**: Calculate the minimum number of edits to turn Pred into True.
2.  **WER Formula**: $(S + D + I) / N$.
    *   S = Substitutions.
    *   D = Deletions.
    *   I = Insertions.
    *   N = Number of words in reference.

## Question
What is 'Beam Search'?
*   Answer: Efficient decoding. Instead of picking just the Top 1 word at each step (Greedy), keep the Top 5 most likely *sentences* alive until the end. This handles ambiguity better ("Recognize speech" vs "Wreck a nice beach").
