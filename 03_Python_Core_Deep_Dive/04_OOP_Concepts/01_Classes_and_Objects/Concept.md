# Classes and Objects

## 1. Everything is an Object
*   In Python, integers, strings, and functions are all objects.
*   **Class**: The blueprint (e.g., `Dog`).
*   **Object**: The instance (e.g., `Buddy`).

## 2. The `__init__` Constructor
*   Initialize attributes when the object is created.
*   `self`: A reference to the current instance. It must be the first parameter of any instance method.

## 3. Class Attributes vs Instance Attributes
*   **Instance Attribute**: `self.name = name`. Unique to each object.
*   **Class Attribute**: `species = "Canis familiaris"`. Shared by ALL objects of that class.

## 4. Methods
*   **Instance Method**: `def bark(self):`. Can access `self`.
*   **Class Method**: `@classmethod def create_stray(cls):`. Can access `cls` (the class itself), but not `self`.
*   **Static Method**: `@staticmethod def is_cute():`. Cannot access `self` or `cls`. Just a regular function living inside a class namespace.
