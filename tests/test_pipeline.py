from kurakani.models import Document
from kurakani.pipeline import BaselineRAG


def test_baseline_pipeline_retrieves_evidence():
    system = BaselineRAG(
        [
            Document(id="d1", text="Kathmandu is the capital of Nepal."),
            Document(id="d2", text="Paris is the capital of France."),
        ]
    )

    response = system.answer_context("What is the capital of Nepal?", top_k=1)

    assert response.retrieved
    assert response.retrieved[0].chunk.document_id == "d1"
