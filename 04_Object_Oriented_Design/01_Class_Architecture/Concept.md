# Object-Oriented Programming (OOP) in Python for ML

OOP is crucial for building scalable ML pipelines, custom PyTorch models, and modular codebases. In ML, everything from a standard scaler to a complex Neural Network is implemented as a class.

## Key Concepts

### 1. Classes and Objects
*   **Class**: A blueprint for creating objects.
*   **Object**: An instance of a class.
*   `__init__`: The constructor method. Initializes the object's attributes.
*   `self`: A reference to the current instance of the class.

### 2. Inheritance
Inheritance allows a class (Child) to derive attributes and methods from another class (Parent). This promotes code reuse.
*   **Example**: `class NeuralNetwork(nn.Module):` inherits from PyTorch's base Module class.
*   `super()`: Used to call methods from the parent class.

### 3. Encapsulation
Bundling data (attributes) and methods (functions) that operate on the data into a single unit.
*   **Private attributes**: Prefixed with `_` (convention) or `__` (name mangling) to indicate they shouldn't be accessed directly from outside.

### 4. Special (Dunder) Methods
Python classes can emulate built-in types using double underscore methods.
*   `__str__`: String representation for users.
*   `__repr__`: String representation for developers (debugging).
*   `__len__`: Custom length behavior.
*   `__getitem__`: Allows indexing logic (crucial for custom Datasets).
*   `__call__`: Makes an instance callable like a function (used extensively in PyTorch/Keras).
