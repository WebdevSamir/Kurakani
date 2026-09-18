import re
from .models import Chunk, Document


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\\s+", " ", text).strip()


def chunk_document(
    document: Document,
    max_chars: int = 800,
    overlap_chars: int = 120,
) -> list[Chunk]:
    """Create deterministic character-window chunks.

    The baseline deliberately uses a simple deterministic chunker so later
    chunking strategies can be compared against a stable reference.
    """
    if max_chars <= 0:
        raise ValueError("max_chars must be positive")
    if overlap_chars < 0 or overlap_chars >= max_chars:
        raise ValueError("overlap_chars must be >= 0 and < max_chars")

    text = normalize_whitespace(document.text)
    if not text:
        return []

    chunks: list[Chunk] = []
    start = 0
    index = 0

    while start < len(text):
        end = min(start + max_chars, len(text))

        if end < len(text):
            boundary = text.rfind(" ", start, end)
            if boundary > start + max_chars // 2:
                end = boundary

        piece = text[start:end].strip()
        if piece:
            chunks.append(
                Chunk(
                    id=f"{document.id}::chunk-{index:04d}",
                    document_id=document.id,
                    text=piece,
                    metadata={**document.metadata, "chunk_index": index},
                )
            )
            index += 1

        if end >= len(text):
            break

        next_start = max(start + 1, end - overlap_chars)
        start = next_start

    return chunks
