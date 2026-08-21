from pydantic import BaseModel

class MessageRequest(BaseModel):
    phone: str
    message: str

class MessageResponse(BaseModel):
    store_id: int
    store_name: str
    reply: str
    suggested_item: str | None = None
    source_order_id: int | None = None
