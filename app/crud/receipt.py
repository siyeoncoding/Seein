from sqlalchemy.orm import Session
from app.models.receipt import Receipt, ReceiptItem
from app.schemas.receipt import ReceiptCreate

# CREATE
def create_receipt(db: Session, receipt_data: ReceiptCreate):
    db_receipt = Receipt(user_id=receipt_data.user_id, ocr_text=receipt_data.ocr_text)
    db.add(db_receipt)
    db.commit()
    db.refresh(db_receipt)

    for item in receipt_data.items:
        db_item = ReceiptItem(
            receipt_id=db_receipt.receipt_id,
            product_name=item.product_name,
            quantity=item.quantity,
            unit_price=item.unit_price,
        )
        db.add(db_item)
    db.commit()
    db.refresh(db_receipt)
    return db_receipt

# READ ALL
def get_receipts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Receipt).offset(skip).limit(limit).all()

# READ ONE
def get_receipt(db: Session, receipt_id: int):
    return db.query(Receipt).filter(Receipt.receipt_id == receipt_id).first()
