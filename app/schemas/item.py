from pydantic import BaseModel
from typing import Optional, List
from typing_extensions import Literal

# ItemIngredient
class ItemIngredientBase(BaseModel):
    ingredient_name: str
    risk_level: Literal["low", "medium", "high"]
    allergy_flag: bool = False

class ItemIngredientCreate(ItemIngredientBase):
    pass

class ItemIngredientResponse(ItemIngredientBase):
    ingredient_id: int

    class Config:
        from_attributes = True

# Item
class ItemBase(BaseModel):
    name: str
    image_url: Optional[str] = None
    category: Optional[str] = None
    registered_by: Optional[int] = None
    ar_tag_location: Optional[str] = None

class ItemCreate(ItemBase):
    ingredients: List[ItemIngredientCreate] = []

class ItemResponse(ItemBase):
    item_id: int
    ingredients: List[ItemIngredientResponse] = []

    class Config:
        from_attributes = True

# UserAllergy
class UserAllergyBase(BaseModel):
    ingredient_name: str

class UserAllergyCreate(UserAllergyBase):
    user_id: int

class AllergyCheckResponse(BaseModel):
    has_allergy: bool
    matching_ingredients: List[str]
