# The Modern Deployment Pipeline

## 1. The Cycle of Models
Models don't just exist. They evolve.
1.  **Pre-training (The Beast)**: Train a Llama-70B on 1 Trillion tokens (SSL). Cost: \$5,000,000.
2.  **Fine-Tuning (The Expert)**: Finetune it on "Medical Journals" using LoRA. Cost: \$500.
3.  **Distillation (The Product)**: Distill the Medical Expert into a Llama-1B student. Cost: \$1,000.
4.  **Quantization (The Edge)**: Convert the 1B model to 4-bit integer weights. Cost: \$0.
5.  **Deployment**: Run on a doctor's iPad.

## 2. Model Cards
In this pipeline, it is CRITICAL to document the lineage.
*   **Parent**: Meta-Llama-3-70B.
*   **Data**: PubMed 2024.
*   **Method**: LoRA (Rank 64) -> Distillation (T=2.0).
*   **Limitations**: "Do not use for prescriptions."
