from fastapi.testclient import TestClient
from app.main import app

import pytest

# --- ROOT --- #
root_url = "/"
health_url = "/health"

# --- BOOKS --- #
get_all_books_url = "/books"

@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
