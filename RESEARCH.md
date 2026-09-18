# Kurakani Research Program

## Research status

**Stage:** Research foundation / architecture definition  
**Primary area:** Retrieval-Augmented Generation (RAG), adaptive retrieval, evidence grounding, and evaluation.

## Problem

A basic RAG pipeline usually performs a fixed retrieval step and sends the retrieved context to an LLM. This is useful, but it leaves several research questions open:

- When is retrieval actually necessary?
- Which retrieval strategy should be used for a given query?
- How should poor retrieval be detected and corrected?
- How can multi-hop or relational questions be handled?
- How can answers be tied to verifiable evidence?
- How should retrieval and generation quality be evaluated independently?
- Can quality be improved without increasing unnecessary retrieval and generation cost?

Kurakani will be developed as an experimental framework for answering these questions empirically.

## Working research question

> Can an adaptive, evidence-grounded retrieval architecture dynamically select retrieval strategies and verification actions based on query characteristics while improving answer faithfulness and retrieval efficiency?

This is a working question, not a claim that the system already achieves these improvements.

## Hypotheses

### H1 — Hybrid retrieval
Combining lexical and semantic retrieval can improve retrieval coverage over a dense-only baseline on queries containing exact terminology, entities, or uncommon phrases.

### H2 — Query-adaptive retrieval
Selecting retrieval behavior according to query characteristics can improve answer quality over a fixed retrieval policy.

### H3 — Retrieval quality gating
A retrieval-quality assessment step can reduce unsupported answers caused by poor retrieved evidence.

### H4 — Graph-enhanced retrieval
Relational or multi-hop questions may benefit from graph-aware retrieval compared with flat passage retrieval.

### H5 — Evidence verification
Explicit evidence/provenance and answer verification can improve measurable grounding and citation accuracy.

### H6 — Efficiency
An adaptive system can avoid unnecessary retrieval or model calls for queries that do not require them.

## Experimental principle

Every proposed improvement must be evaluated against a defined baseline.

We will avoid presenting architectural complexity as a research contribution by itself. A contribution must be supported by:

1. a clearly stated hypothesis,
2. a reproducible implementation,
3. a defined dataset or benchmark,
4. controlled baselines,
5. quantitative metrics,
6. ablations,
7. error analysis, and
8. reproducible experiment records.

## Target architecture

```
User Query
    |
    v
Query Understanding
    |
    v
Retrieval Router
    |
    +---- Dense Retrieval
    +---- Sparse / BM25 Retrieval
    +---- Hybrid Retrieval
    +---- Graph Retrieval
    +---- External Retrieval (optional)
    |
    v
Candidate Evidence
    |
    v
Reranking / Filtering
    |
    v
Evidence Quality Gate
    |
    +---- adequate evidence ----> Generation
    |
    +---- inadequate evidence --> Corrective Retrieval
                                      |
                                      v
                                   Evidence
    |
    v
Answer Generation
    |
    v
Grounding / Verification
    |
    v
Answer + Evidence + Provenance
    |
    v
Evaluation / Tracing
```

## Planned baselines

1. No-retrieval LLM baseline where appropriate.
2. Dense-vector RAG.
3. Sparse/BM25 RAG.
4. Hybrid RAG.
5. Hybrid + reranking.
6. Adaptive retrieval.
7. Adaptive retrieval + quality gate.
8. Graph-enhanced adaptive retrieval.

The final baseline set will depend on the actual corpus and implementation constraints.

## Evaluation dimensions

### Retrieval

- Recall@K
- Precision@K
- MRR
- nDCG
- context relevance

### Generation

- answer correctness
- faithfulness
- answer relevance
- citation/evidence accuracy
- unsupported-claim rate

### System

- end-to-end latency
- retrieval latency
- number of retrieval calls
- number of LLM calls
- input/output token usage
- estimated inference cost

### Research quality

- reproducibility
- ablation completeness
- error categories
- statistical uncertainty where appropriate

## Experimental discipline

Do not compare systems using different datasets, prompts, models, retrieval depths, or evaluation procedures without recording the differences.

Every experiment should record:

- experiment ID
- branch/commit
- dataset version
- corpus version
- embedding model
- reranker
- generator model
- retrieval configuration
- top-k
- chunking configuration
- prompt version
- evaluation metrics
- results
- observations
- limitations

## Non-goals

Kurakani is not initially intended to:

- claim a new foundation model,
- reproduce an entire commercial search stack,
- optimize every RAG technique simultaneously,
- claim publication novelty before experiments establish it.

## Publication path

A possible paper contribution could emerge from the intersection of:

**adaptive retrieval + retrieval-quality estimation + evidence verification + efficiency-aware routing**

but this will remain a hypothesis until supported by experiments.

The eventual paper should be written from measured results, not from the architecture alone.
