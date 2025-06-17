from typing import Optional
from langchain_openai import ChatOpenAI
from api.core.config import settings


class ChatOpenRouter(ChatOpenAI):
    def __init__(self,
                 model_name: str, # Add model_name as a parameter if it's dynamic
                 openai_api_key: Optional[str] = None, # Still allow overriding for flexibility
                 **kwargs):
        api_key_value = openai_api_key or settings.OPENROUTER_API_KEY.get_secret_value()

        super().__init__(base_url=settings.BASE_URL_OPENROUTER, 
                         openai_api_key=api_key_value, 
                         model_name=model_name, 
                         **kwargs)
