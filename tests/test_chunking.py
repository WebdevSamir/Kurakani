from kurakani.chunking import chunk_document
from kurakani.models import Document


def test_chunking_is_deterministic():
    doc = Document(id="doc-1", text="one two three four five six seven eight nine ten")
    first = chunk_document(doc, max_chars=20, overlap_chars=5)
    second = chunk_document(doc, max_chars=20, overlap_chars=5)

    assert first == second
    assert first[0].id == "doc-1::chunk-0000"


def test_empty_document_returns_no_chunks():
    assert chunk_document(Document(id="empty", text="   ")) == []
