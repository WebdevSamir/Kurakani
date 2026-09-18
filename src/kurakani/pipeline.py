from dataclasses import dataclass
from .models import Document, RetrievalResult
from .chunking import chunk_document
from .retrieval import BM25Retriever


@dataclass(frozen=True)
class BaselineResponse:
    query: str
    retrieved: list[RetrievalResult]


class BaselineRAG:
    """Retrieval-only baseline used to validate the research pipeline.

    Generation is deliberately not coupled to a provider yet. This lets us
    evaluate ingestion, chunking and retrieval independently before adding
    model-specific behavior.
    """

    def __init__(self, documents: list[Document], max_chars: int = 800):
        chunks = []
        for document in documents:
            chunks.extend(chunk_document(document, max_chars=max_chars))
        self.retriever = BM25Retriever(chunks)

    def retrieve(self, query: str, top_k: int = 5) -> list[RetrievalResult]:
        return self.retriever.retrieve(query, top_k=top_k)

    def answer_context(self, query: str, top_k: int = 5) -> BaselineResponse:
        return BaselineResponse(
            query=query,
            retrieved=self.retrieve(query, top_k=top_k),
        )
