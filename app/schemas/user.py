from pydantic import BaseModel
from typing import Optional
from enum import Enum

class Gender(str, Enum):
    M = "M"
    F = "F"
    Other = "Other"

class VisionStatus(str, Enum):
    normal = "normal"
    low = "low"
    blind = "blind"

class UserBase(BaseModel):
    name: str
    gender: Optional[Gender]
    vision_status: VisionStatus
    language_setting: Optional[str] = "ko"

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    user_id: int

    class Config:
        from_attributes = True
