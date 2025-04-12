from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List  # ✅ Python 3.7 이하에서도 호환되는 List
from typing_extensions import Literal  # ✅ Literal은 여기서 임포트해야 함

from app.core.database import SessionLocal
from app.schemas.item import (
    ItemCreate,
    ItemResponse,
    UserAllergyCreate,
    AllergyCheckResponse,
)
from app.crud import item as item_crud

router = APIRouter()

# ✅ Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ CREATE Item
@router.post("/items/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return item_crud.create_item(db=db, item_data=item)

# ✅ GET all items
@router.get("/items/", response_model=List[ItemResponse])
def get_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return item_crud.get_items(db, skip=skip, limit=limit)

# ✅ GET one item
@router.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    db_item = item_crud.get_item(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# ✅ POST user allergy 등록
@router.post("/allergy/")
def add_user_allergy(allergy: UserAllergyCreate, db: Session = Depends(get_db)):
    return item_crud.add_user_allergy(db=db, user_id=allergy.user_id, ingredient_name=allergy.ingredient_name)

# ✅ GET allergy check for item
@router.get("/items/{item_id}/allergy-check", response_model=AllergyCheckResponse)
def check_allergy(item_id: int, user_id: int, db: Session = Depends(get_db)):
    result = item_crud.check_allergy_for_item(db=db, item_id=item_id, user_id=user_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return result
