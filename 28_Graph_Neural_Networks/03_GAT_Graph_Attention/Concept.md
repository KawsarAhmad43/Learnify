# Graph Attention Networks (GAT)

## 1. Not All Neighbors are Equal
In GCN, $A_{i,j} = 1$ for all neighbors. You sum them up equally.
But what if one neighbor is my "Boss" and the other is my "Gym Buddy"?
If I'm predicting "Work Performance", I should pay attention to the Boss.
If I'm predicting "Fitness", I should pay attention to the Buddy.

## 2. Attention Mechanism
We learn a dynamic weight $\alpha_{ij}$ which represents the *importance* of node $j$ to node $i$.
*   $\alpha_{ij} = \text{Softmax}( \text{LeakyReLU}( a^T [Wh_i || Wh_j] ) )$.
*   We concatenate features of $i$ and $j$, pass them through a linear layer $a$, and normalize.

## 3. Multi-Head Attention
Just like Transformers!
*   Head 1 focuses on "Work Relationships".
*   Head 2 focuses on "Social Relationships".
*   Concatenate results at the end.
