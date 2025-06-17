from typing import List, Optional

from sqlmodel import SQLModel


class IngredientRecipe(SQLModel):
    ingredient_name: str
    quantity: str
    unit: Optional[str] = None

class RecipeCreate(SQLModel):
    name: str
    instructions: str
    ingredients: List[IngredientRecipe] # (ingredient_name, quantity, unit)

class IngredientDetail(SQLModel):
    name: str

class RecipePublic(SQLModel):
    id: int
    name: str
    instructions: str
    ingredients: List[IngredientDetail] = []
