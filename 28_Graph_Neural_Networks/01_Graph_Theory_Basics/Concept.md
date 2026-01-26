# Graph Theory Basics

## 1. Why Graphs?
*   Images are Grids (Euclidean).
*   Text is Sequence (Euclidean-ish).
*   Molecules, Social Networks, Road Maps are **Graphs** (Non-Euclidean). Arbitrary connections.

## 2. Components
*   $V$: Vertices (Nodes). E.g., People.
*   $E$: Edges (Links). E.g., Friendships.
*   $A$: Adjacency Matrix ($N \times N$). 1 if connected, 0 if not.
*   $X$: Node Features ($N \times D$). e.g., Person's Age, Name.

## 3. The Challenge
Standard Neural Nets (CNNs) need a fixed size input.
*   Image: Always $224 \times 224$ pixels.
*   Graph: My friends list is length 5. Your friends list is length 500.
*   How do we process variable-sized topology?
