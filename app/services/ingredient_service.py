from fastapi import HTTPException
from sqlmodel import Session, select
from api.schemas.recipe_schema import Ingredient, IngredientDetail
from typing import List


def create_ingredient_service(ingredient: IngredientDetail, session: Session) -> IngredientDetail:
    db_ingredient = session.exec(select(Ingredient).where(Ingredient.name == ingredient.name)).first()
    if db_ingredient:
        raise HTTPException(status_code=400, detail="Ingredient already exists")
    new_ingredient = Ingredient(name=ingredient.name)
    session.add(new_ingredient)
    session.commit()
    session.refresh(new_ingredient)
    return IngredientDetail(name=new_ingredient.name)

def list_ingredients_service(session: Session) -> List[IngredientDetail]:
    ingredients = session.exec(select(Ingredient)).all()
    return [IngredientDetail(name=i.name) for i in ingredients]

def get_ingredient_service(ingredient_id: int, session: Session) -> IngredientDetail:
    ingredient = session.get(Ingredient, ingredient_id)
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return IngredientDetail(name=ingredient.name)

def update_ingredient_service(ingredient_id: int, ingredient: IngredientDetail, session: Session) -> IngredientDetail:
    db_ingredient = session.get(Ingredient, ingredient_id)
    if not db_ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    db_ingredient.name = ingredient.name
    session.add(db_ingredient)
    session.commit()
    session.refresh(db_ingredient)
    return IngredientDetail(name=db_ingredient.name)

def delete_ingredient_service(ingredient_id: int, session: Session) -> dict:
    ingredient = session.get(Ingredient, ingredient_id)
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    session.delete(ingredient)
    session.commit()
    return {"ok": True}