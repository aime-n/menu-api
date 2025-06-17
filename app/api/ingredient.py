from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from typing import List

from api.schemas.recipe_schema import Ingredient, IngredientDetail
from api.core.supabase_client import get_session  # Certifique-se de ter essa função
from api.services.ingredient_service import (
    create_ingredient_service,
    get_ingredient_service,
    list_ingredients_service,
    update_ingredient_service,
    delete_ingredient_service,
)

router = APIRouter()

@router.post("/", response_model=IngredientDetail)
def create_ingredient(ingredient: IngredientDetail, session: Session = Depends(get_session)):
    return create_ingredient_service(ingredient, session)

@router.get("/", response_model=List[IngredientDetail])
def list_ingredients(session: Session = Depends(get_session)):
    return list_ingredients_service(session)

@router.get("/{ingredient_id}", response_model=IngredientDetail)
def get_ingredient(ingredient_id: int, session: Session = Depends(get_session)):
    return get_ingredient_service(ingredient_id, session)

@router.put("/{ingredient_id}", response_model=IngredientDetail)
def update_ingredient(ingredient_id: int, ingredient: IngredientDetail, session: Session = Depends(get_session)):
    return update_ingredient_service(ingredient_id, ingredient, session)

@router.delete("/{ingredient_id}", response_model=dict)
def delete_ingredient(ingredient_id: int, session: Session = Depends(get_session)):
    return delete_ingredient_service(ingredient_id, session)
