from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings


load_dotenv()


class DatabaseConfig(BaseSettings):
    DB_NAME: str = os.environ.get("DB_NAME")
    DB_URL: str = f"sqlite+aiosqlite:///{DB_NAME}"


class SentimentAnalysisAPIConfig(BaseSettings):
    URL: str = "https://api.apilayer.com/sentiment/analysis"
    API_KEY: str = os.environ.get("SENTIMENT_ANALYSIS_API_KEY")


class IPAPIConfig(BaseSettings):
    URL: str = "http://ip-api.com/json"
    FIELDS: int = 1105937


db_config = DatabaseConfig()
sentiment_analysis_api_config = SentimentAnalysisAPIConfig()
ip_api_config = IPAPIConfig()
