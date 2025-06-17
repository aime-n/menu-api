from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from ..core.supabase_client import get_session
from ..services import recipe_service
from ..schemas.recipe_schema import RecipeCreate, RecipePublic, Recipe

router = APIRouter()

@router.post("/", response_model=RecipePublic)
def handle_create_recipe(recipe_data: RecipeCreate, session: Session = Depends(get_session)):
    """
    API endpoint to create a new recipe.
    """
    try:
        ingredients_data = [
            (ing.ingredient_name, ing.quantity, ing.unit)
            for ing in recipe_data.ingredients
        ]
        recipe = recipe_service.create_recipe(
            session=session,
            name=recipe_data.name,
            instructions=recipe_data.instructions,
            ingredients_data=ingredients_data
        )
        return recipe
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[RecipePublic])
def handle_get_all_recipes(session: Session = Depends(get_session)):
    """
    API endpoint to retrieve all recipes.
    """
    return recipe_service.get_all_recipes(session=session)

@router.get("/{recipe_name}", response_model=RecipePublic)
def handle_get_recipe_by_name(recipe_name: str, session: Session = Depends(get_session)):
    """
    API endpoint to get a single recipe by its name.
    """
    recipe = recipe_service.get_recipe_by_name(session=session, recipe_name=recipe_name)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


@router.post("/bulk", response_model=List[RecipePublic])
def handle_create_recipes_bulk(
    recipes_data: List[RecipeCreate], session: Session = Depends(get_session)
):
    """
    API endpoint to create multiple recipes at once.
    Recebe uma lista de RecipeCreate.
    """
    created_recipes = []
    errors = []
    for idx, recipe_data in enumerate(recipes_data):
        try:
            ingredients_data = [
                (ing.ingredient_name, ing.quantity, ing.unit)
                for ing in recipe_data.ingredients
            ]
            recipe = recipe_service.create_recipe(
                session=session,
                name=recipe_data.name,
                instructions=recipe_data.instructions,
                ingredients_data=ingredients_data
            )
            created_recipes.append(recipe)
        except Exception as e:
            errors.append({"index": idx, "name": getattr(recipe_data, "name", None), "error": str(e)})
    if errors:
        raise HTTPException(
            status_code=400,
            detail={"created": [r.name for r in created_recipes], "errors": errors}
        )
    return created_recipes


@router.delete("/id/{recipe_id}", response_model=dict)
def handle_delete_recipe_by_id(recipe_id: int, session: Session = Depends(get_session)):
    """
    API endpoint to delete a recipe by its ID.
    """
    try:
        deleted = recipe_service.delete_recipe_by_id(session=session, recipe_id=recipe_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Recipe not found")
        return {"ok": True, "message": f"Recipe with id '{recipe_id}' deleted."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))