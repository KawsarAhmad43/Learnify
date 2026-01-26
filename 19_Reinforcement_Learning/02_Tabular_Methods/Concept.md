# Tabular Methods (Dynamic Programming)

## 1. Perfect Knowledge
If we know exactly how the world works (we know the map), we can just plan.
*   **Value Function ($V(s)$)**: How good is it to be in state $s$?
    *   Example: Being next to the goal is Good. Being next to a cliff is Bad.

## 2. The Bellman Equation
The value of a state is the Reward you get NOW + the Value of where you end up.
*   $V(s) = \max_a [ R(s, a) + \gamma V(s') ]$
*   "Ideally, I should choose the action $a$ that yields the best sum of immediate reward and future value."

## 3. Value Iteration
1.  Initialize all values to 0.
2.  Loop over every state: Update its value using the Bellman Equation.
3.  Repeat until values stop changing (Convergence).
