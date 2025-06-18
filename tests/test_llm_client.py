from app.llm.client import ChatOpenRouter


def test_chat_openrouter_init(monkeypatch):
    class DummySettings:
        BASE_URL_OPENROUTER = "https://dummy-url.com"
        OPENROUTER_API_KEY = type(
            "SecretStr", (), {"get_secret_value": lambda self: "dummy-key"}
        )()

    monkeypatch.setattr("app.llm.client.settings", DummySettings)

    client = ChatOpenRouter(model="test-model")
    assert client.openai_api_key.get_secret_value() == "dummy-key"
    assert client.openai_api_base == "https://dummy-url.com"
    assert client.model == "test-model"


def test_chat_openrouter_init_with_override(monkeypatch):
    class DummySettings:
        BASE_URL_OPENROUTER = "https://dummy-url.com"
        OPENROUTER_API_KEY = type(
            "SecretStr", (), {"get_secret_value": lambda self: "dummy-key"}
        )()

    monkeypatch.setattr("app.llm.client.settings", DummySettings)

    client = ChatOpenRouter(model="test-model", api_key="override-key")
    assert client.api_key.get_secret_value() == "override-key"
    assert client.openai_api_base == "https://dummy-url.com"
    assert client.model == "test-model"
