from app.db.vector_store import get_vector_store
from app.core.config import settings

class Retriever:
    def __init__(self):
        self.vectordb = get_vector_store()

    def retrieve(self, query: str):
        results = self.vectordb.similarity_search(
            query,
            k=settings.TOP_K
        )
        return results