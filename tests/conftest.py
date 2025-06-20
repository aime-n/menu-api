import os

from dotenv import load_dotenv

# Configura variáveis de ambiente para testes
os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")
os.environ.setdefault("LLM_PROVIDER", "openrouter")
os.environ.setdefault("OPENAI_API_KEY", "test-key")
os.environ.setdefault("OPENROUTER_API_KEY", "test-key")
os.environ.setdefault("SUPABASE_URL", "https://test.supabase.co")
os.environ.setdefault("SUPABASE_KEY", "test-key")
os.environ.setdefault("SUPABASE_DB_PASSWORD", "test-password")
os.environ.setdefault("SUPABASE_HOST", "test-host")

# Carrega .env apenas se existir (para desenvolvimento local)
if os.path.exists(".env"):
    load_dotenv(".env")
