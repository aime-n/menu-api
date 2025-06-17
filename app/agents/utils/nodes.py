from api.services.llm_factory import get_llm
from api.my_agent.utils.state import State
from api.core.config import settings


llm = get_llm(settings.DEFAULT_MODEL)

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}
