# Task: Elo Rating

## Objective
Ranking Models.

## Setup
*   Model A vs Model B.
*   Users prefer A 60% of the time.

## Task
1.  Assume ELO formula: $E_A = \frac{1}{1 + 10^{(R_B - R_A)/400}}$.
2.  If A wins 60% ($E_A = 0.6$), what is determination of score difference?
    *   $0.6 = \frac{1}{1 + X}$.
    *   $1 + X = 1.66$. $X = 0.66$.
    *   $10^{\Delta R / 400} = 0.66$ is wrong direction. (Lower X means higher expected win for A).
    *   Let's approximate: A 60% win rate implies roughly a +70 point ELO advantage.

## Question
Why do leaderboards (LMSYS Chatbot Arena) rely on pairwise battles?
*   Answer: Because absolute evaluation (\"Score this on 1-10\") is subjective and noisy. Relative evaluation (\"Which is better?\") is much more consistent across humans.
