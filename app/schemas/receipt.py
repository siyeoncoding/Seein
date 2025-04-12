from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from decimal import Decimal

class ReceiptItemBase(BaseModel):
    product_name: str
    quantity: int = 1
    unit_price: Decimal = 0.00

class ReceiptItemCreate(ReceiptItemBase):
    pass

class ReceiptItemResponse(ReceiptItemBase):
    item_id: int

    class Config:
        from_attributes = True

class ReceiptBase(BaseModel):
    user_id: int
    ocr_text: Optional[str] = None

class ReceiptCreate(ReceiptBase):
    items: List[ReceiptItemCreate]

class ReceiptResponse(ReceiptBase):
    receipt_id: int
    created_at: datetime
    items: List[ReceiptItemResponse] = []

    class Config:
        from_attributes = True
