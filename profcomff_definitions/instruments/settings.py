import os
from functools import lru_cache
from dotenv import load_dotenv


class Settings:
    load_dotenv(".env")
    """Application settings"""

    DB_DSN: str = os.getenv("DB_DSN", "postgresql://postgres:12345@localhost:5432/dwh")
    DB_REMOTE: str = os.getenv("DB_REMOTE", "")


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
