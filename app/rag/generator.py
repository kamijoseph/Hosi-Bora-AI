from langchain_openai import ChatOpenAI
from app.core.config import settings
from app.rag.prompt import build_prompt

class Generator:
    def __init__(self):
        self.llm = ChatOpenAI(
            model=settings.LLM_MODEL,
            openai_api_key=settings.OPENAI_API_KEY,
            temperature=0
        )

    def generate(self, query: str, docs):
        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = build_prompt(context, query)

        response = self.llm.invoke(prompt)

        return response.content