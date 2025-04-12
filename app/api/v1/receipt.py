from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.receipt import ReceiptCreate, ReceiptResponse
from app.crud import receipt as receipt_crud
from typing import List

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
@router.post("/receipts/", response_model=ReceiptResponse)
def create_receipt(receipt: ReceiptCreate, db: Session = Depends(get_db)):
    return receipt_crud.create_receipt(db=db, receipt_data=receipt)

# READ ALL
@router.get("/receipts/", response_model=List[ReceiptResponse])
def read_receipts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return receipt_crud.get_receipts(db, skip=skip, limit=limit)

# READ ONE
@router.get("/receipts/{receipt_id}", response_model=ReceiptResponse)
def read_receipt(receipt_id: int, db: Session = Depends(get_db)):
    receipt = receipt_crud.get_receipt(db, receipt_id)
    if receipt is None:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return receipt
