# Type Hinting and Static Analysis

## 1. Dynamic Typing vs Static Typing
*   **Dynamic (Python default)**: `x = 5`, then `x = "Hello"`. Flexible but error-prone in large codebases.
*   **Static (C++/Java)**: `int x = 5`. Safety.

## 2. Type Hints (PEP 484)
*   Python allows optional type hints.
*   `def add(x: int, y: int) -> int:`
*   These are ignored by the runtime interpreter (mostly).

## 3. Static Analysis (mypy)
*   If you run `python code.py`, it ignores errors.
*   If you run `mypy code.py`, it checks the hints and flags errors BEFORE running.
*   **Generics**: `List[int]`, `Dict[str, float]`, `Optional[int]` (int or None).

## 4. Modern Types (Python 3.10+)
*   Use `list[int]` instead of `List[int]`.
*   Use `int | str` instead of `Union[int, str]`.
