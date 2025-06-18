from typing import Optional

from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from app.core.config import settings


class ChatOpenRouter(ChatOpenAI):
    def __init__(self,
                 model: str, # Add model as a parameter if it's dynamic
                 api_key: Optional[SecretStr] = None, # Still allow overriding for flexibility
                 **kwargs):
        api_key_value = api_key or settings.OPENROUTER_API_KEY.get_secret_value()
        super().__init__(base_url=settings.BASE_URL_OPENROUTER, 
                         api_key=api_key_value, 
                         model=model, 
                         **kwargs)
