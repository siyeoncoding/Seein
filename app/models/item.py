from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum, Table
from sqlalchemy.orm import relationship
from app.core.database import Base

class Item(Base):
    __tablename__ = "Item"

    item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    image_url = Column(String(255))
    category = Column(String(50))
    registered_by = Column(Integer, ForeignKey("User.user_id"))
    ar_tag_location = Column(String(255))

    ingredients = relationship("ItemIngredient", back_populates="item", cascade="all, delete-orphan")


class ItemIngredient(Base):
    __tablename__ = "ItemIngredient"

    ingredient_id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("Item.item_id"), nullable=False)
    ingredient_name = Column(String(100), nullable=False)
    risk_level = Column(Enum("low", "medium", "high"), nullable=False)
    allergy_flag = Column(Boolean, default=False)

    item = relationship("Item", back_populates="ingredients")


class UserAllergy(Base):
    __tablename__ = "UserAllergy"

    user_id = Column(Integer, ForeignKey("User.user_id"), primary_key=True)
    ingredient_name = Column(String(100), primary_key=True)
