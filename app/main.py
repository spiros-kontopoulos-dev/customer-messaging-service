from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas import MessageRequest, MessageResponse
from app.service import respond_to_message

app = FastAPI(title="Restaurant Messaging Service")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/stores/{store_id}/messages", response_model=MessageResponse)
def send_message(
    store_id: int,
    payload: MessageRequest,
    db: Session = Depends(get_db),
) -> MessageResponse:
    try:
        return respond_to_message(
            db,
            store_id=store_id,
            phone=payload.phone,
            message=payload.message,
        )
    except LookupError as exc:
        if str(exc) == "store_not_found":
            raise HTTPException(status_code=404, detail="Store not found") from exc
        raise
