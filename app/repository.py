from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Customer, Order, Store


def get_store(db: Session, store_id: int) -> Store | None:
    return db.get(Store, store_id)


def get_customer_by_phone(db: Session, phone: str) -> Customer | None:
    return db.scalar(select(Customer).where(Customer.phone == phone))


def get_latest_completed_order(db: Session, customer_id: int) -> Order | None:
    stmt = (
        select(Order)
        .where(
            Order.customer_id == customer_id,
            Order.status == "completed",
        )
        .order_by(Order.created_at.desc())
        .limit(1)
    )
    return db.scalar(stmt)
