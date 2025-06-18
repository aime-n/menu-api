# src/api/schemas/chat.py
from datetime import datetime

from langchain_core.messages import BaseMessage
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Request model for the chat endpoint."""
    message: str
    thread_id: str = Field(
        description="A unique identifier for the conversation thread to maintain state."
    )
    # mudar modelo?


class ChatResponse(BaseModel):
    """Response model for the chat endpoint."""
    output: BaseMessage  # any type
    thread_id: str
    timestamp: datetime = datetime.now()
