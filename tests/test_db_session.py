from app.db.session import engine, get_session
from sqlmodel import SQLModel, Session

def test_engine_is_sqlalchemy_engine():
    # Verifica se o engine foi criado corretamente
    from sqlalchemy.engine import Engine
    assert isinstance(engine, Engine)

def test_get_session_yields_session():
    # Verifica se get_session retorna um objeto Session válido
    gen = get_session()
    session = next(gen)
    assert isinstance(session, Session)
    # Fecha o generator corretamente
    try:
        next(gen)
    except StopIteration:
        pass

def test_metadata_tables_exist():
    # Verifica se o metadata contém tabelas (após importar schemas)
    from app.db.session import metadata
    assert hasattr(metadata, "tables")
    assert isinstance(metadata.tables, dict)