import pytest
from fastapi.testclient import TestClient
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine

from app.db.session import get_session
from app.main import app

test_engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # mantém o mesmo banco em memória em todas as conexões
)

SQLModel.metadata.create_all(test_engine)


@pytest.fixture
def session():
    with Session(test_engine) as session:
        yield session


@pytest.fixture
def client(session):
    def override_get_session():
        yield session

    app.dependency_overrides[get_session] = override_get_session
    return TestClient(app)


def test_create_recipe(client):
    payload = {
        "name": "Salad",
        "instructions": "Mix all.",
        "ingredients": [
            {"ingredient_name": "Tomato", "quantity": "2", "unit": "pcs"},
            {"ingredient_name": "Salt", "quantity": "1", "unit": "tsp"},
        ],
    }
    response = client.post("/recipes/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Salad"
    assert data["instructions"] == "Mix all."
    assert any(ing["name"].lower() == "tomato" for ing in data["ingredients"])


def test_get_all_recipes(client):
    # Cria uma receita para garantir que haja pelo menos uma
    client.post(
        "/recipes/",
        json={
            "name": "Soup",
            "instructions": "Boil water.",
            "ingredients": [
                {"ingredient_name": "Water", "quantity": "500", "unit": "ml"}
            ],
        },
    )
    response = client.get("/recipes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert any(r["name"] == "Soup" for r in response.json())


def test_get_recipe_by_name(client):
    client.post(
        "/recipes/",
        json={
            "name": "Cake",
            "instructions": "Bake it.",
            "ingredients": [
                {"ingredient_name": "Flour", "quantity": "200", "unit": "g"}
            ],
        },
    )
    response = client.get("/recipes/Cake")
    assert response.status_code == 200
    assert response.json()["name"] == "Cake"


def test_get_recipe_by_name_not_found(client):
    response = client.get("/recipes/NotExist")
    assert response.status_code == 404


def test_create_recipes_bulk(client):
    payload = [
        {
            "name": "Bulk1",
            "instructions": "Do 1.",
            "ingredients": [{"ingredient_name": "A", "quantity": "1", "unit": "x"}],
        },
        {
            "name": "Bulk2",
            "instructions": "Do 2.",
            "ingredients": [{"ingredient_name": "B", "quantity": "2", "unit": "y"}],
        },
    ]
    response = client.post("/recipes/bulk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(r["name"] == "Bulk1" for r in data)
    assert any(r["name"] == "Bulk2" for r in data)


def test_delete_recipe_by_id(client):
    # Cria uma receita para deletar
    resp = client.post(
        "/recipes/",
        json={
            "name": "DeleteMe",
            "instructions": "Remove.",
            "ingredients": [{"ingredient_name": "X", "quantity": "1", "unit": "z"}],
        },
    )
    recipe_id = resp.json()["id"]
    response = client.delete(f"/recipes/id/{recipe_id}")
    assert response.status_code == 200
    assert response.json()["ok"] is True


def test_delete_recipe_by_id_not_found(client):
    response = client.delete("/recipes/id/9999")
    assert response.status_code == 404
