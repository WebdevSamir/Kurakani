# Kurakani

> **An experimental framework for adaptive, evidence-grounded conversational AI.**

Kurakani is a research-oriented Retrieval-Augmented Generation (RAG) project. The goal is not simply to build another chatbot, but to create a reproducible platform for studying **when to retrieve, how to retrieve, how to detect weak evidence, how to verify generated answers, and how to measure the quality/efficiency trade-offs of different RAG architectures**.

**Status:** 🟡 Baseline implementation — deterministic chunking and BM25 retrieval are now in place.

## Research question

> Can an adaptive, evidence-grounded retrieval architecture dynamically select retrieval strategies and verification actions based on query characteristics while improving answer faithfulness and retrieval efficiency?

This is a research hypothesis, not a claim of an established result.

## Why Kurakani?

A fixed RAG pipeline often looks like:

~~~text
query → retrieve top-k → generate answer
~~~

Kurakani is intended to investigate a more explicit decision process:

~~~text
query
  ↓
query understanding
  ↓
retrieval routing
  ├── dense
  ├── sparse
  ├── hybrid
  └── graph
  ↓
reranking / filtering
  ↓
evidence quality assessment
  ├── sufficient → generation
  └── insufficient → corrective retrieval
  ↓
answer generation
  ↓
verification + provenance
  ↓
answer + evidence + evaluation trace
~~~

## Research directions

- Dense and sparse retrieval
- Hybrid retrieval
- Reranking
- Query-adaptive retrieval
- Retrieval-quality estimation
- Corrective retrieval
- Graph-enhanced retrieval
- Evidence provenance
- Answer verification
- RAG evaluation and error analysis
- Quality vs. latency/token-cost trade-offs

## Planned experimental baselines

| System | Purpose |
|---|---|
| No-retrieval LLM | Reference point where appropriate |
| Dense RAG | Basic semantic retrieval baseline |
| Sparse/BM25 RAG | Lexical retrieval baseline |
| Hybrid RAG | Dense + sparse retrieval |
| Hybrid + reranker | Evidence ordering/filtering |
| Adaptive RAG | Query-dependent retrieval |
| Adaptive + quality gate | Retrieval failure detection |
| Graph-enhanced adaptive RAG | Relational/multi-hop retrieval |

The final comparison set will be determined by the corpus, models, and reproducibility constraints.

## Evaluation

### Retrieval
- Recall@K
- Precision@K
- MRR
- nDCG
- context relevance

### Generation / grounding
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
- token usage
- estimated inference cost

The project deliberately separates retrieval evaluation from generation evaluation because a good final answer can hide poor retrieval and a poor answer can result from otherwise good evidence.

## Current implementation

The first reproducible retrieval baseline lives under `src/kurakani/`. It intentionally uses a dependency-light BM25 implementation before introducing model-specific dense retrieval or generation. See `docs/BASELINE.md`.

## Research documentation

- RESEARCH.md — research question, hypotheses, architecture, and methodology
- EXPERIMENTS.md — experiment protocol and planned experiment sequence
- docs/LITERATURE.md — living literature review
- research/experiment-log/ — reproducible experiment records

## Literature foundation

Kurakani is informed by work on foundational RAG, adaptive/self-reflective retrieval, corrective retrieval, graph-based RAG, and fine-grained RAG evaluation.

Key starting points:

- Lewis et al. — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
- Asai et al. — Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection
- Yan et al. — Corrective Retrieval Augmented Generation
- Han et al. — Retrieval-Augmented Generation with Graphs (GraphRAG)
- Ru et al. — RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation

See docs/LITERATURE.md for the research map and references.

## Research principles

1. **Baseline first.** Every proposed improvement needs a meaningful comparison.
2. **Measure components separately.** Retrieval, generation, grounding, and efficiency should not be collapsed into one number.
3. **Record exact configurations.** Models, prompts, chunking, top-k, datasets, corpus versions, and commits must be traceable.
4. **Run ablations.** Complexity is not evidence of contribution.
5. **Keep negative results.** Failed hypotheses are part of the research record.
6. **Do not claim novelty early.** A paper contribution must emerge from reproducible evidence.

## Repository strategy

GitHub is the shared source of truth for work across development branches and separate research conversations.

Suggested branch pattern:

~~~text
main
├── research/foundation
├── research/baseline-rag
├── research/hybrid-retrieval
├── research/adaptive-retrieval
├── research/graph-rag
├── research/evaluation
└── feature/*
~~~

Every research branch should leave enough documentation for another researcher to reproduce and understand the work.

## Roadmap

### Phase 0 — Foundation
- [x] Initialize research repository
- [x] Define research question
- [x] Define hypotheses
- [x] Define experimental protocol
- [x] Establish literature map

### Phase 1 — Baseline RAG
- [x] Inspect implementation requirements
- [x] Build deterministic ingestion/chunking foundation
- [x] Implement deterministic BM25 retrieval baseline
- [x] Add automated tests
- [ ] Implement dense retrieval
- [ ] Implement baseline generation
- [ ] Add tracing

### Phase 2 — Retrieval
- [ ] BM25/sparse retrieval
- [ ] Hybrid retrieval
- [ ] Reranking
- [ ] Retrieval evaluation dataset

### Phase 3 — Adaptive system
- [ ] Query classification/features
- [ ] Retrieval router
- [ ] Retrieval-quality gate
- [ ] Corrective retrieval
- [ ] Efficiency tracking

### Phase 4 — Graph-enhanced retrieval
- [ ] Entity/relationship extraction
- [ ] Graph representation
- [ ] Graph retrieval
- [ ] Multi-hop benchmark

### Phase 5 — Evaluation
- [ ] Automated evaluation harness
- [ ] Human evaluation protocol
- [ ] Error taxonomy
- [ ] Ablation framework
- [ ] Statistical analysis

### Phase 6 — Research output
- [ ] Consolidate results
- [ ] Identify actual contribution
- [ ] Reproduce strongest experiments
- [ ] Prepare paper draft
- [ ] Release reproducibility artifacts

## Current research warning

Kurakani is **not yet a validated research contribution**. The current repository establishes the research framework; implementation and empirical evaluation are required before any claim about superiority, novelty, or publication readiness can be justified.

## License

License will be selected before the first public research release.
