from langchain_openai import ChatOpenAI
from app.config import settings

def get_deepseek_client():
    return ChatOpenAI(
        model=settings.DEEPSEEK_MODEL,
        openai_api_key=settings.DEEPSEEK_API_KEY,
        openai_api_base=settings.DEEPSEEK_BASE_URL,
        streaming=False
    )
