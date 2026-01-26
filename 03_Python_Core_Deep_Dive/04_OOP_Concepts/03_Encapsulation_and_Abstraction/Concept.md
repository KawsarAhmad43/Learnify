# Encapsulation and Abstraction

## 1. Encapsulation (Information Hiding)
*   **Public**: `self.name`. Accessible from anywhere.
*   **Protected**: `self._internal`. Indication to other devs: "Don't touch this unless you inherit from me". Python doesn't enforce this.
*   **Private**: `self.__secret`. Python mangles this name to `_ClassName__secret` to make it harder (but not impossible) to access.

## 2. Getters and Setters (The Pythonic Way)
*   Don't use `get_name()` and `set_name()`.
*   Use `@property` decorators.
*   It allows you to add logic (validation) to attribute access without changing the interface.

## 3. Abstraction
*   Hiding complexity.
*   **Abstract Base Class (ABC)**: A class that cannot be instantiated. It defines a blueprint.
*   `from abc import ABC, abstractmethod`.
*   Any child class MUST implement all abstract methods.
