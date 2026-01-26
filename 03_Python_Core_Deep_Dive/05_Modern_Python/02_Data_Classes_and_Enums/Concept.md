# Data Classes and Enums

## 1. Boilerplate Problem
*   Writing `__init__`, `__repr__`, `__eq__` for classes that just hold data is tedious.
*   **Data Class (@dataclass)**: Automatically generates these methods based on type hints.

## 2. Enums
*   **Magic Numbers**: Using `0` for Pending, `1` for Active is bad practice.
*   **Enum**: `class Status(Enum): PENDING = 0`.
*   Safety: `Status.PENDING` is not equal to `0` (unless using `IntEnum`).

## 3. Immutability
*   `@dataclass(frozen=True)` makes the object immutable (read-only).
*   This makes it hashable, so you can use it as a dictionary key.
