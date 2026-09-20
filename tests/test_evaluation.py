from kurakani.evaluation import (
    QueryCase,
    evaluate_case,
    mean_metrics,
    ndcg_at_k,
)
from kurakani.models import Chunk, RetrievalResult


def result(chunk_id: str, rank: int) -> RetrievalResult:
    return RetrievalResult(
        chunk=Chunk(id=chunk_id, document_id="d", text=chunk_id),
        score=1.0 / rank,
        rank=rank,
    )


def test_metrics_for_first_relevant_result():
    case = QueryCase(
        query_id="q1",
        query="alpha",
        relevant_chunk_ids=frozenset({"a"}),
    )
    metrics = evaluate_case([result("a", 1), result("b", 2)], case, k=2)

    assert metrics.recall_at_k == 1.0
    assert metrics.precision_at_k == 0.5
    assert metrics.mrr == 1.0
    assert metrics.ndcg_at_k == 1.0


def test_mrr_handles_relevant_result_at_rank_two():
    case = QueryCase(
        query_id="q2",
        query="beta",
        relevant_chunk_ids=frozenset({"b"}),
    )
    metrics = evaluate_case([result("a", 1), result("b", 2)], case, k=2)

    assert metrics.mrr == 0.5


def test_ndcg_uses_graded_relevance():
    results = [result("b", 1), result("a", 2)]
    score = ndcg_at_k(results, {"a": 3, "b": 1}, k=2)
    assert 0 < score < 1


def test_mean_metrics_averages_cases():
    cases = [
        QueryCase("q1", "a", frozenset({"a"})),
        QueryCase("q2", "b", frozenset({"b"})),
    ]
    metrics = [
        evaluate_case([result("a", 1)], cases[0], 1),
        evaluate_case([result("x", 1)], cases[1], 1),
    ]
    mean = mean_metrics(metrics)
    assert mean.recall_at_k == 0.5
    assert mean.mrr == 0.5
