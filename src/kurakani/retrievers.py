from __future__ import annotations

from typing import Protocol, Sequence

from .models import Chunk, RetrievalResult


class Retriever(Protocol):
    def retrieve(self, query: str, top_k: int = 5) -> list[RetrievalResult]:
        ...


class DenseRetriever:
    """Optional sentence-transformers dense retriever.

    The dependency is intentionally optional so the core research framework
    remains lightweight. Exact model name and configuration must be recorded
    for reproducible experiments.
    """

    def __init__(
        self,
        chunks: Sequence[Chunk],
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
    ):
        try:
            from sentence_transformers import SentenceTransformer
        except ImportError as exc:
            raise ImportError(
                "DenseRetriever requires the optional 'dense' dependency. "
                "Install with: pip install -e '.[dense]'"
            ) from exc

        self.chunks = list(chunks)
        self.model_name = model_name
        self._model = SentenceTransformer(model_name)
        self._embeddings = self._model.encode(
            [chunk.text for chunk in self.chunks],
            normalize_embeddings=True,
        )

    def retrieve(self, query: str, top_k: int = 5) -> list[RetrievalResult]:
        if top_k <= 0:
            raise ValueError("top_k must be positive")
        if not self.chunks:
            return []

        query_embedding = self._model.encode(
            [query],
            normalize_embeddings=True,
        )[0]
        scores = self._embeddings @ query_embedding
        ranked = sorted(
            range(len(self.chunks)),
            key=lambda index: (-float(scores[index]), index),
        )

        return [
            RetrievalResult(
                chunk=self.chunks[index],
                score=float(scores[index]),
                rank=rank,
            )
            for rank, index in enumerate(ranked[:top_k], start=1)
        ]
