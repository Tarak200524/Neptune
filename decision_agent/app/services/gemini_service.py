from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import settings

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
    google_api_key=settings.GEMINI_API_KEY,
    temperature=0.7,
    timeout=30,
    max_retries=2
)
