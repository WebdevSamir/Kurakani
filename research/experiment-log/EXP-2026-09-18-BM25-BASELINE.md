# EXP-2026-09-18-BM25-BASELINE

## Objective

Establish a deterministic, dependency-light lexical retrieval baseline for Kurakani.

## Hypothesis

A transparent BM25 implementation provides a reproducible reference point against which later dense, hybrid, reranked, and adaptive retrieval systems can be compared.

## Scope

This experiment validates the software pipeline only. It does **not** establish that BM25 is superior to dense retrieval or that the full Kurakani research question has been answered.

## Configuration

- Retriever: BM25
- k1: 1.5
- b: 0.75
- Chunking: deterministic character windows
- Default chunk size: 800 characters
- Default top-k: 5
- Dependencies: Python standard library for core implementation

## Acceptance criteria

- deterministic tokenization
- deterministic chunk IDs
- deterministic retrieval ordering
- unit tests for chunking
- unit tests for retrieval
- end-to-end retrieval pipeline test

## Result

Pending execution in CI/local environment.

## Next experiment

Build a proper evaluation harness and a dense retrieval adapter. Compare both on a controlled retrieval dataset before introducing hybrid retrieval.
