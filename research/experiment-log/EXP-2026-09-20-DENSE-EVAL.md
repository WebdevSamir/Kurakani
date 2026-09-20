# EXP-2026-09-20-DENSE-EVAL

## Objective

Establish a common retrieval evaluation layer and a pluggable dense-retrieval baseline so BM25 and dense retrieval can be compared under the same query cases.

## Hypothesis

A dense retriever may recover semantically relevant evidence that lexical BM25 misses, but this is an empirical question and is not assumed to hold across datasets or query types.

## Changes

- Added a retriever protocol.
- Added an optional Sentence Transformers dense adapter.
- Added Recall@K, Precision@K, MRR, and nDCG@K.
- Added deterministic metric tests.
- Added documentation for benchmark reproducibility.

## Results

No benchmark results are claimed by this record. The implementation and metric tests are the current milestone; benchmark execution is a separate experiment.

## Next experiment

Run the same qrels through BM25 and dense retrieval, then add hybrid retrieval only if the comparison is informative.
