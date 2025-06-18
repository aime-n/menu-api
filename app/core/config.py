from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from app.schemas.llm import ModelProvider, ModelName


# Settings específicas para o banco de dados
class DatabaseSettings(BaseSettings):
    SUPABASE_URL: SecretStr = Field(default_factory=lambda: SecretStr(""))
    SUPABASE_KEY: SecretStr = Field(default_factory=lambda: SecretStr(""))
    SUPABASE_DB_PASSWORD: SecretStr = Field(default_factory=lambda: SecretStr(""))
    SUPABASE_HOST: SecretStr = Field(default_factory=lambda: SecretStr(""))
    DATABASE_URL: SecretStr = Field(default_factory=lambda: SecretStr(""))


# Settings específicas para LLM
class LLMSettings(BaseSettings):
    LLM_PROVIDER: ModelProvider = ModelProvider.OPENROUTER
    OPENAI_API_KEY: SecretStr = Field(default_factory=lambda: SecretStr(""))
    OPENROUTER_API_KEY: SecretStr = Field(default_factory=lambda: SecretStr(""))
    BASE_URL_OPENROUTER: str = "https://openrouter.ai/api/v1"
    TIMEOUT: int = 600
    DEFAULT_MODEL: ModelName = ModelName.DEEPSEEK_V3_MODEL


# Settings gerais que herdam das específicas
class Settings(DatabaseSettings, LLMSettings):
    PROJECT_NAME: str = "Menu AI API"
    PROJECT_VERSION: str = "0.1.0"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra='ignore'
    )


@lru_cache()
def get_settings():
    """
    Returns a cached instance of the Settings class.
    This ensures that .env is loaded only once.
    """
    return Settings()


settings = get_settings()
