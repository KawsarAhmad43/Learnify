# Task: Calculating Savings

## Objective
Quantify why LoRA is popular.

## Setup
*   One Linear Layer: $W$ is $1000 \times 1000$.
*   Full Finetuning: We update all elements of $W$.
*   LoRA: We use Rank $r=4$. $A$ is $1000 \times 4$, $B$ is $4 \times 1000$.

## Task
1.  Calculate total params in $W$.
2.  Calculate total params in $A + B$.
3.  Calculate the ratio (Compression Factor).

## Question
If $W$ takes 4MB of RAM (float32), how small is the LoRA adapter?
