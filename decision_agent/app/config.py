import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DEEPSEEK_API_KEY: str
    DEEPSEEK_BASE_URL: str = "https://api.deepseek.com"
    DEEPSEEK_MODEL: str = "deepseek-chat"
    
    TELEGRAM_BOT_NAME: str
    TELEGRAM_BOT_TOKEN: str
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
