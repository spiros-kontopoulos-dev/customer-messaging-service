from collections.abc import Iterator
from datetime import UTC, datetime

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.db import Base
from app.models import Brand, Customer, Order, Store

@pytest.fixture()
def db() -> Iterator[Session]:
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        brand = Brand(id=1, name="Slice House")
        store = Store(id=1, brand=brand, name="Downtown")
        customer = Customer(id=1, phone="+15550001111", name="Alex")
        session.add_all([brand, store, customer])
        session.flush()
        session.add(
            Order(
                id=1,
                customer=customer,
                store=store,
                item_name="Margherita Pizza",
                status="completed",
                created_at=datetime(2026, 8, 10, 18, 30, tzinfo=UTC),
            )
        )
        session.commit()
        yield session
