# src/api/schemas/chat.py
from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Any
from api.schemas.llm import ModelName, ModelProvider
from datetime import datetime
from langchain_core.messages import BaseMessage, AIMessage, HumanMessage


class ChatRequest(BaseModel):
    """Request model for the chat endpoint."""
    messages: List[HumanMessage]
    thread_id: str = Field(
        description="A unique identifier for the conversation thread to maintain state."
    )
    # mudar modelo?


class ChatResponse(BaseModel):
    """Response model for the chat endpoint."""
    output: BaseMessage  # any type
    thread_id: str
    timestamp: datetime = datetime.now()
