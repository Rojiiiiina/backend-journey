from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

DATABASE_URL = "postgresql://postgres:9840@localhost/backenddb"

engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass

def get_db():
    with Session(engine) as session:
        yield session