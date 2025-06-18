import pytest
from fastapi.testclient import TestClient

from app.core.logger import logger
from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_chat_invoke_success(client):

    payload = {"message": "Hi!", "thread_id": "test-thread"}
    response = client.post("/chat/invoke", json=payload)
    assert response.status_code == 200
    # check if the response contains output and thread_id
    assert "output" in response.json()
    assert "thread_id" in response.json()
    # verificar se thread_id é o mesmo que o enviado
    assert response.json()["thread_id"] == "test-thread"
