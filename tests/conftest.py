from fastapi.testclient import TestClient
from app.main import app

import pytest

@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
