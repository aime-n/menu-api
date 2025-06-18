import pytest

from app.core import llm_factory
from app.schemas.llm import ModelName, ModelProvider


class DummySettings:
    DEFAULT_MODEL = ModelName.DEEPSEEK_V3_MODEL
    LLM_PROVIDER = ModelProvider.OPENROUTER
    OPENAI_API_KEY = type(
        "SecretStr", (), {"get_secret_value": lambda self: "openai-key"}
    )()
    OPENROUTER_API_KEY = type(
        "SecretStr", (), {"get_secret_value": lambda self: "openrouter-key"}
    )()


def test_get_llm_openrouter(monkeypatch):
    monkeypatch.setattr("app.core.llm_factory.settings", DummySettings)
    DummySettings.LLM_PROVIDER = ModelProvider.OPENROUTER
    llm = llm_factory.get_llm()
    assert "openrouter" in llm.__class__.__name__.lower()


def test_get_llm_openai(monkeypatch):
    monkeypatch.setattr("app.core.llm_factory.settings", DummySettings)
    DummySettings.LLM_PROVIDER = ModelProvider.OPENAI
    llm = llm_factory.get_llm()
    assert "openai" in llm.__class__.__name__.lower()


def test_get_llm_invalid_provider(monkeypatch):
    monkeypatch.setattr("app.core.llm_factory.settings", DummySettings)
    DummySettings.LLM_PROVIDER = "invalid"
    with pytest.raises(ValueError):
        llm_factory.get_llm()
