from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import declarative_base



Base = declarative_base()

class User(Base):
    __tablename__ = "User"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    gender = Column(Enum('M', 'F', 'Other'), nullable=True)
    vision_status = Column(Enum('normal', 'low', 'blind'), nullable=False)
    language_setting = Column(String(20), default='ko')
