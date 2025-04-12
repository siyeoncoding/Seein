from sqlalchemy.orm import Session
from app.models.scan import ScanRecord
from app.schemas.scan import ScanRecordCreate

# CREATE
def create_scan_record(db: Session, scan: ScanRecordCreate):
    db_scan = ScanRecord(**scan.dict())
    db.add(db_scan)
    db.commit()
    db.refresh(db_scan)
    return db_scan

# READ ALL
def get_scan_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ScanRecord).offset(skip).limit(limit).all()

# READ ONE
def get_scan_record(db: Session, record_id: int):
    return db.query(ScanRecord).filter(ScanRecord.record_id == record_id).first()
