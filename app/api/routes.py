from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.rag.pipeline import RAGPipeline

router = APIRouter()
rag = RAGPipeline()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    result = rag.run(request.question)
    return result