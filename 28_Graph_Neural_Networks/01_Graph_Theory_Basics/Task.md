# Task: Isomorphism

## Objective
Geometry.

## Setup
*   Graph A: 3 nodes in a triangle.
*   Graph B: 3 nodes in a straight line.
*   Can you deform A into B without cutting edges? No.
*   Graph C: 3 nodes in a line (Nodes 1-2-3).
*   Graph D: 3 nodes in a line (Nodes 3-2-1). (Renumbered).
*   Are C and D the same graph? Yes. This is **Isomorphism**.

## Task
1.  Standard CNNs are NOT permutation invariant. If you swap pixel 1 and pixel 2, the CNN output changes.
2.  GNNs MUST be permutation invariant. The order of friends in the list shouldn't change the prediction.

## Question
What is 'Homophily'?
*   Answer: \"Birds of a feather flock together\". Connected nodes tend to have similar properties (e.g., age, interests). This is why GNNs work (Smoothing).
