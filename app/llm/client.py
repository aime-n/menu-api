from typing import Optional
from langchain_openai import ChatOpenAI
from app.core.config import settings
from pydantic import SecretStr


class ChatOpenRouter(ChatOpenAI):
    def __init__(self,
                 model: str, # Add model as a parameter if it's dynamic
                 api_key: Optional[str] = None, # Still allow overriding for flexibility
                 **kwargs):
        api_key_value = api_key or settings.OPENROUTER_API_KEY.get_secret_value()
        secret_api_key = SecretStr(api_key_value)
        super().__init__(base_url=settings.BASE_URL_OPENROUTER, 
                         api_key=secret_api_key, 
                         model=model, 
                         **kwargs)
