# Task: Signal to Noise Ratio

## Objective
Calculate how much signal is left at step $T$.

## Formula
$\bar{\alpha}_t$ (Alpha CumProd) determines signal strength.
$x_t = \sqrt{\bar{\alpha}_t} x_0 + \sqrt{1 - \bar{\alpha}_t} \epsilon$.

## Task
1.  Assume $\bar{\alpha}_T = 0.006$. (Common value for T=1000).
2.  Calculate Signal Coefficient: $\sqrt{0.006} \approx 0.077$.
3.  Calculate Noise Coefficient: $\sqrt{1 - 0.006} = \sqrt{0.994} \approx 0.997$.

## Question
At step T, is the image mostly Signal or mostly Noise?
*   Answer: Mostly Noise (99.7%). The signal is barely a whisper. The model's job is to latch onto that 7% signal and amplify it.
