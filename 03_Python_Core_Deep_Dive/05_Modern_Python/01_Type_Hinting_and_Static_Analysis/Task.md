# Task: Protocol

## Objective
Structural Subtyping.

## Setup
*   You want a function that accepts ANY object that has a `fly()` method (Bird, Plane, Superman).
*   Inheritance is too rigid (Superman is not a Bird).

## Task
1.  Import `Protocol` from `typing`.
2.  Define a class `Flyable(Protocol)` with a method `def fly(self) -> str: ...`.
3.  Write a function `let_it_fly(item: Flyable)`.
4.  Pass in objects that do NOT inherit from `Flyable` but have the `fly()` method.
5.  Run `mypy` on your file. It should pass.
6.  Pass an object without `fly()`. `mypy` should fail.

## Question
What is `Any`?
*   Answer: `from typing import Any`. It disables type checking for that variable. It is the "Escape Hatch". Use it sparingly, otherwise you defeat the purpose of type hinting.
