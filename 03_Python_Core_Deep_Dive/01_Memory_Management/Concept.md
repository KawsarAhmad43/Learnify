# Core Python for AI/ML

To be an effective AI/ML Engineer, you don't just need to "know Python"; you need to write **efficient**, **vectorized**, and **clean** Python code. This module focuses on the specific subsets of Python that are most relevant to Data Science.

## Key Concepts

### 1. Dynamic Typing and Memory Management
Python is dynamically typed. Everything is an object.
*   **Variables**: References to objects in memory.
*   **Mutability**: Lists and dictionaries are mutable; tuples and strings are immutable. This affects how functions handle arguments (pass-by-assignment).

### 2. Efficient Control Flow
*   **List Comprehensions**: A concise way to create lists. Often faster than for-loops.
    ```python
    squares = [x**2 for x in range(10)]
    ```
*   **Enumerate & Zip**: Pythonic ways to iterate.
    *   `enumerate(iterable)`: Returns index and value.
    *   `zip(list1, list2)`: Combines two iterables element-wise.

### 3. Functions as First-Class Citizens
*   Functions can be passed as arguments, returned from other functions, and assigned to variables.
*   **Lambda Functions**: Anonymous small functions. `lambda x: x + 1`.
*   **Args and Kwargs**: Flexible argument parsing using `*args` (positional) and `**kwargs` (keyword).

### 4. Comparison with Other Languages
Unlike C++ or Java, Python is slower for raw loops. In ML, we avoid raw loops by using libraries like NumPy which run C-optimized code under the hood. However, understanding standard Python data structures is crucial for data cleaning and pipeline orchestration.
