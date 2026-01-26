# Task: Define Rewards

## Objective
Design a Reward Function for a specific goal.

## Scenario: Parking Assistant
You are training a car to park in a spot.

## Variables
*   $d$: Distance to spot center (0 is perfect).
*   $c$: Collision (True/False).
*   $t$: Time steps taken.

## Task
Write a python function `get_reward(d, c, t)` that:
1.  Punishes collisions heavily (-100).
2.  Punishes time slightly (-1 per step) to encourage speed.
3.  Rewards being close to the spot.
    *   Maybe $10 - d$? Or $1 / (d + 0.1)$?

## Requirements
*   If collision, return -100.
*   Otherwise, return (Close Reward) - 1.

Test it with:
*   Collision=True
*   Distance=0 (Perfect park)
*   Distance=10 (Far away)
