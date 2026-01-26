# Task: The Masked Token

## Objective
Understand BERT's training objective.

## Sentence
"The quick brown [MASK] jumps."

## Vocabulary
`["cat", "dog", "fox", "table"]`

## Task
1.  Assume the model output logits for the `[MASK]` position are:
    *   cat: 2.5
    *   dog: 2.1
    *   fox: 5.8
    *   table: -1.0
2.  Apply Softmax manually (or conceptually).
3.  Which word fills the mask?

## Context
Why did it choose "fox"? Because "quick brown" and "jumps" are strong context clues found in the training data (English idioms). A "table" typically doesn't jump.
