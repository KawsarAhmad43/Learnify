# Task: The Budget

## Objective
Epsilon Decay.

## Setup
*   Every time you query the private database (or train a batch), you \"spend\" some privacy budget (epsilon).
*   If you query it too many times, epsilon becomes infinite, and privacy is lost (The Law of Large Numbers filters out the noise).

## Task
1.  You have a budget of $\epsilon = 5.0$ for the year.
2.  Each query costs $\epsilon = 0.1$.
3.  You can only ask 50 questions.
4.  **Strategy**:
    *   Train for fewer epochs.
    *   Use larger batch sizes (One query covers more people, less privacy leakage per person).

## Question
What is 'Local DP' vs 'Global DP'?
*   Answer:
    *   **Local DP**: Noise is added on the Client's phone. The Server never sees the true data. (Google RAPPOR).
    *   **Global DP**: Server sees true data, adds noise before publishing results. (Census). Local DP is stronger but destroys utility more (Noise scales with N).
