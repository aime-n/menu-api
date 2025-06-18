from app.core.config import get_settings, Settings

def test_get_settings_returns_settings_instance():
    settings = get_settings()
    assert isinstance(settings, Settings)

def test_settings_fields_exist():
    settings = get_settings()
    # Testa se os principais campos existem
    assert hasattr(settings, "SUPABASE_URL")
    assert hasattr(settings, "SUPABASE_KEY")
    assert hasattr(settings, "DATABASE_URL")
    assert hasattr(settings, "LLM_PROVIDER")
    assert hasattr(settings, "OPENAI_API_KEY")
    assert hasattr(settings, "PROJECT_NAME")
    assert hasattr(settings, "PROJECT_VERSION")
    assert hasattr(settings, "DEFAULT_MODEL")