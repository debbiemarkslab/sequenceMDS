# sequenceMDS: Biological sequence visualization that preserves mutation distance.

## The approach
For a given set of D datapoints of M-dimensions, MDS yields a set of D embedded points in N-dimensions <br>
s.t. distances between embedded points preserve the distances between the original datapoints.

Here, we define hamming distance as the datapoint distance, and Euclidean distance as the embedding distance. <br>
Therefore, our 2-D embedding gives Euclidean distances between points that approximate the hamming distance between the corresponding sequences.

1. Create a multiple sequence alignment
2. Calculate all-vs-all hamming distances between the aligned sequences
3. Apply MDS to find a set of 2-D points that match hamming distances
4. Visualize the 2-D embedding

## Get started
The method is very simple and invokes existing modules, there is no install for this repo. <br>
Instead, look at ```sequenceMDS example 1.ipynb``` to see what commands to run.

For creating multiple sequence alignments, we recommend installing MAFFT.
For computing all-vs-all hamming distances, we include several functions in ```hamming.py```.
For MDS calculation, install sklearn.


## Disclaimers
1. MDS does not find a perfect match of 2-D distance to provided distance. <br>
However, for a well-specified hamming matrix, it is typically accurate enough to serve for qualitative interpretation and for rule-of-thumb comparisons.


2. The MDS algorithm will return slightly different solutions unless a random seed is specified. <br>
The biggest difference is typically the global rotation.

3. Computing hamming distance from a multiple sequence alignment, rather than all-vs-all pairwise sequence alignments, is an approximation to save compute time. <br>
With a sufficiently accurate multiple sequence alignment this is typically sufficient for visualization. <br>
For sequences without a coherent common alignment, such as sequences from separate protein families, you may want to compute all-vs-all alignments e.g. using Smith-Waterman.
