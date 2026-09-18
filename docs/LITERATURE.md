# Literature Review

This is a living literature map. Papers are grouped by the problem they help us understand rather than treated as features to copy.

## 1. Foundational RAG

### Lewis et al. — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
Introduced the widely used RAG formulation that combines parametric generation with retrieved non-parametric memory.

**Why it matters to Kurakani:** establishes the baseline architecture against which later retrieval and generation strategies can be compared.

Reference: https://arxiv.org/abs/2005.11401

## 2. Adaptive retrieval and self-reflection

### Self-RAG — Asai et al.
Self-RAG investigates adaptive retrieval and self-reflection, addressing the weakness of indiscriminately retrieving a fixed number of passages for every query.

**Kurakani relevance:** motivates the query-adaptive retrieval and verification experiments.

Reference: https://arxiv.org/abs/2310.11511

## 3. Corrective retrieval

### Corrective Retrieval-Augmented Generation (CRAG) — Yan et al.
CRAG introduces retrieval evaluation and corrective actions when retrieved evidence is judged inadequate.

**Kurakani relevance:** motivates an explicit evidence-quality gate and corrective retrieval experiment.

Reference: https://arxiv.org/abs/2401.15884

## 4. Graph-based RAG

### GraphRAG — Han et al.
The GraphRAG literature studies the use of graph-structured information for retrieval-augmented generation, particularly where relational structure matters.

**Kurakani relevance:** motivates a controlled graph-enhanced retrieval experiment rather than assuming graphs improve every query.

Reference: https://arxiv.org/abs/2501.00309

## 5. RAG evaluation

### RAGChecker — Ru et al.
RAGChecker proposes fine-grained diagnostics for retrieval and generation and emphasizes the difficulty of evaluating modular RAG systems.

**Kurakani relevance:** supports separating retrieval metrics from generation/grounding metrics and performing error analysis.

Reference: https://arxiv.org/abs/2408.08067

## Evaluation philosophy

The literature suggests that a single end-to-end score is insufficient for understanding RAG behavior. Kurakani therefore treats the following as separate dimensions:

- retrieval quality
- context quality
- answer correctness
- faithfulness
- evidence/citation quality
- efficiency

## Literature gaps to investigate

These are research questions for investigation, not established claims:

1. How should a router decide between dense, sparse, hybrid, and graph retrieval?
2. Can retrieval-quality estimation be made cheap enough to improve overall efficiency?
3. When does graph retrieval help enough to justify its additional complexity?
4. Can provenance be used as an active verification signal rather than only a display feature?
5. Can adaptive retrieval improve grounding while reducing unnecessary retrieval calls?
6. How robust is the routing policy across domains and query types?

## Important distinction

Kurakani should not claim novelty merely because it combines known components.

Novelty may instead emerge from:

- a new routing policy,
- a new retrieval-quality signal,
- a new evidence verification mechanism,
- a new efficiency/quality objective,
- a new benchmark or dataset,
- or a strong empirical finding about when particular retrieval strategies work.

That distinction should guide the research from the beginning.
