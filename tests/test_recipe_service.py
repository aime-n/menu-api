import pytest
from sqlmodel import Session, SQLModel, create_engine

from app.db.models import RecipeIngredientLink
from app.services import recipe_service


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


def test_get_or_create_ingredient_creates(session):
    ingredient = recipe_service.get_or_create_ingredient(session, "Tomato")
    assert ingredient.name == "tomato"
    # Should not create duplicate
    ingredient2 = recipe_service.get_or_create_ingredient(session, "Tomato")
    assert ingredient.id == ingredient2.id


def test_create_recipe_and_links(session):
    ingredients_data = [
        ("Tomato", "2", "pcs"),
        ("Salt", "1", "tsp"),
    ]
    recipe = recipe_service.create_recipe(
        session,
        name="Salad",
        instructions="Mix all.",
        ingredients_data=ingredients_data,
    )
    assert recipe.name == "Salad"
    # Check links
    links = session.exec(
        RecipeIngredientLink.__table__.select().where(
            RecipeIngredientLink.recipe_id == recipe.id
        )
    ).all()
    assert len(links) == 2


def test_get_all_recipes(session):
    recipe_service.create_recipe(session, "R1", "Do it", [("A", "1", "x")])
    recipe_service.create_recipe(session, "R2", "Do it", [("B", "2", "y")])
    recipes = recipe_service.get_all_recipes(session)
    assert len(recipes) == 2


def test_get_recipe_by_name(session):
    recipe_service.create_recipe(session, "Cake", "Bake it", [("Flour", "200g", "g")])
    recipe = recipe_service.get_recipe_by_name(session, "Cake")
    assert recipe is not None
    assert recipe.name == "Cake"


def test_get_recipe_by_name_not_found(session):
    recipe = recipe_service.get_recipe_by_name(session, "NotExist")
    assert recipe is None


def test_delete_recipe_by_id(session):
    recipe = recipe_service.create_recipe(
        session, "Pie", "Bake", [("Apple", "2", "pcs")]
    )
    deleted = recipe_service.delete_recipe_by_id(session, recipe.id)
    assert deleted is True
    # Try again, should return False
    deleted = recipe_service.delete_recipe_by_id(session, recipe.id)
    assert deleted is False
