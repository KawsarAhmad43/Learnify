# Task: Payment Gateway

## Objective
Polymorphism.

## Setup
*   You store `PaymentMethod` objects.

## Task
1.  Create a parent class `Payment`.
    *   Method `process(amount)`: Raise NotImplementedError.
2.  Create child classes `CreditCard`, `PayPal`, `Bitcoin`.
    *   `CreditCard.process`: Print "Charging {amount} to Visa...".
    *   `PayPal.process`: Print "Redirecting to PayPal for {amount}...".
3.  **Task**: Create a function `checkout(cart_total, payment_method)`. It should call `payment_method.process(cart_total)`.
4.  Test it with different payment objects.

## Question
What is the 'Diamond Problem'?
*   Answer: Class A. Classes B and C inherit from A. Class D inherits from B and C. If D calls `super().method()`, which one does it call? B or C? Python solves this with Linearization (MRO).
