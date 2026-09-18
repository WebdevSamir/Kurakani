import math
import re
from collections import Counter, defaultdict
from .models import Chunk, RetrievalResult


_TOKEN_RE = re.compile(r"[A-Za-z0-9_]+")


def tokenize(text: str) -> list[str]:
    return _TOKEN_RE.findall(text.lower())


class BM25Retriever:
    """Small dependency-free BM25 implementation for the baseline.

    This is intentionally simple and transparent. It is a reference
    implementation, not the final high-performance retriever.
    """

    def __init__(self, chunks: list[Chunk], k1: float = 1.5, b: float = 0.75):
        if k1 <= 0:
            raise ValueError("k1 must be positive")
        if not 0 <= b <= 1:
            raise ValueError("b must be between 0 and 1")

        self.chunks = list(chunks)
        self.k1 = k1
        self.b = b
        self._tokens = [tokenize(c.text) for c in self.chunks]
        self._lengths = [len(tokens) for tokens in self._tokens]
        self._avgdl = sum(self._lengths) / len(self._lengths) if self._lengths else 0.0

        document_frequency: Counter[str] = Counter()
        self._term_frequencies: list[Counter[str]] = []

        for tokens in self._tokens:
            tf = Counter(tokens)
            self._term_frequencies.append(tf)
            document_frequency.update(tf.keys())

        self._idf = {
            term: math.log(1 + (len(self.chunks) - df + 0.5) / (df + 0.5))
            for term, df in document_frequency.items()
        }

    def _score(self, query_terms: list[str], index: int) -> float:
        if not query_terms or not self.chunks:
            return 0.0

        dl = self._lengths[index]
        denominator_length = self._avgdl or 1.0
        tf = self._term_frequencies[index]
        score = 0.0

        for term in query_terms:
            if term not in tf:
                continue
            term_frequency = tf[term]
            numerator = term_frequency * (self.k1 + 1)
            denominator = term_frequency + self.k1 * (
                1 - self.b + self.b * dl / denominator_length
            )
            score += self._idf.get(term, 0.0) * numerator / denominator

        return score

    def retrieve(self, query: str, top_k: int = 5) -> list[RetrievalResult]:
        if top_k <= 0:
            raise ValueError("top_k must be positive")

        query_terms = tokenize(query)
        scored = [
            (self._score(query_terms, index), index)
            for index in range(len(self.chunks))
        ]
        scored.sort(key=lambda item: (-item[0], item[1]))

        results: list[RetrievalResult] = []
        for rank, (score, index) in enumerate(scored[:top_k], start=1):
            results.append(
                RetrievalResult(
                    chunk=self.chunks[index],
                    score=score,
                    rank=rank,
                )
            )
        return results
