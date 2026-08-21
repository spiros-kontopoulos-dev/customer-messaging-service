import os
from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:postgres@localhost:5432/kubbly_mock",
)

class Base(DeclarativeBase):
    pass

@lru_cache(maxsize=1)
def get_engine() -> Engine:
    return create_engine(DATABASE_URL, pool_pre_ping=True)

def get_session_factory():
    return sessionmaker(bind=get_engine(), class_=Session, expire_on_commit=False)

def get_db():
    db = get_session_factory()()
    try:
        yield db
    finally:
        db.close()
