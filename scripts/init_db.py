from app import models  # noqa: F401
from app.db import Base, get_engine

if __name__ == "__main__":
    Base.metadata.create_all(bind=get_engine())
    print("Database tables are ready.")
