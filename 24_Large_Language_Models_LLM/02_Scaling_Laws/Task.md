# Task: Compute Budget

## Objective
Allocate resource.

## Constraint
You have enough money for $10^{23}$ FLOPs.
Formula: $C = 6ND$.
Optimal D: $D = 20N$.
Substitute: $C = 6N(20N) = 120N^2$.

## Task
1.  Solve for N (Model Size).
    *   $10^{23} = 120N^2$.
    *   $N^2 = 10^{23} / 120 \approx 8.3 \times 10^{20}$.
    *   $N \approx \sqrt{8.3} \times 10^{10} \approx 2.8 \times 10^{10}$.
2.  Result: $N \approx 28$ Billion Parameters.

## Question
If you have this budget, should you train a 1 Trillion parameter model?
*   Answer: No! It would be severely undertrained (data starved) and perform worse than the 28B model.
