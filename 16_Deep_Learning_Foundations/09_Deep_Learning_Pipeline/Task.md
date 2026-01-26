# Task: Refactor into a Class

## Objective
Take the spaghetti code below and wrap it into a `Classifier` class.

## Spaghetti Code
```python
w = 0.5
b = 0.1
def train(x, y):
    global w, b
    # ... update w, b
def predict(x):
    return w*x + b
```

## Task
1.  Create `class Classifier`.
2.  Store `w` and `b` as `self.w`, `self.b`.
3.  Add `fit(X, y)` method.
4.  Add `predict(X)` method.
5.  Instantiate it and call `model.fit()` then `model.predict()`.
