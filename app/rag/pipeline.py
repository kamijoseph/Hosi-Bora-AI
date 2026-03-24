from app.rag.retriever import Retriever
from app.rag.generator import Generator

class RAGPipeline:
    def __init__(self):
        self.retriever = Retriever()
        self.generator = Generator()

    def run(self, query: str):
        docs = self.retriever.retrieve(query)
        answer = self.generator.generate(query, docs)

        sources = [doc.metadata for doc in docs]

        return {
            "answer": answer,
            "sources": sources
        }