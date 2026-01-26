# Task: Cliff Walking

## Objective
Compare Q-Learning vs SARSA.

## Scenario
A grid. Bottom row is a "Cliff" (-100 reward).
Start at Bottom-Left. Goal at Bottom-Right.
Safe path: Top edge.
Risky path: Bottom edge (shortest, but one slip falls into Cliff).

## Concept
1.  **Q-Learning**: Updates assuming optimal valid action next. It ignores the fact that because of $\epsilon$-greedy, it might randomly jump off the cliff next turn. It learns the **Risky Path** (optimal if $\epsilon=0$).
2.  **SARSA**: Updates using the *actual* next action. If the next action is Random(Jump), it effectively "sees" the fall. It learns the **Safe Path**.

## Task
Draw (on paper or mentally) the path you think each algorithm generates if $\epsilon=0.1$.
*   Why does SARSA stay away from the edge?
*   Why does Q-Learning hug the edge?
