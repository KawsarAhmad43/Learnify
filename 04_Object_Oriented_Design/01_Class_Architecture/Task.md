# Tasks: OOP in Python

## Task 1: The Shape Hierarchy
1.  Create a base class `Shape` with a method `area()` that returns 0.
2.  Create a subclass `Rectangle` that takes `width` and `height` in `__init__` and overrides `area()`.
3.  Create a subclass `Circle` that takes `radius` and overrides `area()`.
4.  Demonstrate polymorphism: Create a list of different shapes and print their areas in a loop.

## Task 2: Custom Dataset Class
In ML, we often wrap data in classes.
1.  Create a class `SimpleDataset` that takes a list of data points in `__init__`.
2.  Implement `__len__` to return the size of the dataset.
3.  Implement `__getitem__` to allow indexing (e.g., `dataset[0]`).
4.  Bonus: Implement `__repr__` to print "SimpleDataset with N items".

## Task 3: Model Builder
Create a class `Model` that:
1.  Takes a `model_name` and `weights` (list of numbers) in `__init__`.
2.  Has a method `predict(input_val)` that effectively does `input_val * sum(weights)`.
3.  Implement `__call__` so you can do `model(input_val)` instead of `model.predict(input_val)`.
