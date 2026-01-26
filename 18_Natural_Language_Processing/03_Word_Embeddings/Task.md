# Task: Odd One Out

## Objective
Find the word that doesn't fit using vector distances.

## Word List
`["apple", "banana", "orange", "car"]`

## Mock Embeddings
*   apple: [1, 0]
*   banana: [0.9, 0.1]
*   orange: [0.95, 0.05]
*   car: [0, 1]

## Task
1.  Calculate the "Centroid" (Average) of all 4 vectors.
2.  Calculate the distance of each word from the Centroid.
3.  The word with the *largest* distance is the outlier.

## Formula
You can use Euclidean Distance ($ \sqrt{\sum (x-y)^2} $) or Cosine Distance.
