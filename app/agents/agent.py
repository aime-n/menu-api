from langgraph.graph import START, StateGraph

from app.agents.utils.nodes import chatbot
from app.agents.utils.state import State


# from functools import lru_cache
# TODO @lru_cache()?
def get_graph():
    """
    Returns a StateGraph instance for the agent.
    This function is used to compile the graph and visualize it.
    """

    graph_builder = StateGraph(State)

    graph_builder.add_node("chatbot", chatbot)

    # entry point for the graph
    graph_builder.add_edge(START, "chatbot")

    # compile the graph
    graph = graph_builder.compile(name="my_agent")
    # visualize_graph(graph, save=True, filename="graph.png")
    # graph = graph.with_config(RunnableConfig(log_input=True, log_output=True))  # TODO construir com um configuravel
    return graph
