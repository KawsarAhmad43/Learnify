# Linear Algebra with NumPy

## 1. Dot Product and Matrix Multiplication
*   **Dot Product**: The sum of the products of corresponding elements.
    *   `np.dot(a, b)`
    *   If `a` and `b` are 1D arrays: Inner product (scalar).
*   **Matrix Multiplication**:
    *   `np.matmul(A, B)` or the operator **`@`**.
    *   Condition: Inner dimensions must match (Cols of A == Rows of B).

## 2. The `np.linalg` submodule
Contains advanced linear algebra functions.
*   `np.linalg.inv(A)`: Inverse of A.
*   `np.linalg.eig(A)`: Eigenvalues and Eigenvectors.
*   `np.linalg.solve(A, b)`: Solves $Ax=b$.

## 3. Operations for Neural Networks
*   **Transpose**: `A.T`
*   **Element-wise product** (Hadamard product): `A * B`
