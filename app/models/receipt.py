from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Receipt(Base):
    __tablename__ = "Receipt"

    receipt_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("User.user_id"), nullable=False)
    ocr_text = Column(Text)
    created_at = Column(DateTime, server_default=func.now())

    items = relationship("ReceiptItem", back_populates="receipt", cascade="all, delete-orphan")


class ReceiptItem(Base):
    __tablename__ = "ReceiptItem"

    item_id = Column(Integer, primary_key=True, index=True)
    receipt_id = Column(Integer, ForeignKey("Receipt.receipt_id"), nullable=False)
    product_name = Column(String(100), nullable=False)
    quantity = Column(Integer, default=1)
    unit_price = Column(DECIMAL(10, 2), default=0.00)

    receipt = relationship("Receipt", back_populates="items")
