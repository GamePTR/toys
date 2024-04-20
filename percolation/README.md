> This document is brief, more clear information is in the pdf.

The pdf is from [course algorithm](https://www.coursera.org/learn/algorithms-part1)'s week one union find.

## Problem description:

### A model for many physical systems:
- N-by-N grid of sites.
- Each site is open with probability p (or blocked with probability 1 – p).
- System percolates iff top and bottom are connected by open sites.
Such as electricity conductor, fluid flow and social interaction.

### What is the middle vacancy probability p?(pdf page 51)
When N is large, theory guarantees a sharp threshold p*:
- p > p*: almost certainly percolates.
- p < p*: almost certainly does not percolate.

## Method: Monte Carlo simulation
- Initialize N-by-N whole grid to be blocked.
- Declare random sites open until top connected to bottom.
- Vacancy percentage estimates p*.

## Usage
```
git clone 
```
### Visualization

### simulation

