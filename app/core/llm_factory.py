from langchain_openai import ChatOpenAI
from app.llm.client import ChatOpenRouter
from app.core.config import settings
from langchain_core.language_models.chat_models import BaseChatModel
from app.schemas.llm import ModelName, ModelProvider
from typing import Optional


# TODO logger

def get_llm(model_name: Optional[ModelName] = None) -> BaseChatModel:
    """
    Factory function to get an LLM instance based on configured provider.
    """
    effective_model_name = model_name or settings.DEFAULT_MODEL
    provider = settings.LLM_PROVIDER.lower()

    if provider == ModelProvider.OPENROUTER:
        return ChatOpenRouter(model=effective_model_name.value)

    elif provider == ModelProvider.OPENAI:
        # Needs credits
        return ChatOpenAI(
            model=effective_model_name.value,
            api_key=settings.OPENAI_API_KEY.get_secret_value())
    
    # add bedrock, gemini, azure, etc. here in the future
    else:
        raise ValueError(f"Unsupported LLM provider: {settings.LLM_PROVIDER}")
    
