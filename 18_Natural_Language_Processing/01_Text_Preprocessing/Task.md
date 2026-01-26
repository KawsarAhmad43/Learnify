# Task: Stemming vs Lemmatization

## Objective
Understand the difference between chopping (Stemming) and looking up (Lemmatization).

## Input
`words = ["running", "flies", "better", "meeting"]`

## Task
1.  Initialize `PorterStemmer` and `WordNetLemmatizer` from NLTK.
2.  Process the list with both.
3.  Compare results.

## Expectations
*   **Running**: Stem->`run`, Lemma->`running` (needs POS tag 'v' to become `run`).
*   **Flies**: Stem->`fli`, Lemma->`fly`.
*   **Better**: Stem->`better`, Lemma->`good`.
*   **Meeting**: Stem->`meet` (verb meaning), Lemma->`meeting` (noun meaning).

Write a script to verify this.
