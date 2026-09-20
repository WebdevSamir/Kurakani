from kurakani.models import Chunk, RetrievalResult
from kurakani.retrieval import BM25Retriever


def test_bm25_matches_retriever_protocol_shape():
    chunks = [Chunk(id="a", document_id="d", text="alpha")]
    retriever = BM25Retriever(chunks)

    results = retriever.retrieve("alpha", top_k=1)

    assert isinstance(results[0], RetrievalResult)
    assert results[0].rank == 1
