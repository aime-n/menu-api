from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class RecipeIngredientLink(SQLModel, table=True):
    """Link table for the many-to-many relationship between recipes and ingredients."""
    recipe_id: Optional[int] = Field(
        default=None, foreign_key="recipe.id", primary_key=True
    )
    ingredient_id: Optional[int] = Field(
        default=None, foreign_key="ingredient.id", primary_key=True
    )
    quantity: str = Field(index=True)
    unit: Optional[str] = None


class Ingredient(SQLModel, table=True):
    """Represents an ingredient."""
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    recipes: List["Recipe"] = Relationship(back_populates="ingredients", link_model=RecipeIngredientLink)


class Recipe(SQLModel, table=True):
    """Represents a recipe, which can contain multiple ingredients."""
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    instructions: str
    ingredients: List[Ingredient] = Relationship(back_populates="recipes", link_model=RecipeIngredientLink)
