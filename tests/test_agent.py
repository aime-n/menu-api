from app.agents.agent import get_graph


def test_get_graph_returns_stategraph():
    graph = get_graph()
    # Verifica se o objeto retornado tem método 'invoke' e atributo 'config'
    assert hasattr(graph, "invoke")
    assert hasattr(graph, "config")


def test_graph_invoke_returns_expected_keys():
    graph = get_graph()
    # Simula uma entrada mínima compatível com o State esperado
    inputs = {"messages": [{"role": "user", "content": "Hello"}]}
    result = graph.invoke(inputs)
    assert isinstance(result, dict)
    assert "messages" in result
