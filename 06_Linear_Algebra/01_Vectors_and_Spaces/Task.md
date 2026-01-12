# Tasks: Linear Algebra

## Task 1: NumPy Basics for Linear Algebra
You will need `numpy` for this.
1.  Create two vectors `v1 = [2, 3]` and `v2 = [4, -1]`.
2.  Calculate their **dot product** manually (element-wise multiplication and sum) and then using `np.dot`.
3.  Calculate the **L2 Norm** (magnitude) of `v1`.

## Task 2: Matrix Multiplication
1.  Create a matrix $A$ of shape (2, 3) and a matrix $B$ of shape (3, 2).
2.  Multiply them to get matrix $C$ ($C = AB$). Verify the shape of $C$.
3.  Try to compute $BA$. Is the shape different?

## Task 3: Cosine Similarity
Cosine similarity is a measure of similarity between two non-zero vectors.
$$ \text{similarity} = \cos(\theta) = \frac{A \cdot B}{||A|| ||B||} $$
1.  Write a function `cosine_similarity(v1, v2)`.
2.  Calculate similarity between `[1, 0]` and `[0, 1]` (Should be 0).
3.  Calculate similarity between `[1, 1]` and `[2, 2]` (Should be 1.0).
