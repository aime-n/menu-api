import pytest
from fastapi.testclient import TestClient
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine

from app.db.session import get_session
from app.main import app
from app.schemas.recipe import IngredientDetail

# 1. Crie engine global de teste
test_engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # mantém o mesmo banco em memória em todas as conexões
)

# 2. Crie as tabelas antes de qualquer teste
SQLModel.metadata.create_all(test_engine)


# 3. Fixture da sessão de teste
@pytest.fixture
def session():
    with Session(test_engine) as session:
        yield session


# 4. Fixture do client com override da dependência
@pytest.fixture
def client(session):
    def override_get_session():
        yield session

    app.dependency_overrides[get_session] = override_get_session
    return TestClient(app)


def test_create_ingredient(client):
    response = client.post("/ingredients/", json={"name": "Tomato"})
    assert response.status_code == 200
    assert response.json()["name"] == "Tomato"


def test_list_ingredients(client):
    client.post("/ingredients/", json={"name": "Salt"})
    client.post("/ingredients/", json={"name": "Pepper"})
    response = client.get("/ingredients/")
    assert response.status_code == 200
    names = [item["name"] for item in response.json()]
    assert "Salt" in names
    assert "Pepper" in names


def test_get_ingredient(client):
    create_resp = client.post("/ingredients/", json={"name": "Sugar", "id": 111})
    ingredient_id = create_resp.json().get("id", 1)  # fallback for id=1 if not present
    response = client.get(f"/ingredients/{ingredient_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Sugar"


def test_update_ingredient(client):
    create_resp = client.post("/ingredients/", json={"name": "Egg", "id": 222})
    ingredient_id = create_resp.json().get("id", 1)
    response = client.put(f"/ingredients/{ingredient_id}", json={"name": "Eggs"})
    assert response.status_code == 200
    assert response.json()["name"] == "Eggs"


def test_delete_ingredient(client):
    create_resp = client.post("/ingredients/", json={"name": "Butter", "id": 333})
    ingredient_id = create_resp.json().get("id", 1)
    response = client.delete(f"/ingredients/{ingredient_id}")
    assert response.status_code == 200
    assert response.json()["ok"] is True


def test_get_ingredient_not_found(client):
    response = client.get("/ingredients/9999")
    assert response.status_code == 404


def test_update_ingredient_not_found(client):
    response = client.put("/ingredients/9999", json={"name": "Milk"})
    assert response.status_code == 404


def test_delete_ingredient_not_found(client):
    response = client.delete("/ingredients/9999")
    assert response.status_code == 404
