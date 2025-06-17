from langgraph.graph import StateGraph, START
from api.my_agent.utils.state import State
from api.my_agent.utils.nodes import chatbot
from langchain_core.runnables import RunnableConfig


from api.utils.visualize_graph import visualize_graph

# from functools import lru_cache
# TODO @lru_cache()?
def get_graph() -> StateGraph:
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


if __name__ == "__main__":
    from uuid import uuid4

    print("Graph compiled and saved as graph.png")
    # result = graph.invoke({"messages": ["Hello, how are you?"]})
    # result.pretty_print()
    

    inputs = {"messages": [("user", "Find me a recipe for chocolate chip cookies")]}
    result = graph.invoke(
        inputs,
    )
    result["messages"][-1].content.pretty_print()