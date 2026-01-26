# Inheritance and Polymorphism

## 1. Inheritance (Is-A Relationship)
*   **Don't Repeat Yourself (DRY)**: If `Car` and `Bike` both have `speed` and `move()`, create a parent class `Vehicle`.
*   **Syntax**: `class Child(Parent):`.
*   **super()**: Call the parent's method. `super().__init__()`.

## 2. Polymorphism (Many Forms)
*   **Method Overriding**: The child class provides a specific implementation of a method that is already defined in its parent class.
*   **Duck Typing**: "If it walks like a duck and quacks like a duck, it's a duck." Python doesn't care about the strict class, only if the object has the required method.
*   Example: `len()` works on List, Tuple, String, and Dictionary because they all implement `__len__`.

## 3. Multiple Inheritance
*   Python supports inheriting from multiple classes: `class Bat(Mammal, Bird):`.
*   **MRO (Method Resolution Order)**: Python uses the C3 Linearization algorithm to decide which parent method to call. Check `ClassName.mro()`.
