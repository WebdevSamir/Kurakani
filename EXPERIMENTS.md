# Kurakani Experiment Protocol

This document defines how experiments should be recorded so work from different branches and conversations remains synchronized.

## Experiment ID format

Use:

`EXP-YYYY-MM-DD-NAME`

Example:

`EXP-2026-09-18-DENSE-BASELINE`

## Required experiment record

For each experiment, record:

### 1. Objective
What question is being tested?

### 2. Hypothesis
What outcome is expected and why?

### 3. System
Which implementation/branch/commit is being evaluated?

### 4. Dataset
Name, version, size, train/dev/test split if applicable.

### 5. Corpus
Documents, sources, snapshot date, preprocessing.

### 6. Retrieval
- retriever
- embedding model
- sparse method
- top-k
- reranker
- filtering

### 7. Generation
- model
- temperature
- max output tokens
- system prompt version

### 8. Metrics
Report retrieval, generation, and system metrics separately.

### 9. Results
Use a table whenever possible.

### 10. Error analysis
Identify representative failures and categorize them.

### 11. Conclusion
State whether the result supports, weakens, or leaves the hypothesis unresolved.

### 12. Reproducibility
Record the exact commit SHA and configuration.

## Initial experiment sequence

### EXP-01 — Repository and pipeline smoke test
Goal: establish a deterministic minimal pipeline.

### EXP-02 — Dense retrieval baseline
Goal: measure baseline retrieval and generation quality.

### EXP-03 — Sparse retrieval baseline
Goal: measure lexical retrieval independently.

### EXP-04 — Hybrid retrieval
Goal: test whether combining sparse and dense retrieval improves retrieval metrics.

### EXP-05 — Reranking
Goal: test whether reranking improves evidence quality.

### EXP-06 — Query-adaptive routing
Goal: test fixed retrieval against adaptive retrieval.

### EXP-07 — Retrieval quality gate
Goal: test whether poor retrieval can be detected and corrected.

### EXP-08 — Graph-enhanced retrieval
Goal: test graph retrieval on relational and multi-hop questions.

### EXP-09 — Evidence verification
Goal: measure citation/evidence grounding and unsupported claims.

### EXP-10 — Efficiency analysis
Goal: compare quality against latency, retrieval calls, model calls, and token usage.

## Ablation requirements

For any proposed contribution, remove one component at a time.

Example:

- full adaptive system
- without router
- without reranker
- without quality gate
- without graph retrieval
- without verification

The purpose is to determine which components actually matter.

## Result policy

A negative result is valid research.

Do not modify the evaluation procedure after seeing results unless the change is explicitly documented as a new experiment.
