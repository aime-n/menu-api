from sqlalchemy import text

from app.db.session import engine

with engine.connect() as conn:
    conn.execute(text("DROP TABLE IF EXISTS alembic_version CASCADE"))
    conn.commit()
    print("Dropped alembic_version table") 