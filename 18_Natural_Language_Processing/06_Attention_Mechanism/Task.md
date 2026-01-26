# Task: Match the Query

## Objective
Simulate the Q/K matching Process.

## Database
1.  Key: "color", Value: "red"
2.  Key: "animal", Value: "cat"
3.  Key: "fruit", Value: "apple"

## Query
`q = "fruit"`

## Task
1.  Define simple \"Word Embeddings\" where `color`, `animal`, `fruit` are orthogonal vectors (like `[1,0,0]`, `[0,1,0]`, etc).
2.  Compute dot product of Query against all Keys.
3.  Which Score is highest?
4.  Retrieve the Value.

## Code Hint
Use `numpy.dot`.
