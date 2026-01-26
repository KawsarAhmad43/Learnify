# Task: Manual TF-IDF

## Objective
Calculate the score by hand to understand the math.

## Corpus
1.  A: "cat dog"
2.  B: "cat cat"

## Formula
*   $TF(t, d) = \text{count of t in d} / \text{total words in d}$
*   $IDF(t) = \log(N / \text{df}(t))$ (Using Base 10 or e, usually e)
*   $N=2$

## Task
1.  Calculate TF("cat", A). (1/2 = 0.5)
2.  Calculate TF("cat", B). (2/2 = 1.0)
3.  Calculate IDF("cat"). (Present in A and B, so df=2).
    *   $IDF = \log(2/2) = \log(1) = 0$.
4.  Total Score = TF * IDF.
    *   Since "cat" is everywhere, its score is 0!

Write a python script to verify this behavior using sklearn (Note: Sklearn adds +1 to smoothing, so it won't be exactly 0, but it will be low).
