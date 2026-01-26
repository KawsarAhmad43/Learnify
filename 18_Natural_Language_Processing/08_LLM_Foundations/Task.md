# Task: Few-Shot Prompting

## Objective
Guide the model without training.

## Goal
Classify movie reviews as "Positive" or "Negative".

## Zero-Shot Prompt
```
Review: "The movie was okay."
Sentiment:
```

## Few-Shot Prompt
Construct a prompt that teaches the model the pattern.

## Task
Write a string that includes:
1.  Example 1: "Loved it" -> Positive.
2.  Example 2: "Hated it" -> Negative.
3.  Target: "It was barely watchable" -> ?

## Question
Why does this work better than Zero-Shot? (Because it defines the output format and the vibe).
