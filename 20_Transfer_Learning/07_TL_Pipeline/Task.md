# Task: Learning Rate Scheduler

## Objective
Design a \"One-Cycle\" warmup.

## Concept
If you start training with High LR on a pre-trained model, the first few gradients might be huge and \"shatter\" the delicate pre-trained weights.
**Solution**: Warmup. Start LR at 0, slowly go up to Max, then go down.

## Task
1.  Define a schedule for 10 epochs.
2.  Epoch 1: LR = $1e-5$ (Warmup).
3.  Epoch 2-5: LR = $1e-3$ (Training).
4.  Epoch 6-10: LR = $1e-4$ (Cooldown/Annealing).

## Question
Why do we lower the LR at the end? (To settle into the minimum valley).
