from sqlmodel import Session, SQLModel, create_engine

from app.db.models import Ingredient, Recipe, RecipeIngredientLink


def test_ingredient_model_fields():
    ing = Ingredient(name="Tomato")
    assert ing.name == "Tomato"
    assert ing.id is None


def test_recipe_model_fields():
    recipe = Recipe(name="Salad", instructions="Mix all.")
    assert recipe.name == "Salad"
    assert recipe.instructions == "Mix all."
    assert recipe.id is None


def test_recipe_ingredient_link_fields():
    link = RecipeIngredientLink(recipe_id=1, ingredient_id=2, quantity="2", unit="pcs")
    assert link.recipe_id == 1
    assert link.ingredient_id == 2
    assert link.quantity == "2"
    assert link.unit == "pcs"


def test_relationships_work():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        ing = Ingredient(name="Salt")
        recipe = Recipe(name="Soup", instructions="Boil water.")
        session.add(ing)
        session.add(recipe)
        session.commit()
        link = RecipeIngredientLink(
            recipe_id=recipe.id, ingredient_id=ing.id, quantity="1", unit="tsp"
        )
        session.add(link)
        session.commit()
        # Test if relationships are established
        loaded_recipe = session.get(Recipe, recipe.id)
        loaded_ingredient = session.get(Ingredient, ing.id)
        assert loaded_ingredient in loaded_recipe.ingredients
        assert loaded_recipe in loaded_ingredient.recipes
