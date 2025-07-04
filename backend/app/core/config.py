import os
from dotenv import load_dotenv

load_dotenv()  # carrega .env.dev

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

settings = Settings()
