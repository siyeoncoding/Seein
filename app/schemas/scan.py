from pydantic import BaseModel
from typing_extensions import Optional, Literal
from datetime import datetime

class ScanRecordBase(BaseModel):
    user_id: int
    scan_type: Literal["document", "product", "space"]
    result_text: Optional[str] = None
    image_url: Optional[str] = None

class ScanRecordCreate(ScanRecordBase):
    pass

class ScanRecordResponse(ScanRecordBase):
    record_id: int
    scan_date: datetime

    class Config:
        from_attributes = True  # Pydantic v2 이상
