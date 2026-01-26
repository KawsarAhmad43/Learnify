# Task: Text Generation (Manual)

## Objective
Simulate the generation loop.

## Model
Assume we have a model `M` that takes a letter and returns the next letter.
`M` behaves as follows:
*   h -> e
*   e -> l
*   l -> l
*   l -> o

## Task
1.  Start with input "h".
2.  Feed it to `M` to get output.
3.  Take that output and feed it back into `M`.
4.  Repeat 3 times.
5.  What is the final string?

## Hint
It's a `while` loop or `for` loop where `input = output`.
