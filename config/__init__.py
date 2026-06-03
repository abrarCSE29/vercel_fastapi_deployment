from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables / .env file."""

    mongodb_uri: str
    mongodb_database: str

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        # Optional: support both MONGODB_URI and mongodb_uri
        "case_sensitive": False,
    }


settings = Settings()
