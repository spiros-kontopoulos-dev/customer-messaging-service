from sqlalchemy.orm import Session

from app import repository
from app.schemas import MessageResponse


def respond_to_message(
    db: Session,
    *,
    store_id: int,
    phone: str,
    message: str,
) -> MessageResponse:
    store = repository.get_store(db, store_id)
    if store is None:
        raise LookupError("store_not_found")

    customer = repository.get_customer_by_phone(db, phone)
    if customer is None:
        return MessageResponse(
            store_id=store.id,
            store_name=store.name,
            reply="I don't recognize this number yet. What would you like to order?",
        )

    normalized = " ".join(message.lower().split())
    if normalized not in {"my usual", "the usual", "usual"}:
        return MessageResponse(
            store_id=store.id,
            store_name=store.name,
            reply="I can help with your usual order. Try asking for 'my usual'.",
        )

    order = repository.get_latest_completed_order(db, customer.id)
    if order is None:
        return MessageResponse(
            store_id=store.id,
            store_name=store.name,
            reply="I couldn't find a previous completed order for you.",
        )

    return MessageResponse(
        store_id=store.id,
        store_name=store.name,
        reply=f"Your usual at {store.name} is {order.item_name}. Want me to reorder it?",
        suggested_item=order.item_name,
        source_order_id=order.id,
    )
