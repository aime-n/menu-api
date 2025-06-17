from app.core.llm_factory import get_llm
from app.agents.utils.state import State
from app.core.config import settings


llm = get_llm(settings.DEFAULT_MODEL)

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}
