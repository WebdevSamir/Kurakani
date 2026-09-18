import argparse

from .models import Document
from .pipeline import BaselineRAG


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the Kurakani baseline retriever.")
    parser.add_argument("query", help="Question/query to retrieve evidence for.")
    args = parser.parse_args()

    documents = [
        Document(
            id="sample-1",
            text=(
                "Kurakani is a research prototype for retrieval-augmented "
                "generation. The project studies retrieval quality, adaptive "
                "routing, evidence grounding, and evaluation."
            ),
        ),
        Document(
            id="sample-2",
            text=(
                "A baseline RAG system retrieves relevant passages and passes "
                "them to a language model. Retrieval and generation should be "
                "evaluated separately."
            ),
        ),
    ]

    system = BaselineRAG(documents)
    response = system.answer_context(args.query)

    print(f"Query: {response.query}\n")
    for result in response.retrieved:
        print(f"[{result.rank}] score={result.score:.4f} {result.chunk.id}")
        print(result.chunk.text)
        print()


if __name__ == "__main__":
    main()
