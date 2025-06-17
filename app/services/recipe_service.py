from typing import List, Optional, Tuple
from sqlmodel import Session, select
from ..schemas.recipe_schema import Recipe, Ingredient, RecipeIngredientLink


def get_or_create_ingredient(session: Session, name: str) -> Ingredient:
    """Retrieves an ingredient by name if it exists, otherwise creates a new one."""
    statement = select(Ingredient).where(Ingredient.name == name.lower())
    ingredient = session.exec(statement).first()
    if not ingredient:
        ingredient = Ingredient(name=name.lower())
        session.add(ingredient)
        session.commit()
        session.refresh(ingredient)
    return ingredient

def create_recipe(session: Session, name: str, instructions: str, ingredients_data: List[Tuple[str, str, str]]) -> Recipe:
    """Creates a new recipe and its ingredients."""
    try:
        recipe = Recipe(name=name, instructions=instructions)
        session.add(recipe)
        session.flush()  # Ensure the recipe has an ID before adding ingredients

        # Create links between the recipe and its ingredients
        for ingredient_name, quantity, unit in ingredients_data:
            ingredient = get_or_create_ingredient(session, ingredient_name)
            link = RecipeIngredientLink(
                quantity=quantity, 
                unit=unit, 
                recipe_id=recipe.id, 
                ingredient_id=ingredient.id)
            session.add(link)
        
        session.commit()
        session.refresh(recipe)
        return recipe
    except Exception as e:
        session.rollback()
        raise e

def get_all_recipes(session: Session) -> List[Recipe]:
    """Retrieves all recipes."""
    return session.exec(select(Recipe)).all()

def get_recipe_by_name(session: Session, recipe_name: str) -> Optional[Recipe]:
    """Retrieves a single recipe by its name."""
    statement = select(Recipe).where(Recipe.name == recipe_name)
    return session.exec(statement).first()

def delete_recipe_by_id(session: Session, recipe_id: int) -> bool:
    """
    Deleta uma receita pelo ID. Retorna True se deletou, False se não encontrou.
    """
    recipe = session.get(Recipe, recipe_id)
    if not recipe:
        return False
    session.delete(recipe)
    session.commit()
    return True