from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable

from .models import RetrievalResult


@dataclass(frozen=True)
class QueryCase:
    query_id: str
    query: str
    relevant_chunk_ids: frozenset[str]
    graded_relevance: dict[str, int] | None = None


@dataclass(frozen=True)
class RetrievalMetrics:
    recall_at_k: float
    precision_at_k: float
    mrr: float
    ndcg_at_k: float


def recall_at_k(results: list[RetrievalResult], relevant: set[str], k: int) -> float:
    if not relevant:
        return 0.0
    retrieved = {r.chunk.id for r in results[:k]}
    return len(retrieved & relevant) / len(relevant)


def precision_at_k(results: list[RetrievalResult], relevant: set[str], k: int) -> float:
    if k <= 0:
        raise ValueError("k must be positive")
    retrieved = results[:k]
    if not retrieved:
        return 0.0
    return sum(r.chunk.id in relevant for r in retrieved) / len(retrieved)


def reciprocal_rank(results: list[RetrievalResult], relevant: set[str]) -> float:
    for result in results:
        if result.chunk.id in relevant:
            return 1.0 / result.rank
    return 0.0


def ndcg_at_k(
    results: list[RetrievalResult],
    graded_relevance: dict[str, int],
    k: int,
) -> float:
    def dcg(gains: Iterable[int]) -> float:
        return sum(g / math.log2(index + 2) for index, g in enumerate(gains))

    predicted = [max(0, graded_relevance.get(r.chunk.id, 0)) for r in results[:k]]
    ideal = sorted(
        (max(0, value) for value in graded_relevance.values()),
        reverse=True,
    )[:k]

    ideal_dcg = dcg(ideal)
    if ideal_dcg == 0:
        return 0.0
    return dcg(predicted) / ideal_dcg


def evaluate_case(
    results: list[RetrievalResult],
    case: QueryCase,
    k: int,
) -> RetrievalMetrics:
    graded = case.graded_relevance or {
        chunk_id: 1 for chunk_id in case.relevant_chunk_ids
    }
    return RetrievalMetrics(
        recall_at_k=recall_at_k(results, set(case.relevant_chunk_ids), k),
        precision_at_k=precision_at_k(results, set(case.relevant_chunk_ids), k),
        mrr=reciprocal_rank(results, set(case.relevant_chunk_ids)),
        ndcg_at_k=ndcg_at_k(results, graded, k),
    )


def mean_metrics(metrics: Iterable[RetrievalMetrics]) -> RetrievalMetrics:
    values = list(metrics)
    if not values:
        raise ValueError("at least one metric result is required")
    n = len(values)
    return RetrievalMetrics(
        recall_at_k=sum(x.recall_at_k for x in values) / n,
        precision_at_k=sum(x.precision_at_k for x in values) / n,
        mrr=sum(x.mrr for x in values) / n,
        ndcg_at_k=sum(x.ndcg_at_k for x in values) / n,
    )
