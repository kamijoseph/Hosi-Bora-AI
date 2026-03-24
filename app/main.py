from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Hosi Bora AI",
    description="Medical Assistance RAG API",
    version="1.0"
)

app.include_router(router)