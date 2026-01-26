# Task: Augmentation Logic

## Objective
Define Positive Pairs.

## Input
Image A: A photo of a Golden Retriever running in a park.

## Task
1.  List 3 augmentations that preserve the \"identity\" (makes a valid Positive Pair).
    *   Example: Grayscale. (Still a dog).
2.  List 1 augmentation that might BREAK the identity (makes a bad Positive Pair).
    *   Example: Selecting a crop that only contains the grass in the corner. (Now it looks like a lawn, not a dog).

## Question
Why is \"Random Crop\" the most powerful augmentation for SSL? (Because it forces the model to verify that the 'Head' and the 'Tail' belong to the same object).
