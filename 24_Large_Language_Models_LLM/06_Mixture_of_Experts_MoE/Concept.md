# Mixture of Experts (MoE)

## 1. The Bottleneck of Dense Models
In a Dense model (GPT-3), every token activates 100% of the weights.
*   "The": uses 175B params.
*   "Cat": uses 175B params.
*   This is incredibly inefficient. "The" is a simple word, it doesn't need 175B brains.

## 2. Sparse Architecture
*   Replace the Feed Forward layer (MLP) with **8 smaller MLPs (Experts)**.
*   Add a **Router (Gating Network)**.
*   Input -> Router chooses Top-2 Experts -> Run only those 2 -> Weighted Average Output.

## 3. Mixtral 8x7B
*   Total Params: 47B.
*   Active Params (per token): 13B (Router picks 2 experts of 7B).
*   **Result**: Smart like a 50B model, Fast like a 13B model.

## 4. Load Balancing
If Expert #1 is the "Grammar Expert", it gets overworked. Expert #8 (Quantum Physics) is lazy.
We add a **Load Balancing Loss** to force the router to distribute work evenly.
