# Task: Layer Surgery

## Objective
Understand model architecture modification.

## Model: VGG16
*   Features: 5 Blocks of Convolution.
*   Classifier: Linear(4096) -> Linear(4096) -> Linear(1000).

## Task
1.  Assume `vgg.classifier` is a Sequential block with 6 layers (Linear, ReLU, Dropout, Linear, ReLU, Dropout, Linear).
2.  The last layer is at index 6.
3.  Write pseudo-code to replace ONLY the last layer with a layer that outputs 10 classes.

## Code Hint
`model.classifier[6] = nn.Linear(?, ?)`

## Question
What should the `in_features` of this new layer be? (Hint: It must match the output of the previous layer, which is 4096).
