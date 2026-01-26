# Magic Methods (Dunder Methods)

## 1. What are they?
*   Methods starting and ending with double underscores `__`.
*   They are called implicitly by Python operators or built-in functions.
*   `x + y` -> calls `x.__add__(y)`.
*   `len(x)` -> calls `x.__len__()`.
*   `print(x)` -> calls `x.__str__()`.

## 2. Common Magic Methods
*   **Initialization**: `__init__`, `__new__`.
*   **Representation**: `__str__` (user friendly), `__repr__` (developer friendly).
*   **Arithmetic**: `__add__`, `__sub__`, `__mul__`, `__truediv__`.
*   **Comparison**: `__eq__` (==), `__lt__` (<), `__gt__` (>).
*   **Container**: `__getitem__` (indexing), `__len__`, `__contains__` (in).

## 3. Operator Overloading
*   By implementing `__add__`, you can define what `+` means for your custom objects (e.g., Vector addition).
*   This makes your objects feel like native Python types.
