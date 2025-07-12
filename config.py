from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings


load_dotenv()


class DatabaseConfig(BaseSettings):
    DB_NAME: str = os.environ.get("DB_NAME")
    DB_URL: str = f"sqlite+aiosqlite:///{DB_NAME}"


db_config = DatabaseConfig()
