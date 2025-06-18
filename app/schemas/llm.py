from enum import Enum


class ModelProvider(str, Enum):
    """Enum for supported LLM providers."""
    OPENROUTER = "openrouter"
    OPENAI = "openai"

    
class ModelName(str, Enum):
    """Enum for supported model providers."""
    LLAMA_MODEL = "nvidia/llama-3.3-nemotron-super-49b-v1:free"
    GEMMA_3_1B_MODEL = "google/gemma-3-1b-it:free"
    GEMMA_3_27B_MODEL = "google/gemma-3-27b-it:free"
    DEEPSEEK_V3_MODEL = "deepseek/deepseek-chat-v3-0324:free"
    DEEPSEEK_R1_MODEL = "deepseek/deepseek-r1-zero:free"

