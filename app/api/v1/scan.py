from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import shutil
import uuid
import os

from app.core.database import SessionLocal
from app.schemas.scan import ScanRecordCreate, ScanRecordResponse
from app.crud import scan as scan_crud
from app.services.summary_service import summarize_image_from_server

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE scan record
@router.post("/scans/", response_model=ScanRecordResponse)
def create_scan(scan: ScanRecordCreate, db: Session = Depends(get_db)):
    return scan_crud.create_scan_record(db=db, scan=scan)

# READ ALL scan records
@router.get("/scans/", response_model=List[ScanRecordResponse])
def read_scans(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return scan_crud.get_scan_records(db, skip=skip, limit=limit)

# READ ONE scan record
@router.get("/scans/{record_id}", response_model=ScanRecordResponse)
def read_scan(record_id: int, db: Session = Depends(get_db)):
    scan = scan_crud.get_scan_record(db, record_id)
    if scan is None:
        raise HTTPException(status_code=404, detail="Scan record not found")
    return scan

# OCR + 요약 서버 호출
@router.post("/scan/ocr-summary")
async def scan_and_summarize(file: UploadFile = File(...)):
    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)
    temp_path = os.path.join(temp_dir, f"{uuid.uuid4().hex}.png")

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        result = summarize_image_from_server(temp_path)
    finally:
        os.remove(temp_path)

    return result
