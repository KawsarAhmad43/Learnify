# NumPy Foundations

## 1. Introduction
NumPy (Numerical Python) is the fundamental package for scientific computing in Python. It provides the **`ndarray`** (N-dimensional array) object, which is much faster and more efficient than Python lists.

## 2. The `ndarray` Object
An array is a grid of values, all of the same type, indexed by a tuple of non-negative integers.
*   **Rank**: Number of dimensions.
*   **Shape**: The size of each dimension (e.g., `(3, 4)` is a matrix with 3 rows and 4 columns).
*   **dtype**: The data type of the elements (e.g., `float64`, `int32`).

## 3. Creating Arrays
*   `np.array([1, 2, 3])`: From list.
*   `np.zeros((2,2))`: Array of all zeros.
*   `np.ones((2,2))`: Array of all ones.
*   `np.arange(10)`: Like Python `range()`.
*   `np.linspace(0, 1, 5)`: 5 linearly spaced values between 0 and 1.

## 4. Indexing and Slicing
Similar to Python lists but multidimensional.
*   `a[0, 1]`: Element at row 0, column 1.
*   `a[:, 1]`: All rows, column 1 (Slicing).
*   `a[1:3, :]`: Rows 1 and 2, all columns.

## 5. Reshaping
Changing the shape of an array without changing its data.
*   `a.reshape(2, 3)`
