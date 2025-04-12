from sqlalchemy import Column, Integer, Text, DateTime, Enum, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class ScanRecord(Base):
    __tablename__ = "ScanRecord"

    record_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("User.user_id"), nullable=False)
    scan_date = Column(DateTime, server_default=func.now())
    scan_type = Column(Enum("document", "product", "space"), nullable=False)
    result_text = Column(Text)
    image_url = Column(Text)
