from app.core.config import settings

print(f"Environment: {settings.ENVIRONMENT}")
print(f"Database URL: {settings.DATABASE_URL.get_secret_value()}")
print(f"Using localhost: {'localhost' in settings.DATABASE_URL.get_secret_value()}")
print(f"Using Supabase: {'supabase' in settings.DATABASE_URL.get_secret_value()}") 