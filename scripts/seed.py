from datetime import UTC, datetime

from sqlalchemy import delete

from app.db import get_session_factory
from app.models import Brand, Customer, Order, Store

PHONE = "+15550001111"

if __name__ == "__main__":
    with get_session_factory()() as db:
        db.execute(delete(Order))
        db.execute(delete(Customer))
        db.execute(delete(Store))
        db.execute(delete(Brand))

        brand = Brand(id=1, name="Slice House")
        downtown = Store(id=1, brand=brand, name="Downtown")
        riverside = Store(id=2, brand=brand, name="Riverside")
        customer = Customer(id=1, phone=PHONE, name="Alex")

        db.add_all([brand, downtown, riverside, customer])
        db.flush()

        db.add_all([
            Order(id=1, customer=customer, store=downtown, item_name="Margherita Pizza", status="completed", created_at=datetime(2026, 8, 10, 18, 30, tzinfo=UTC)),
            Order(id=2, customer=customer, store=riverside, item_name="Pepperoni Pizza", status="completed", created_at=datetime(2026, 8, 18, 19, 15, tzinfo=UTC)),
        ])
        db.commit()

    print("Seeded demo brand, stores, customer, and orders.")
