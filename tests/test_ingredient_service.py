import pytest
from fastapi import HTTPException
from sqlmodel import Session, SQLModel, create_engine

from app.db.models import Ingredient
from app.schemas.recipe import IngredientDetail
from app.services import ingredient_service


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


def test_create_ingredient_service(session):
    detail = IngredientDetail(name="Tomato")
    result = ingredient_service.create_ingredient_service(detail, session)
    assert result.name == "Tomato"


def test_create_ingredient_service_duplicate(session):
    detail = IngredientDetail(name="Tomato")
    ingredient_service.create_ingredient_service(detail, session)
    with pytest.raises(HTTPException) as exc:
        ingredient_service.create_ingredient_service(detail, session)
    assert exc.value.status_code == 400


def test_list_ingredients_service(session):
    session.add(Ingredient(name="Salt"))
    session.add(Ingredient(name="Pepper"))
    session.commit()
    result = ingredient_service.list_ingredients_service(session)
    names = [i.name for i in result]
    assert "Salt" in names and "Pepper" in names


def test_get_ingredient_service(session):
    ingredient = Ingredient(name="Sugar")
    session.add(ingredient)
    session.commit()
    result = ingredient_service.get_ingredient_service(ingredient.id, session)
    assert result.name == "Sugar"


def test_get_ingredient_service_not_found(session):
    with pytest.raises(HTTPException) as exc:
        ingredient_service.get_ingredient_service(999, session)
    assert exc.value.status_code == 404


def test_update_ingredient_service(session):
    ingredient = Ingredient(name="Egg")
    session.add(ingredient)
    session.commit()
    detail = IngredientDetail(name="Eggs")
    result = ingredient_service.update_ingredient_service(
        ingredient.id, detail, session
    )
    assert result.name == "Eggs"


def test_update_ingredient_service_not_found(session):
    detail = IngredientDetail(name="Milk")
    with pytest.raises(HTTPException) as exc:
        ingredient_service.update_ingredient_service(999, detail, session)
    assert exc.value.status_code == 404


def test_delete_ingredient_service(session):
    ingredient = Ingredient(name="Butter")
    session.add(ingredient)
    session.commit()
    result = ingredient_service.delete_ingredient_service(ingredient.id, session)
    assert result["ok"] is True


def test_delete_ingredient_service_not_found(session):
    with pytest.raises(HTTPException) as exc:
        ingredient_service.delete_ingredient_service(999, session)
    assert exc.value.status_code == 404
