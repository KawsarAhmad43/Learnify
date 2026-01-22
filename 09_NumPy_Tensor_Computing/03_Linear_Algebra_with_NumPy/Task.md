# Task: Linear Algebra

## Objective
Solve linear systems using NumPy.

## Tasks

### Task 1: System of Equations
Solve for $x, y, z$:
$$
3x + y = 9 \\
x + 2y = 8
$$

1.  Construct matrix $A$ and vector $b$.
2.  Use `np.linalg.solve(A, b)`.
3.  Verify the solution by doing `A @ x`.

### Task 2: Cosine Similarity
Calculate the cosine similarity between two vectors $u$ and $v$.
$$\text{Similarity} = \frac{u \cdot v}{||u|| \cdot ||v||}$$
*   $u = [1, 2, 3]$
*   $v = [4, 5, 6]$
*   Hint: `np.linalg.norm` calculates the magnitude.
