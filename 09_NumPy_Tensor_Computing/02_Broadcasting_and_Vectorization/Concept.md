# Broadcasting and Vectorization

## 1. Vectorization
Vectorization means applying operations to whole arrays at once, rather than iterating through them with loops.
*   **Why?** NumPy pushes the loop into compiled C code, making it orders of magnitude faster.
*   **Example**: `C = A + B` (Adds corresponding elements).

## 2. Broadcasting
Broadcasting is the mechanism that allows NumPy to perform arithmetic on arrays of different shapes.
*   **The Rule**: In order to broadcast, the size of the trailing axes for both arrays in an operation must either be the **same size** or one of them must be **one**.

### Examples
*   Matrix `(4, 3)` + Scalar `(1)` -> Scalar is broadcast to `(4, 3)`.
*   Matrix `(4, 3)` + Vector `(3,)` -> Vector is broadcast to every row.
*   Matrix `(4, 3)` + Vector `(4, 1)` -> Vector is broadcast to every column.

## 3. Universal Functions (ufuncs)
Functions that operate element-wise on arrays.
*   `np.add`, `np.subtract`, `np.sin`, `np.exp`, `np.sqrt`.
