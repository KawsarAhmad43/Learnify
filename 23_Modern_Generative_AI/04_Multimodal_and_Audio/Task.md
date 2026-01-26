# Task: Contrastive Loss

## Objective
Understand positive/negative pairs.

## Setup
*   Batch of 3 images: [Img1, Img2, Img3].
*   Batch of 3 texts: [Txt1, Txt2, Txt3].
*   Img1 matches Txt1.

## Task
1.  Calculate Similarity Matrix ($3 \times 3$).
2.  The diagonal elements $(1,1), (2,2), (3,3)$ are **Positive Pairs**. We want to maximize these.
3.  The off-diagonal elements $(1,2), (1,3)...$ are **Negative Pairs**. We want to minimize these.
4.  If Batch Size is 100, how many negative pairs does each image have?
    *   Answer: 99.

## Question
Why does CLIP require massive batch sizes (e.g., 32,000)?
*   Answer: Larger batches mean harder negative samples. If you only compare \"Dog\" vs \"Cat\", it's easy. If you compare \"Golden Retriever\" vs \"Labrador\" vs \"Cocker Spaniel\" in a huge batch, the model learns fine-grained features.
