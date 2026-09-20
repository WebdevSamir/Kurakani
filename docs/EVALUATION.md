# Retrieval Evaluation

Kurakani evaluates retrieval independently from generation so that retrieval failures are measurable before an LLM is introduced.

## Query case format

Each evaluation case contains:

- `query_id`
- `query`
- `relevant_chunk_ids`
- optional graded relevance labels

The current metric set is:

- Recall@K
- Precision@K
- MRR
- nDCG@K

These metrics are deliberately retrieval-focused. They do not establish answer faithfulness or overall RAG quality.

## Dense baseline

`DenseRetriever` is an optional adapter backed by Sentence Transformers. The default model is a small, practical baseline, not a claim of state-of-the-art performance.

Install the optional dependency with:

```bash
pip install -e '.[dense]'
```

For every reported experiment, record the exact embedding model, corpus, chunking configuration, top-k, metric definition, and software version.

## Experimental sequence

1. Validate metric implementations on small deterministic fixtures.
2. Run BM25 and dense retrieval on the same qrels.
3. Compare retrieval metrics at the same K values.
4. Add hybrid retrieval only after the individual baselines are measured.
5. Keep dataset-specific results separate from claims about general retrieval performance.

## Benchmark plan

BEIR provides a heterogeneous IR benchmark framework for comparing retrieval methods across datasets. HotpotQA can test multi-hop evidence retrieval, while MIRACL is useful for multilingual retrieval experiments.

Large external datasets should not be committed to the repository. Store dataset provenance, version, preprocessing, and download instructions instead.
