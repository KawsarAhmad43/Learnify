# New Features (Walrus & Pattern Matching)

## 1. The Walrus Operator `:=` (Python 3.8)
*   **Assignment Expression**: Allows you to assign a value to a variable *inside* an expression.
*   **Syntax**: `(x := 5)`.
*   **Use Case**: Avoiding double function calls in `if` or `while` loops.

## 2. Structural Pattern Matching (Python 3.10)
*   **Match/Case**: Python's switch statement on steriods.
*   It's not just equality checking. It can unpack sequences and check types.
*   **Syntax**:
    ```python
    match command:
        case ["quit"]:
            quit()
        case ["move", x, y]:
            move(x, y)
    ```

## 3. Positional-Only Parameters `/` (Python 3.8)
*   `def func(x, /, y):`
*   `x` MUST be positional. `y` can be positional or keyword.
*   Useful for API design where the name of the argument doesn't matter (like `len(obj)`).
