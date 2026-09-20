from kurakani.models import Chunk
from kurakani.retrieval import BM25Retriever


def test_bm25_returns_relevant_chunk_first():
    chunks = [
        Chunk(id="a", document_id="d1", text="Python is a programming language."),
        Chunk(id="b", document_id="d2", text="Bananas are a fruit."),
        Chunk(id="c", document_id="d3", text="Python can be used for machine learning."),
    ]

    results = BM25Retriever(chunks).retrieve("Python programming", top_k=2)

    assert results[0].chunk.id == "a"
    assert results[0].score > 0


def test_retrieval_is_deterministic_for_ties():
    chunks = [
        Chunk(id="a", document_id="d1", text="alpha beta"),
        Chunk(id="b", document_id="d2", text="alpha beta"),
    ]

    results = BM25Retriever(chunks).retrieve("alpha", top_k=2)

    assert [r.chunk.id for r in results] == ["a", "b"]
