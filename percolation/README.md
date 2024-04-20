# Precolation

> This document is brief, more clear information is in the pdf.

The pdf is copied from [course algorithm](https://www.coursera.org/learn/algorithms-part1)'s week one union find.

## Problem description:

A model for many physical systems:

- N-by-N grid of sites.
- Each site is open with probability p (or blocked with probability 1 – p).
- System percolates iff top and bottom are connected by open sites.

> Aplication example: electricity conductor, fluid flow and social interaction.

What is the mutational vacancy probability p? (pdf page 51) When N is large, theory guarantees a sharp threshold p*:
- p > p*: almost certainly percolates.
- p < p*: almost certainly does not percolate.

## Method
### Monte Carlo simulation

- Initialize N-by-N whole grid to be blocked.
- Declare random sites open until top connected to bottom.
- Vacancy percentage estimates p*.

### Union find

- Each time open a blocked grid, union with the neighbers iff neighers are also open

## Usage
```
git clone https://github.com/GamePTR/toys.git
```
### Visualization
```
cd toys/percolation
python visualization.py
```
## TODO (Wellcome to your participation)
- friendly user entry(more optional)
- entry that repeatedly simulate without visualization and compute the average p
