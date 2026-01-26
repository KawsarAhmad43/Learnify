# Task: Mode Collapse

## Objective
Identify failure states.

## Setup
*   Training Data: 50% photos of Cats, 50% photos of Dogs.
*   Ideally, Generator produces 50/50.

## Task
1.  **Scenario A**: G generates only Cats.
    *   Discriminator learns: \"If it looks like a Dog, it's REAL. If it looks like a Cat, I have to check closely.\"
    *   This is okay initially.
2.  **Scenario B (Collapse)**: G generates ONE specific white cat in the exact same pose every time.
    *   Discriminator learns: \"If it's that specific white cat, it's FAKE.\"
    *   G switches to generating ONE specific black dog.
    *   Discriminator switches to block black dogs.
    *   Cycle continues.

## Question
How do we detect this?
*   Answer: While standard metrics (Loss) might look stable, the \"Diversity Score\" of the generated batch will drop to near zero. (Variance of output batch is low).
