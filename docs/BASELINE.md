# Baseline RAG Implementation

## Why this baseline is intentionally small

The first implementation should be easy to inspect and reproduce. A dependency-heavy stack would make it harder to distinguish research effects from infrastructure effects.

The baseline currently contains:

1. deterministic document representation,
2. deterministic character-window chunking,
3. BM25 retrieval,
4. a retrieval-only pipeline,
5. automated unit tests.

Generation is not yet coupled to an LLM provider. This is deliberate: retrieval quality should be measurable independently before generation is introduced.

## Research role

This baseline provides the reference implementation for later experiments:

- dense retrieval
- hybrid retrieval
- reranking
- adaptive routing
- retrieval quality gating
- graph retrieval

## Current limitation

BM25 is lexical retrieval, not semantic retrieval. Therefore this is **not yet the final dense-RAG baseline** described in the research roadmap.

The next implementation step is a pluggable dense-retrieval adapter plus a standardized evaluation harness.

## Dataset strategy

For retrieval benchmarking, we should use established datasets rather than inventing an arbitrary test set.

BEIR is a heterogeneous information-retrieval benchmark containing datasets across multiple tasks and domains, and its authors report BM25 as a robust baseline. https://arxiv.org/abs/2104.08663

For multi-hop research, HotpotQA is useful because it contains questions requiring evidence from multiple documents and provides supporting facts. https://arxiv.org/abs/1809.09600

For multilingual research, MIRACL provides relevance judgments across 18 languages and can become relevant if Kurakani is extended toward multilingual retrieval. https://arxiv.org/abs/2210.09984

We should not mix these datasets casually: each experiment needs a defined task, corpus, query set, and metric.

## Evaluation direction

The current RAG evaluation literature emphasizes separate measurement of retrieval and generation rather than relying on one end-to-end score. https://arxiv.org/abs/2504.14891 and https://arxiv.org/abs/2408.08067

Therefore the next evaluation harness should report at least:

- Recall@K
- MRR
- nDCG where relevance grades are available
- context relevance
- answer correctness
- faithfulness
- latency
- retrieval calls
- token usage once generation is added
