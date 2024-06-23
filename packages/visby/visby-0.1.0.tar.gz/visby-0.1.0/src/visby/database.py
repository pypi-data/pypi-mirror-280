import os
from typing import Any

from sqlmodel import SQLModel, create_engine

DATABASE_URL = os.getenv("POSTGRES_DATABASE_URL", "sqlite:///./visby.db")

engine = create_engine(DATABASE_URL)


def create_db_and_tables(engine: Any) -> Any:
    SQLModel.metadata.create_all(engine)
