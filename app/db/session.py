from sqlmodel import create_engine, Session, SQLModel
from api.core.config import settings
from supabase import create_client, Client

# Import your schemas so that SQLModel knows about them
from api.schemas import recipe_schema 

# The SQLModel.metadata object contains all the table definitions.
# We will import this into Alembic's environment script.
metadata = SQLModel.metadata

# url: str = settings.SUPABASE_URL.get_secret_value()
# key: str = settings.SUPABASE_KEY.get_secret_value()
# supabase: Client = create_client(url, key)

# Create the SQLAlchemy engine using the DATABASE_URL from settings
engine = create_engine(settings.DATABASE_URL, echo=False)

def get_session():
    """Dependency to get a database session for each request."""
    with Session(engine) as session:
        yield session