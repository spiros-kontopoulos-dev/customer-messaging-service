from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import models  # noqa: E402,F401
from app.db import Base, get_engine  # noqa: E402

if __name__ == "__main__":
    Base.metadata.create_all(bind=get_engine())
    print("Database tables are ready.")
