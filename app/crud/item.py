from sqlalchemy.orm import Session
from app.models.item import Item, ItemIngredient, UserAllergy
from app.schemas.item import ItemCreate

# CREATE
def create_item(db: Session, item_data: ItemCreate):
    db_item = Item(
        name=item_data.name,
        image_url=item_data.image_url,
        category=item_data.category,
        registered_by=item_data.registered_by,
        ar_tag_location=item_data.ar_tag_location
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    for ing in item_data.ingredients:
        db_ingredient = ItemIngredient(
            item_id=db_item.item_id,
            ingredient_name=ing.ingredient_name,
            risk_level=ing.risk_level,
            allergy_flag=ing.allergy_flag
        )
        db.add(db_ingredient)

    db.commit()
    db.refresh(db_item)
    return db_item

# READ ALL
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()

# READ ONE
def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.item_id == item_id).first()

# USER 알레르기 등록
def add_user_allergy(db: Session, user_id: int, ingredient_name: str):
    allergy = UserAllergy(user_id=user_id, ingredient_name=ingredient_name)
    db.add(allergy)
    db.commit()
    return allergy

# 알레르기 감지
def check_allergy_for_item(db: Session, item_id: int, user_id: int):
    item = get_item(db, item_id)
    if not item:
        return None

    user_allergies = db.query(UserAllergy.ingredient_name).filter(UserAllergy.user_id == user_id).all()
    user_allergy_set = set(a[0] for a in user_allergies)

    matching = [i.ingredient_name for i in item.ingredients if i.ingredient_name in user_allergy_set]
    return {
        "has_allergy": len(matching) > 0,
        "matching_ingredients": matching
    }
