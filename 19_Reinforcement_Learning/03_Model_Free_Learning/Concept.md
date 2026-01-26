# Model Free Learning

## 1. What if you DON'T know the rules?
In GridWorld, we knew that "Right" takes you to "State X". In the real world, we don't know the physics (The Model).
*   **Model-Based**: Planning (Value Iteration). Needs $P(s'|s,a)$.
*   **Model-Free**: Learning by Trial and Error (Monte Carlo, Q-Learning).

## 2. Monte Carlo Methods
Ideally, we play an entire Episode until Game Over.
1.  Play: State A -> B -> C -> Win (+100).
2.  Reverse:
    *   C got +100.
    *   B led to C, so B is good.
    *   A led to B, so A is good.
3.  Average the returns over many games.

## 3. The Limitation
You must finish the game to learn. If the game goes on forever (like the Stock Market), Monte Carlo fails.
