from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from app.core.config import settings

def get_embedding_function():
    return OpenAIEmbeddings(
        model=settings.EMBEDDING_MODEL,
        openai_api_key=settings.OPENAI_API_KEY
    )

def get_vector_store():
    embedding_function = get_embedding_function()

    vectordb = Chroma(
        persist_directory=settings.CHROMA_DB_DIR,
        embedding_function=embedding_function
    )

    return vectordb